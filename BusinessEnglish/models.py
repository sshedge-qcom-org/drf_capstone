from django.db import models

class Lesson(models.Model):
    """One daily Business-English lesson (maps to a raw_data/dayN file).

    Phase 1 keeps this intentionally minimal — just enough fields to get a
    real API endpoint working. We flesh it out (idioms, vocab, tracker, ...)
    in Phase 2.
    """

    # The real-world identifier of a lesson (Day 1, 2, 3...). `unique` stops
    # two rows sharing a day, and later we point the API's lookup at this so
    # URLs read /api/lessons/1/ instead of exposing the auto-generated `id`.
    day_number = models.PositiveIntegerField(unique=True)

    # CharField = short, *bounded* text -> it REQUIRES max_length.
    title = models.CharField(max_length=200)           # e.g. "Day 1 — Lite Lesson"
    dialogue_topic = models.CharField(max_length=200)  # e.g. "System design"

    # TextField = *unbounded* free-form text; right for a whole sentence.
    focus_theme = models.TextField()

    # Optional for now. null -> the DB column may be empty;
    # blank -> forms/validation may leave it empty. A date needs both.
    date = models.DateField(null=True, blank=True)

    class Meta:
        # Always return lessons in day order (API lists, admin, shell).
        ordering = ["day_number"]

    def __str__(self):
        # Readable label in the admin & `manage.py shell`
        # (without this Django just shows "Lesson object (1)
        return f"Day {self.day_number}: {self.dialogue_topic}"