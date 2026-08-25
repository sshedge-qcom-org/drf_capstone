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


def _title_safe(text: str) -> str:
    """Collapse to a single line and neutralise quotes for an admonition title."""
    return " ".join(text.split()).replace('"', "'")


def _preserve_breaks(text: str) -> str:
    """Keep single line breaks (Markdown hard breaks) while allowing paragraphs."""
    return "\n".join((line + "  ") if line.strip() else "" for line in text.split("\n"))


def _badges(expr: ParsedExpression) -> str:
    """A row of pill badges (kind + status) shown under an expression heading."""
    pills = [
        f'<span class="fe-badge fe-badge--{expr.kind}">'
        f'{_TYPE_LABEL.get(expr.kind, expr.kind)}</span>'
    ]
    if expr.status:
        pills.append(
            f'<span class="fe-badge fe-badge--{expr.status}">'
            f'{expr.status.title()}</span>'
        )
    return '<span class="fe-badges">' + "".join(pills) + "</span>"


def _render_expression(expr: ParsedExpression) -> list[str]:
    out = [f"### {expr.order}. {expr.name}", "", _badges(expr), ""]
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
        # Fold the (single-sentence) mistake into the callout title so it stays
        # on one line instead of a title row + a body row.
        out += [f'!!! failure "Avoid: {_title_safe(expr.mistake_wrong)}"', ""]
    if expr.mistake_right:
        out.append('!!! success "Say instead"')
        out.append(_indent("\n".join(f"- {right}" for right in expr.mistake_right)))
        out.append("")
    if expr.mistake_note:
        out += ['!!! warning "Note"', _indent(expr.mistake_note), ""]

    if expr.examples:
        out += ["**Examples**", ""]
        for ex in expr.examples:
            out += [f'=== "{ex.label}"', f"    {ex.text}", ""]
    return out


def _cat_label(name: str) -> str:
    """Shorten a category header ("Meeting questions" → "Meeting") for a tab."""
    stripped = name.strip()
    low = stripped.lower()
    for suffix in (" questions", " question"):
        if low.endswith(suffix):
            return stripped[: -len(suffix)].strip()
    return stripped


def _parse_speaking_practice(text: str):
    """Split the free-text Speaking Practice into (intro, grouped prompts).

    Each prompt block ends in a ``Force …:`` line; the lines before it are the
    scenario, optionally preceded by a ``Label:`` line, optionally preceded by a
    category header (only on the first prompt of each category). Lenient by
    design so it survives the per-day format drift (labels/quotes present on
    some days, absent on others; ``Force these expressions:`` vs ``Force:``).
    """
    blocks: list[list[str]] = []
    current: list[str] = []
    for raw in text.split("\n"):
        line = raw.strip()
        if line:
            current.append(line)
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)

    intro: list[str] = []
    prompts = []  # (category, label, scenario, forced)
    category = None
    for block in blocks:
        force_idx = next(
            (i for i, ln in enumerate(block) if ln.lower().startswith("force")),
            None,
        )
        if force_idx is None:
            joined = " ".join(block)
            if joined.lower().startswith("instruction:"):
                joined = joined.split(":", 1)[1].strip()
            intro.append(joined)
            continue
        _, _, rest = block[force_idx].partition(":")
        forced = [item.strip() for item in rest.split(",") if item.strip()]
        head = block[:force_idx]
        scenario = head[-1].strip().strip("“”\"") if head else ""
        head = head[:-1]
        label = ""
        if head and head[-1].endswith(":"):
            label = head[-1][:-1].strip()
            head = head[:-1]
        if head:
            category = head[-1].strip()
        prompts.append((category, label, scenario, forced))

    groups = []  # (category, [(label, scenario, forced), …])
    for cat, label, scenario, forced in prompts:
        if not groups or groups[-1][0] != cat:
            groups.append((cat, []))
        groups[-1][1].append((label, scenario, forced))
    return intro, groups


def _render_prompt(label, scenario, forced, indent=""):
    out = []
    if label:
        out += [f"{indent}**{label}**", ""]
    if scenario:
        out += [f"{indent}> {scenario}", ""]
    if forced:
        chips = " · ".join(f"`{expr}`" for expr in forced)
        out += [f"{indent}:material-target: **Use:** {chips}", ""]
    return out


def _render_speaking_practice(text: str) -> list[str]:
    intro, groups = _parse_speaking_practice(text)
    if not groups:  # unrecognised shape — fall back to plain rendering
        return [_preserve_breaks(text), ""]

    out = []
    if intro:
        out.append('!!! quote "Practice out loud"')
        out += [f"    {line}" for line in intro]
        out.append("")

    use_tabs = sum(1 for cat, _ in groups if cat) > 1
    if use_tabs:
        for cat, items in groups:
            out += [f'=== "{_cat_label(cat) if cat else "Practice"}"', ""]
            for label, scenario, forced in items:
                out += _render_prompt(label, scenario, forced, indent="    ")
    else:
        for cat, items in groups:
            if cat:
                out += [f"**{_cat_label(cat)}**", ""]
            for label, scenario, forced in items:
                out += _render_prompt(label, scenario, forced)
    return out


def _pill(cls_suffix: str, label: str) -> str:
    """A badge pill safe to drop inside a Markdown table cell (inline HTML)."""
    return f'<span class="fe-badge fe-badge--{cls_suffix}">{label}</span>'


def _render_output_correction(text: str) -> list[str]:
    """Render the free-text Output Correction as a 'Your turn' callout.

    Task prompts ("Use X and Y …") and fill-in templates become bullets; short
    label lines ("Example prompts:") are emphasised; everything else stays as
    prose. The leading "no answers were provided" boilerplate (an authoring
    artifact referencing the MY_ANSWERS placeholder) is dropped.
    """
    raw_lines = text.split("\n")
    idx = 0
    while idx < len(raw_lines):
        stripped = raw_lines[idx].strip()
        if not stripped:
            idx += 1
            continue
        low = stripped.lower()
        if "my_answers" in low or ("provide" in low and (low[:4] == "no a"
                                   or "didn" in low)):
            idx += 1
            continue
        break
    raw_lines = raw_lines[idx:]

    body: list[str] = []
    prev = None  # "bullet" | "text" | None
    for raw in raw_lines:
        line = raw.strip()
        if not line:
            body.append("")
            prev = None
            continue
        if line.startswith(("Use ", "“", '"')):
            kind, rendered = "bullet", f"- {line}"
        elif line.endswith(":") and len(line) <= 30:
            kind, rendered = "text", f"**{line}**"
        else:
            kind, rendered = "text", line
        if prev is not None and prev != kind:
            body.append("")
        body.append(rendered)
        prev = kind

    while body and body[0] == "":
        body.pop(0)
    while body and body[-1] == "":
        body.pop()

    out = ['!!! example "Your turn"']
    out += [f"    {ln}" if ln else "" for ln in body]
    out.append("")
    return out


def render_lesson(lesson: ParsedLesson) -> str:
    """Render one lesson to a full Markdown page."""
    lines = [f"# Day {lesson.day_number} — {lesson.dialogue_topic}", ""]

    # The focus theme becomes a coloured subtitle right under the title (the one
    # line that actually says what the lesson is about).
    if lesson.focus_theme:
        lines += [f"*{lesson.focus_theme}*", ""]

    # Difficulty / mode / date carry little weight, so collapse them into one
    # small, muted meta line instead of three stacked rows.
    meta = [v for v in (lesson.difficulty, lesson.mode,
                        str(lesson.date) if lesson.date else "") if v]
    if meta:
        lines += [f'<p class="fe-meta">{" · ".join(meta)}</p>', ""]

    for kind, title, _ in _KIND_SECTIONS:
        exprs = [e for e in lesson.expressions if e.kind == kind]
        if not exprs:
            continue
        lines += [f"## {title} {{ .fe-sec--{kind} }}", ""]
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
        lines += ["## Speaking Practice", ""]
        lines += _render_speaking_practice(lesson.speaking_practice)
    if lesson.output_correction:
        lines += ["## Output Correction", ""]
        lines += _render_output_correction(lesson.output_correction)

    if lesson.tomorrow_preview:
        lines += ['!!! tip "Tomorrow\'s preview"', _indent(lesson.tomorrow_preview), ""]

    if lesson.expressions:
        lines += [
            "## Tracker", "",
            "| Expression | Type | 5-word meaning | Status |",
            "| --- | --- | --- | --- |",
        ]
        lines += [
            f"| {_cell(e.name)} | {_pill(e.kind, _TYPE_LABEL.get(e.kind, e.kind))} | "
            f"{_cell(e.five_word_meaning)} | "
            f"{_pill(e.status, e.status.title()) if e.status else ''} |"
            for e in lesson.expressions
        ]
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_index(lessons: list[ParsedLesson]) -> str:
    """Render the docs landing page: a short intro, a call-to-action, and a
    clean single-column table of every lesson (newest flagged "Latest")."""
    latest = lessons[-1] if lessons else None
    latest_day = latest.day_number if latest else None

    lines = [
        "---",
        "title: Business English for Senior Engineers",
        "---", "",
        "# Business English for Senior Engineers", "",
        "*Speak with clarity, precision, and confidence — a daily dose of "
        "professional idioms, phrasal verbs, and C1/C2 vocabulary for system "
        "design, code reviews, production issues, and sprint planning.*", "",
        "A fresh lesson lands every day. Each one is about a 10-minute read and "
        "the collection keeps growing — pick up where you left off below.", "",
    ]
    if latest:
        lines += [
            f"[:material-arrow-right-circle: Start today's lesson — Day "
            f"{latest.day_number}: {latest.dialogue_topic}]"
            f"(day-{latest.day_number}.md){{ .md-button .md-button--primary }}",
            "",
        ]

    lines += [
        "## Lessons", "",
        "| Day | Topic | Focus theme | Added |",
        "| --- | --- | --- | --- |",
    ]
    for lesson in lessons:
        day_cell = f"**[Day {lesson.day_number}](day-{lesson.day_number}.md)**"
        if lesson.day_number == latest_day:
            day_cell += ' <span class="fe-badge fe-badge--latest">Latest</span>'
        added = str(lesson.date) if lesson.date else "—"
        lines.append(
            f"| {day_cell} | {_cell(lesson.dialogue_topic)} | "
            f"{_cell(lesson.focus_theme)} | {added} |"
        )

    lines += [
        "",
        "## How to use", "",
        "Read each expression **aloud**, lean on the ✅ corrections over the ❌ "
        "mistakes, and reuse the labelled example sentences as your own "
        "templates. Try the Speaking Practice prompts without reading them.", "",
    ]
    return "\n".join(lines) + "\n"
