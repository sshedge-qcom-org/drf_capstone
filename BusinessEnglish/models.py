"""Normalized data model for the Business-English lesson corpus.

A lesson (``raw_data/dayN``) fans out into three child tables:

    Lesson ─┬─ Expression ── Example      (the taught idioms / phrasal verbs / vocab)
            └─ UpgradePair                (the "Natural English Upgrade" table)

The parser (``services/lesson_parser.py``) is the single structural authority;
``import_lessons`` maps its dataclasses onto these models, and both the DRF API
and the MkDocs export read from here.
"""

from django.db import models


class Lesson(models.Model):
    """One daily Business-English lesson (maps to a ``raw_data/dayN`` file)."""

    # Real-world identifier (Day 1, 2, 3...). `unique` stops two rows sharing a
    # day; the API points its lookup here so URLs read /api/lessons/1/.
    day_number = models.PositiveIntegerField(unique=True)

    # From the trailing Tracker table's first row (all rows share the date).
    date = models.DateField(null=True, blank=True)

    # Header + intro fields.
    title = models.CharField(max_length=200)            # "Day 1 — Lite Lesson"
    mode = models.CharField(max_length=50, default="Lite")
    focus_theme = models.TextField()                    # header "Focus theme:"
    dialogue_topic = models.CharField(max_length=200)   # header "Dialogue topic:"
    difficulty = models.CharField(max_length=100, blank=True)
    lesson_focus = models.TextField(blank=True)         # intro "Focus:" line

    # Header notes that vary in label/presence across days.
    review_items = models.TextField(blank=True)         # "Review items[ reused]:"
    avoiding_repeats = models.TextField(blank=True)     # "Avoiding recent repeats...:"

    # Free-form trailing sections.
    speaking_practice = models.TextField(blank=True)    # section 6
    output_correction = models.TextField(blank=True)    # section 9
    tomorrow_preview = models.TextField(blank=True)     # placement varies by day

    # Provenance: which raw_data file produced this row.
    source_filename = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["day_number"]

    def __str__(self):
        return f"Day {self.day_number}: {self.dialogue_topic}"


class Expression(models.Model):
    """A single taught expression — an idiom, phrasal verb, or vocabulary word."""

    class Kind(models.TextChoices):
        IDIOM = "idiom", "Idiom"
        PHRASAL_VERB = "phrasal_verb", "Phrasal verb"
        VOCABULARY = "vocabulary", "Vocabulary"

    class Status(models.TextChoices):
        NEW = "new", "New"
        REVIEW = "review", "Review"

    lesson = models.ForeignKey(
        Lesson, related_name="expressions", on_delete=models.CASCADE
    )
    kind = models.CharField(max_length=20, choices=Kind.choices)
    order = models.PositiveIntegerField()               # 1-based within its kind

    name = models.CharField(max_length=200)             # "Paint ourselves into a corner"
    slug = models.SlugField(max_length=220, blank=True)
    meaning = models.TextField()
    ipa = models.CharField(max_length=200, blank=True)
    formality = models.CharField(max_length=200, blank=True)  # idioms only

    # Vocabulary-only list fields (empty list for idioms/phrasal verbs).
    synonyms = models.JSONField(default=list, blank=True)
    antonyms = models.JSONField(default=list, blank=True)
    collocations = models.JSONField(default=list, blank=True)

    # The ❌ / ✅ / ⚠️ "common mistake" block. `mistake_right` is a list because
    # some expressions carry more than one ✅ correction (e.g. "roll back").
    mistake_wrong = models.TextField(blank=True)        # ❌
    mistake_right = models.JSONField(default=list, blank=True)  # ✅ (>=1)
    mistake_note = models.TextField(blank=True)         # ⚠️

    # Reconciled from the Tracker table (matched by lowercased name).
    five_word_meaning = models.CharField(max_length=200, blank=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.NEW
    )

    class Meta:
        ordering = ["lesson", "kind", "order"]
        unique_together = ("lesson", "kind", "order")

    def __str__(self):
        return f"{self.name} ({self.get_kind_display()})"


class Example(models.Model):
    """A labelled example sentence attached to an Expression.

    ``label`` is the context tag stripped of the trailing " example" — e.g.
    "Engineering", "Meeting", "Code-review", "Stakeholder".
    """

    expression = models.ForeignKey(
        Expression, related_name="examples", on_delete=models.CASCADE
    )
    label = models.CharField(max_length=100)
    text = models.TextField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["expression", "order"]

    def __str__(self):
        return f"{self.label}: {self.text[:40]}"


class UpgradePair(models.Model):
    """One row of the "Natural English Upgrade" table (section 4)."""

    lesson = models.ForeignKey(
        Lesson, related_name="upgrades", on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField()
    original = models.TextField()   # "Common Indian corporate English"
    improved = models.TextField()   # "Natural international English"
    reason = models.TextField()     # "Why it's better"

    class Meta:
        ordering = ["lesson", "order"]

    def __str__(self):
        return f"{self.original[:30]} → {self.improved[:30]}"
