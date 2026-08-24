"""``manage.py import_lessons`` — parse ``raw_data/`` into the database.

Idempotent: each lesson is matched on ``day_number`` via ``update_or_create``
and its children are rebuilt inside a transaction, so re-running produces
identical row counts (no duplicates, no drift).

    manage.py import_lessons              # import/refresh from raw_data/
    manage.py import_lessons --clear      # wipe all lessons first
    manage.py import_lessons --dry-run    # parse + report, write nothing
    manage.py import_lessons --strict     # fail on any parse anomaly
"""

from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.text import slugify

from BusinessEnglish.models import Lesson, Expression, Example, UpgradePair
from BusinessEnglish.services.lesson_parser import ParsedLesson, parse_all


class Command(BaseCommand):
    help = "Parse raw_data/ lesson files into the database (idempotent)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            default=str(Path(settings.BASE_DIR) / "raw_data"),
            help="Directory of dayN lesson files (default: <BASE_DIR>/raw_data).",
        )
        parser.add_argument(
            "--clear", action="store_true",
            help="Delete all existing lessons before importing.",
        )
        parser.add_argument(
            "--dry-run", action="store_true",
            help="Parse and report counts without writing to the database.",
        )
        parser.add_argument(
            "--strict", action="store_true",
            help="Raise on parse anomalies (missing fields / empty lessons).",
        )

    def handle(self, *args, **options):
        raw_dir = Path(options["path"])
        if not raw_dir.is_dir():
            raise CommandError(f"raw_data directory not found: {raw_dir}")

        lessons = parse_all(raw_dir)
        if not lessons:
            raise CommandError(f"No dayN lesson files found in {raw_dir}")

        if options["strict"]:
            self._validate(lessons)

        totals = {"lessons": 0, "expressions": 0, "examples": 0, "upgrades": 0}

        if options["dry_run"]:
            for parsed in lessons:
                self._tally(parsed, totals)
                self.stdout.write(
                    f"[dry-run] Day {parsed.day_number}: {len(parsed.expressions)} "
                    f"expressions, {len(parsed.upgrades)} upgrades"
                )
            self._report(totals, dry_run=True)
            return

        with transaction.atomic():
            if options["clear"]:
                deleted, _ = Lesson.objects.all().delete()
                self.stdout.write(self.style.WARNING(f"Cleared existing data ({deleted} rows)."))
            for parsed in lessons:
                self._import_one(parsed)
                self._tally(parsed, totals)

        self._report(totals, dry_run=False)

    # -- helpers ----------------------------------------------------------------

    def _import_one(self, parsed: ParsedLesson) -> None:
        """Upsert one lesson and rebuild its children."""
        lesson, _ = Lesson.objects.update_or_create(
            day_number=parsed.day_number,
            defaults={
                "date": parsed.date,
                "title": parsed.title,
                "mode": parsed.mode,
                "focus_theme": parsed.focus_theme,
                "dialogue_topic": parsed.dialogue_topic,
                "difficulty": parsed.difficulty,
                "lesson_focus": parsed.lesson_focus,
                "review_items": parsed.review_items,
                "avoiding_repeats": parsed.avoiding_repeats,
                "speaking_practice": parsed.speaking_practice,
                "output_correction": parsed.output_correction,
                "tomorrow_preview": parsed.tomorrow_preview,
                "source_filename": parsed.source_filename,
            },
        )

        # Rebuild children so edits/removals in raw_data are reflected exactly.
        # Expressions cascade-delete their examples.
        lesson.expressions.all().delete()
        lesson.upgrades.all().delete()

        for parsed_expr in parsed.expressions:
            expression = Expression.objects.create(
                lesson=lesson,
                kind=parsed_expr.kind,
                order=parsed_expr.order,
                name=parsed_expr.name,
                slug=slugify(parsed_expr.name),
                meaning=parsed_expr.meaning,
                ipa=parsed_expr.ipa,
                formality=parsed_expr.formality,
                synonyms=parsed_expr.synonyms,
                antonyms=parsed_expr.antonyms,
                collocations=parsed_expr.collocations,
                mistake_wrong=parsed_expr.mistake_wrong,
                mistake_right=parsed_expr.mistake_right,
                mistake_note=parsed_expr.mistake_note,
                five_word_meaning=parsed_expr.five_word_meaning,
                status=parsed_expr.status,
            )
            Example.objects.bulk_create([
                Example(
                    expression=expression,
                    label=parsed_example.label,
                    text=parsed_example.text,
                    order=order,
                )
                for order, parsed_example in enumerate(parsed_expr.examples, start=1)
            ])

        UpgradePair.objects.bulk_create([
            UpgradePair(
                lesson=lesson,
                order=order,
                original=parsed_upgrade.original,
                improved=parsed_upgrade.improved,
                reason=parsed_upgrade.reason,
            )
            for order, parsed_upgrade in enumerate(parsed.upgrades, start=1)
        ])

    def _validate(self, lessons: list[ParsedLesson]) -> None:
        for parsed in lessons:
            if not parsed.expressions:
                raise CommandError(f"Day {parsed.day_number}: no expressions parsed.")
            if not parsed.dialogue_topic:
                raise CommandError(f"Day {parsed.day_number}: missing dialogue topic.")
            for expr in parsed.expressions:
                if not expr.meaning:
                    raise CommandError(
                        f"Day {parsed.day_number}: '{expr.name}' has no meaning."
                    )

    @staticmethod
    def _tally(parsed: ParsedLesson, totals: dict) -> None:
        totals["lessons"] += 1
        totals["expressions"] += len(parsed.expressions)
        totals["examples"] += sum(len(e.examples) for e in parsed.expressions)
        totals["upgrades"] += len(parsed.upgrades)

    def _report(self, totals: dict, dry_run: bool) -> None:
        prefix = "[dry-run] Would import" if dry_run else "Imported"
        self.stdout.write(self.style.SUCCESS(
            f"{prefix}: {totals['lessons']} lessons, {totals['expressions']} expressions, "
            f"{totals['examples']} examples, {totals['upgrades']} upgrades."
        ))
