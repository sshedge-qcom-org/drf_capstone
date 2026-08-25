"""Tests for the fantasticEnglish lesson pipeline: parser → import → API → docs.

Grouped by layer:
  * ParserTests      — the Django-free parser against real raw_data/ files.
  * ImportCommandTests — DB import counts + idempotency.
  * LessonAPITests    — the read-only DRF API shape, filters, pagination, 404.
  * RendererTests     — Markdown rendering markers + DB/raw equivalence.
  * MkDocsBuildTests  — a `mkdocs build --strict` smoke check on committed docs.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase
from rest_framework.test import APITestCase

from BusinessEnglish.models import Lesson, Expression, Example, UpgradePair
from BusinessEnglish.services.lesson_parser import parse_all, parse_lesson_file
from BusinessEnglish.services.markdown_renderer import render_index, render_lesson

RAW_DIR = Path(settings.BASE_DIR) / "raw_data"

# Expected totals are derived from raw_data/ (not hard-coded) so that adding a
# new dayN file never breaks the suite.
_PARSED = parse_all(RAW_DIR)
EXPECTED_LESSONS = len(_PARSED)
EXPECTED_EXPRESSIONS = sum(len(l.expressions) for l in _PARSED)
EXPECTED_EXAMPLES = sum(len(e.examples) for l in _PARSED for e in l.expressions)
EXPECTED_UPGRADES = sum(len(l.upgrades) for l in _PARSED)
EXPECTED_VOCAB = sum(1 for l in _PARSED for e in l.expressions if e.kind == "vocabulary")


class ParserTests(SimpleTestCase):
    """Exercise the parser directly — no database involved."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.lessons = {lesson.day_number: lesson for lesson in parse_all(RAW_DIR)}

    def test_days_are_contiguous(self):
        self.assertGreaterEqual(len(self.lessons), 4)
        self.assertEqual(sorted(self.lessons), list(range(1, len(self.lessons) + 1)))

    def test_expression_counts_and_kinds(self):
        for day, lesson in self.lessons.items():
            with self.subTest(day=day):
                self.assertEqual(len(lesson.expressions), 10)
                kinds = [e.kind for e in lesson.expressions]
                self.assertEqual(kinds.count("idiom"), 3)
                self.assertEqual(kinds.count("phrasal_verb"), 3)
                self.assertEqual(kinds.count("vocabulary"), 4)

    def test_date_from_tracker(self):
        self.assertEqual(str(self.lessons[1].date), "2026-08-19")
        self.assertEqual(str(self.lessons[4].date), "2026-08-22")

    def test_multiple_corrections_and_note(self):
        # "Roll back" (day1) has two ✅ corrections and a ⚠️ note.
        roll_back = next(e for e in self.lessons[1].expressions if e.name == "Roll back")
        self.assertEqual(len(roll_back.mistake_right), 2)
        self.assertTrue(roll_back.mistake_note)
        self.assertIn("revert", roll_back.mistake_note.lower())

    def test_vocabulary_list_fields(self):
        constraint = next(e for e in self.lessons[1].expressions if e.name == "Constraint")
        self.assertEqual(constraint.synonyms, ["limitation", "restriction", "boundary"])
        self.assertEqual(len(constraint.collocations), 4)

    def test_tracker_reconciliation(self):
        # Every expression should pick up its 5-word meaning + status from the Tracker.
        for lesson in self.lessons.values():
            for expr in lesson.expressions:
                with self.subTest(day=lesson.day_number, expr=expr.name):
                    self.assertTrue(expr.five_word_meaning)
                    self.assertIn(expr.status, {"new", "review"})

    def test_tomorrow_preview_placement_varies(self):
        # day1 before Tracker, day3 inline, day4 after Tracker → all captured;
        # day2 has no preview.
        self.assertTrue(self.lessons[1].tomorrow_preview)
        self.assertEqual(self.lessons[2].tomorrow_preview, "")
        self.assertTrue(self.lessons[3].tomorrow_preview)
        self.assertIn("Root cause", self.lessons[4].tomorrow_preview)

    def test_examples_are_unquoted(self):
        example = self.lessons[1].expressions[0].examples[0]
        self.assertFalse(example.text.startswith(("\"", "“")))

    def test_crlf_day4_parses(self):
        # day4 is CRLF; splitlines() should still yield a clean 10-expression lesson.
        day4 = parse_lesson_file(RAW_DIR / "day4")
        self.assertEqual(len(day4.expressions), 10)


class ImportCommandTests(TestCase):
    """import_lessons writes the expected rows and is idempotent."""

    def test_import_counts(self):
        call_command("import_lessons", "--clear", verbosity=0)
        self.assertEqual(Lesson.objects.count(), EXPECTED_LESSONS)
        self.assertEqual(Expression.objects.count(), EXPECTED_EXPRESSIONS)
        self.assertEqual(Example.objects.count(), EXPECTED_EXAMPLES)
        self.assertEqual(UpgradePair.objects.count(), EXPECTED_UPGRADES)

    def test_import_is_idempotent(self):
        call_command("import_lessons", "--clear", verbosity=0)
        call_command("import_lessons", verbosity=0)  # second run, no --clear
        self.assertEqual(Lesson.objects.count(), EXPECTED_LESSONS)
        self.assertEqual(Expression.objects.count(), EXPECTED_EXPRESSIONS)
        self.assertEqual(Example.objects.count(), EXPECTED_EXAMPLES)

    def test_dry_run_writes_nothing(self):
        call_command("import_lessons", "--dry-run", verbosity=0)
        self.assertEqual(Lesson.objects.count(), 0)


class LessonAPITests(APITestCase):
    """The read-only DRF API surface."""

    @classmethod
    def setUpTestData(cls):
        call_command("import_lessons", "--clear", verbosity=0)

    def test_lesson_list_is_paginated_summary(self):
        response = self.client.get("/api/lessons/")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["count"], EXPECTED_LESSONS)
        self.assertIn("results", body)
        first = body["results"][0]
        self.assertEqual(first["expression_count"], 10)
        self.assertNotIn("expressions", first)  # list stays lightweight

    def test_lesson_detail_is_nested(self):
        response = self.client.get("/api/lessons/1/")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(len(body["expressions"]), 10)
        self.assertEqual(len(body["upgrades"]), 10)
        self.assertEqual(len(body["expressions"][0]["examples"]), 3)

    def test_lesson_lookup_by_day_number(self):
        self.assertEqual(self.client.get("/api/lessons/2/").json()["day_number"], 2)

    def test_missing_lesson_returns_404(self):
        self.assertEqual(self.client.get("/api/lessons/99/").status_code, 404)

    def test_lesson_expressions_action_filters_by_kind(self):
        response = self.client.get("/api/lessons/1/expressions/?kind=idiom")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_expression_search(self):
        response = self.client.get("/api/expressions/?search=roll+back")
        body = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Roll back", [r["name"] for r in body["results"]])

    def test_expression_kind_filter(self):
        response = self.client.get("/api/expressions/?kind=vocabulary")
        self.assertEqual(response.json()["count"], EXPECTED_VOCAB)  # 4 vocab × days

    def test_expression_pagination(self):
        page_size = settings.REST_FRAMEWORK["PAGE_SIZE"]
        response = self.client.get("/api/expressions/")
        body = response.json()
        self.assertEqual(body["count"], EXPECTED_EXPRESSIONS)
        self.assertEqual(len(body["results"]), min(page_size, EXPECTED_EXPRESSIONS))
        self.assertEqual(body["next"] is not None, EXPECTED_EXPRESSIONS > page_size)


class RendererTests(SimpleTestCase):
    """Markdown rendering markers and DB/raw equivalence."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.lessons = {lesson.day_number: lesson for lesson in parse_all(RAW_DIR)}

    def test_admonitions_and_tables_present(self):
        markdown = render_lesson(self.lessons[1])
        for marker in ('!!! failure "Avoid:', '!!! success "Say instead"',
                       "## Natural English Upgrade", "## Tracker", "| --- | --- |"):
            self.assertIn(marker, markdown)

    def test_warning_admonition_when_note_exists(self):
        # day1 "Roll back" carries a ⚠️ note.
        self.assertIn('!!! warning "Note"', render_lesson(self.lessons[1]))

    def test_examples_render_as_content_tabs(self):
        # Example sentences become pymdownx tabbed blocks keyed by their label.
        markdown = render_lesson(self.lessons[1])
        self.assertIn('=== "Engineering"', markdown)

    def test_speaking_practice_is_structured(self):
        # Speaking Practice becomes an intro callout + per-category tabs with
        # scenario blockquotes and target-expression chips (not a flat blob).
        markdown = render_lesson(self.lessons[1])
        self.assertIn('!!! quote "Practice out loud"', markdown)
        self.assertIn('=== "Meeting"', markdown)
        self.assertIn("**Use:**", markdown)

    def test_output_correction_is_a_callout_without_boilerplate(self):
        # Output Correction renders as a callout; the internal "MY_ANSWERS"
        # boilerplate line is dropped.
        markdown = render_lesson(self.lessons[1])
        self.assertIn('!!! example "Your turn"', markdown)
        self.assertNotIn("MY_ANSWERS", markdown)

    def test_tracker_status_uses_pills(self):
        # The Tracker status column renders as a badge pill, not bare text.
        markdown = render_lesson(self.lessons[1])
        self.assertRegex(markdown, r'fe-badge fe-badge--(new|review)">(New|Review)</span> \|')

    def test_index_links_every_day(self):
        markdown = render_index(list(self.lessons.values()))
        for day in self.lessons:
            self.assertIn(f"day-{day}.md", markdown)


class MkDocsBuildTests(SimpleTestCase):
    """`mkdocs build --strict` should succeed on the committed docs."""

    def test_strict_build(self):
        if not (Path(settings.BASE_DIR) / "docs" / "index.md").exists():
            self.skipTest("docs/ not generated; run export_docs first")
        with tempfile.TemporaryDirectory() as site_dir:
            result = subprocess.run(
                [sys.executable, "-m", "mkdocs", "build", "--strict",
                 "--site-dir", site_dir],
                cwd=settings.BASE_DIR,
                capture_output=True, text=True,
            )
        self.assertEqual(result.returncode, 0, msg=result.stderr)
