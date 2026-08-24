"""``manage.py export_docs`` — render lessons to ``docs/*.md`` for MkDocs.

Default source is the **database** (single source of truth at serving time);
``--from-raw`` renders straight from ``raw_data/`` without touching the DB,
which is handy for CI or a DB-less docs build.

    manage.py export_docs               # from the DB
    manage.py export_docs --from-raw    # bypass the DB, parse raw_data/
    manage.py export_docs --clear       # remove generated docs first
"""

from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from BusinessEnglish.models import Lesson
from BusinessEnglish.services.lesson_parser import (
    ParsedExample, ParsedExpression, ParsedLesson, ParsedUpgrade, parse_all,
)
from BusinessEnglish.services.markdown_renderer import render_index, render_lesson


class Command(BaseCommand):
    help = "Render lessons to docs/*.md for the MkDocs site."

    def add_arguments(self, parser):
        parser.add_argument(
            "--from-raw", action="store_true",
            help="Render from raw_data/ instead of the database.",
        )
        parser.add_argument(
            "--clear", action="store_true",
            help="Delete generated index.md/day-*.md before writing.",
        )

    def handle(self, *args, **options):
        base_dir = Path(settings.BASE_DIR)
        docs_dir = base_dir / "docs"

        if options["from_raw"]:
            lessons = parse_all(base_dir / "raw_data")
        else:
            lessons = [self._to_parsed(obj) for obj in (
                Lesson.objects
                .prefetch_related("expressions__examples", "upgrades")
                .order_by("day_number")
            )]

        if not lessons:
            raise CommandError(
                "No lessons to export. Run import_lessons first, or pass --from-raw."
            )

        docs_dir.mkdir(parents=True, exist_ok=True)
        if options["clear"]:
            for stale in [docs_dir / "index.md", *docs_dir.glob("day-*.md")]:
                stale.unlink(missing_ok=True)

        (docs_dir / "index.md").write_text(render_index(lessons), encoding="utf-8")
        for lesson in lessons:
            (docs_dir / f"day-{lesson.day_number}.md").write_text(
                render_lesson(lesson), encoding="utf-8"
            )

        self.stdout.write(self.style.SUCCESS(
            f"Exported {len(lessons)} lesson pages + index to {docs_dir}"
            f" ({'raw_data' if options['from_raw'] else 'database'})."
        ))

    @staticmethod
    def _to_parsed(lesson: Lesson) -> ParsedLesson:
        """Adapt an ORM Lesson (with children) to the renderer's dataclasses."""
        expressions = [
            ParsedExpression(
                kind=expr.kind, order=expr.order, name=expr.name,
                meaning=expr.meaning, ipa=expr.ipa, formality=expr.formality,
                synonyms=expr.synonyms, antonyms=expr.antonyms,
                collocations=expr.collocations,
                mistake_wrong=expr.mistake_wrong, mistake_right=expr.mistake_right,
                mistake_note=expr.mistake_note,
                examples=[ParsedExample(ex.label, ex.text) for ex in expr.examples.all()],
                five_word_meaning=expr.five_word_meaning, status=expr.status,
            )
            for expr in lesson.expressions.all()
        ]
        upgrades = [
            ParsedUpgrade(u.original, u.improved, u.reason)
            for u in lesson.upgrades.all()
        ]
        return ParsedLesson(
            day_number=lesson.day_number, title=lesson.title, mode=lesson.mode,
            focus_theme=lesson.focus_theme, dialogue_topic=lesson.dialogue_topic,
            difficulty=lesson.difficulty, lesson_focus=lesson.lesson_focus,
            review_items=lesson.review_items, avoiding_repeats=lesson.avoiding_repeats,
            speaking_practice=lesson.speaking_practice,
            output_correction=lesson.output_correction,
            tomorrow_preview=lesson.tomorrow_preview, date=lesson.date,
            source_filename=lesson.source_filename,
            expressions=expressions, upgrades=upgrades,
        )
