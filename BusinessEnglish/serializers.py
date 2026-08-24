"""DRF serializers for the read-only lesson API.

Two Lesson serializers keep list responses cheap and detail responses rich:
a lightweight :class:`LessonListSerializer` (summary + expression count) and a
:class:`LessonDetailSerializer` that nests the full expressions and upgrades.
"""

from rest_framework import serializers

from .models import Lesson, Expression, Example, UpgradePair


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ("label", "text", "order")


class ExpressionSerializer(serializers.ModelSerializer):
    kind_display = serializers.CharField(source="get_kind_display", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    lesson_day = serializers.IntegerField(source="lesson.day_number", read_only=True)
    examples = ExampleSerializer(many=True, read_only=True)

    class Meta:
        model = Expression
        fields = (
            "id", "lesson_day", "kind", "kind_display", "order", "name", "slug",
            "meaning", "ipa", "formality",
            "synonyms", "antonyms", "collocations",
            "mistake_wrong", "mistake_right", "mistake_note",
            "five_word_meaning", "status", "status_display",
            "examples",
        )


class UpgradePairSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpgradePair
        fields = ("order", "original", "improved", "reason")


class LessonListSerializer(serializers.ModelSerializer):
    """Summary shape for the list endpoint (no nested children)."""

    expression_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "day_number", "date", "title", "mode",
            "dialogue_topic", "focus_theme", "difficulty", "expression_count",
        )


class LessonDetailSerializer(serializers.ModelSerializer):
    """Full lesson with nested expressions and the upgrade table."""

    expressions = ExpressionSerializer(many=True, read_only=True)
    upgrades = UpgradePairSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "day_number", "date", "title", "mode",
            "focus_theme", "dialogue_topic", "difficulty", "lesson_focus",
            "review_items", "avoiding_repeats",
            "speaking_practice", "output_correction", "tomorrow_preview",
            "source_filename",
            "expressions", "upgrades",
        )
