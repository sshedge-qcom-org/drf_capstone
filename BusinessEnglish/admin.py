"""Admin registration for the lesson corpus.

Inlines let you see a Lesson's expressions and upgrade pairs on one page, and an
Expression's examples on its own page — handy for spot-checking an import.
"""

from django.contrib import admin

from .models import Lesson, Expression, Example, UpgradePair


class ExpressionInline(admin.TabularInline):
    model = Expression
    extra = 0
    fields = ("kind", "order", "name", "status")
    ordering = ("kind", "order")
    show_change_link = True


class UpgradePairInline(admin.TabularInline):
    model = UpgradePair
    extra = 0
    fields = ("order", "original", "improved")
    ordering = ("order",)


class ExampleInline(admin.TabularInline):
    model = Example
    extra = 0
    fields = ("order", "label", "text")
    ordering = ("order",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("day_number", "dialogue_topic", "date", "mode")
    list_filter = ("mode", "difficulty")
    search_fields = ("dialogue_topic", "focus_theme", "title")
    ordering = ("day_number",)
    inlines = [ExpressionInline, UpgradePairInline]


@admin.register(Expression)
class ExpressionAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "lesson", "status")
    list_filter = ("kind", "status", "lesson")
    search_fields = ("name", "meaning")
    ordering = ("lesson", "kind", "order")
    inlines = [ExampleInline]


@admin.register(UpgradePair)
class UpgradePairAdmin(admin.ModelAdmin):
    list_display = ("lesson", "order", "original", "improved")
    list_filter = ("lesson",)
    ordering = ("lesson", "order")


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ("expression", "label", "order")
    list_filter = ("label",)
    search_fields = ("text",)
