"""Render :class:`ParsedLesson` dataclasses to MkDocs (Material) Markdown.

Django-free by design: it consumes the same dataclasses the parser produces, so
``export_docs`` can feed it either from the DB (via an ORM→dataclass adapter) or
straight from ``raw_data`` (``--from-raw``). The ❌/✅/⚠️ mistake blocks become
Material admonitions (``!!! failure`` / ``!!! success`` / ``!!! warning``).
"""

from __future__ import annotations

from .lesson_parser import ParsedExpression, ParsedLesson


_KIND_SECTIONS = [
    ("idiom", "Professional Idioms", "Idiom"),
    ("phrasal_verb", "Phrasal Verbs", "Phrasal verb"),
    ("vocabulary", "C1/C2 Vocabulary", "Vocabulary"),
]
_TYPE_LABEL = {kind: label for kind, _, label in _KIND_SECTIONS}


def _cell(text: str) -> str:
    """Make a value safe for a single Markdown table cell."""
    return text.replace("\n", " ").replace("|", "\\|").strip()


def _indent(text: str) -> str:
    """Indent every line by 4 spaces for admonition bodies (blanks stay blank)."""
    return "\n".join(("    " + line) if line.strip() else "" for line in text.split("\n"))


def _preserve_breaks(text: str) -> str:
    """Keep single line breaks (Markdown hard breaks) while allowing paragraphs."""
    return "\n".join((line + "  ") if line.strip() else "" for line in text.split("\n"))


def _render_expression(expr: ParsedExpression) -> list[str]:
    out = [f"### {expr.order}. {expr.name}", ""]
    out.append(f"- **Meaning:** {expr.meaning}")
    if expr.ipa:
        out.append(f"- **IPA:** `{expr.ipa}`")
    if expr.formality:
        out.append(f"- **Formality:** {expr.formality}")
    if expr.synonyms:
        out.append(f"- **Synonyms:** {', '.join(expr.synonyms)}")
    if expr.antonyms:
        out.append(f"- **Antonyms:** {', '.join(expr.antonyms)}")
    if expr.collocations:
        out.append(f"- **Collocations:** {', '.join(expr.collocations)}")
    out.append("")

    if expr.mistake_wrong:
        out += ['!!! failure "Avoid"', _indent(expr.mistake_wrong), ""]
    if expr.mistake_right:
        out.append('!!! success "Say instead"')
        out.append(_indent("\n".join(f"- {right}" for right in expr.mistake_right)))
        out.append("")
    if expr.mistake_note:
        out += ['!!! warning "Note"', _indent(expr.mistake_note), ""]

    if expr.examples:
        out += ["**Examples**", ""]
        out += [f"- *{ex.label}:* {ex.text}" for ex in expr.examples]
        out.append("")
    return out


def render_lesson(lesson: ParsedLesson) -> str:
    """Render one lesson to a full Markdown page."""
    lines = [f"# Day {lesson.day_number} — {lesson.dialogue_topic}", ""]

    meta = []
    if lesson.focus_theme:
        meta.append(f"**Focus theme:** {lesson.focus_theme}")
    if lesson.difficulty:
        meta.append(f"**Difficulty:** {lesson.difficulty}")
    if lesson.mode:
        meta.append(f"**Mode:** {lesson.mode}")
    if lesson.date:
        meta.append(f"**Date:** {lesson.date}")
    if meta:
        lines += ["  \n".join(meta), ""]
    if lesson.lesson_focus:
        lines += [f"*{lesson.lesson_focus}*", ""]

    for kind, title, _ in _KIND_SECTIONS:
        exprs = [e for e in lesson.expressions if e.kind == kind]
        if not exprs:
            continue
        lines += [f"## {title}", ""]
        for expr in exprs:
            lines += _render_expression(expr)

    if lesson.upgrades:
        lines += [
            "## Natural English Upgrade", "",
            "| Common Indian corporate English | Natural international English | Why it's better |",
            "| --- | --- | --- |",
        ]
        lines += [
            f"| {_cell(u.original)} | {_cell(u.improved)} | {_cell(u.reason)} |"
            for u in lesson.upgrades
        ]
        lines.append("")

    if lesson.speaking_practice:
        lines += ["## Speaking Practice", "", _preserve_breaks(lesson.speaking_practice), ""]
    if lesson.output_correction:
        lines += ["## Output Correction", "", _preserve_breaks(lesson.output_correction), ""]

    if lesson.tomorrow_preview:
        lines += ['!!! tip "Tomorrow\'s preview"', _indent(lesson.tomorrow_preview), ""]

    if lesson.expressions:
        lines += [
            "## Tracker", "",
            "| Expression | Type | 5-word meaning | Status |",
            "| --- | --- | --- | --- |",
        ]
        lines += [
            f"| {_cell(e.name)} | {_TYPE_LABEL.get(e.kind, e.kind)} | "
            f"{_cell(e.five_word_meaning)} | {e.status} |"
            for e in lesson.expressions
        ]
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_index(lessons: list[ParsedLesson]) -> str:
    """Render the docs landing page with a table linking to each day."""
    lines = [
        "# Business English for Senior Engineers", "",
        "A daily Business-English lesson corpus — professional idioms, phrasal "
        "verbs, and C1/C2 vocabulary for system design, code reviews, production "
        "issues, and sprint planning. Rendered from `raw_data/` via the shared "
        "parser, the same source that powers the REST API.", "",
        "| Day | Topic | Focus theme | Date |",
        "| --- | --- | --- | --- |",
    ]
    for lesson in lessons:
        lines.append(
            f"| [Day {lesson.day_number}](day-{lesson.day_number}.md) "
            f"| {_cell(lesson.dialogue_topic)} | {_cell(lesson.focus_theme)} "
            f"| {lesson.date or ''} |"
        )
    lines.append("")
    return "\n".join(lines) + "\n"
