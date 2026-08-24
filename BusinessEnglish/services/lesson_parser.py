"""Parse ``raw_data/dayN`` lesson files into plain dataclasses.

This module is the **single structural authority** for the lesson format and is
deliberately **free of Django imports** so it stays unit-testable without the
ORM. ``import_lessons`` maps these dataclasses onto the DB; ``export_docs
--from-raw`` can render straight from them without a database.

The format (see CLAUDE.md for the full spec) is a ``key: value`` header, an
intro line pair, numbered sections (1 idioms / 2 phrasal verbs / 3 vocabulary /
4 upgrade table / 6 speaking / 9 output correction — 5/7/8 are intentionally
skipped in the "Lite" variant), and a trailing tab-separated Tracker table.
Parsing is pattern-driven, never line-number-driven, and tolerant of the
day-to-day variance (LF vs CRLF, label wording, "Tomorrow's preview" placement).
"""

from __future__ import annotations

import datetime
import re
from dataclasses import dataclass, field
from pathlib import Path


# ── Dataclasses ────────────────────────────────────────────────────────────

@dataclass
class ParsedExample:
    label: str
    text: str


@dataclass
class ParsedExpression:
    kind: str                       # "idiom" | "phrasal_verb" | "vocabulary"
    order: int
    name: str
    meaning: str = ""
    ipa: str = ""
    formality: str = ""
    synonyms: list[str] = field(default_factory=list)
    antonyms: list[str] = field(default_factory=list)
    collocations: list[str] = field(default_factory=list)
    mistake_wrong: str = ""
    mistake_right: list[str] = field(default_factory=list)
    mistake_note: str = ""
    examples: list[ParsedExample] = field(default_factory=list)
    # Reconciled from the Tracker table.
    five_word_meaning: str = ""
    status: str = "new"


@dataclass
class ParsedUpgrade:
    original: str
    improved: str
    reason: str


@dataclass
class ParsedLesson:
    day_number: int
    title: str
    mode: str
    focus_theme: str
    dialogue_topic: str
    difficulty: str
    lesson_focus: str
    review_items: str
    avoiding_repeats: str
    speaking_practice: str
    output_correction: str
    tomorrow_preview: str
    date: datetime.date | None
    source_filename: str
    expressions: list[ParsedExpression] = field(default_factory=list)
    upgrades: list[ParsedUpgrade] = field(default_factory=list)


# ── Patterns & helpers ───────────────────────────────────────────────────────

_SECTION_RE = re.compile(r"^(\d+)\s+—\s+(.+)$")     # "1 — Professional Idioms"
_EXPR_RE = re.compile(r"^(\d+)\.\s+(.+)$")           # "1. Paint ourselves ..."
_EXAMPLE_RE = re.compile(r"^(.+?) example:$", re.IGNORECASE)
_TITLE_RE = re.compile(r"^Day\s+\d+\s+—")            # "Day 1 — Lite Lesson"

# section number → expression kind
_KIND_BY_SECTION = {1: "idiom", 2: "phrasal_verb", 3: "vocabulary"}

# leading glyphs (incl. the U+FE0F variation selector on ⚠️) + whitespace
_GLYPH_STRIP = "❌✅⚠️️ \t"
_QUOTES_OPEN = "\"“‘"
_QUOTES_CLOSE = "\"”’"


def _value(line: str) -> str:
    """Return everything after the first ``:`` on a ``key: value`` line."""
    return line.partition(":")[2].strip()


def _split_list(value: str) -> list[str]:
    """Split a comma-separated field ("a, b, c") into a clean list."""
    return [part.strip() for part in value.split(",") if part.strip()]


def _unquote(text: str) -> str:
    """Strip a single pair of matching outer quotes (straight or curly)."""
    text = text.strip()
    if len(text) >= 2 and text[0] in _QUOTES_OPEN and text[-1] in _QUOTES_CLOSE:
        text = text[1:-1].strip()
    return text


def _after_glyph(line: str) -> str:
    """Drop a leading ❌/✅/⚠️ glyph and unquote the remaining sentence."""
    return _unquote(line.lstrip(_GLYPH_STRIP))


def _is_preview(stripped: str) -> bool:
    low = stripped.lower()
    return low.startswith("tomorrow") and "preview" in low


# ── Parser ───────────────────────────────────────────────────────────────────

def parse_lesson_text(text: str, source_filename: str = "") -> ParsedLesson:
    """Parse the full text of one lesson file into a :class:`ParsedLesson`."""
    # splitlines() handles LF (day1-3) and CRLF (day4) transparently.
    lines = text.splitlines()

    # 1) Header: `key: value` lines up to the first blank line.
    header: dict[str, str] = {}
    i = 0
    while i < len(lines) and lines[i].strip():
        if ":" in lines[i]:
            key, _, val = lines[i].partition(":")
            header[key.strip().lower()] = val.strip()
        i += 1

    # 2) Body state machine over the remaining lines.
    current: str | None = None          # active section kind
    cur_expr: ParsedExpression | None = None
    pending_example_label: str | None = None
    upgrade_header_seen = False
    tracker_header_seen = False
    grab_preview_next = False

    lesson_title = ""
    lesson_focus = ""
    tomorrow_preview = ""
    speaking_lines: list[str] = []
    output_lines: list[str] = []
    expressions: list[ParsedExpression] = []
    upgrades: list[ParsedUpgrade] = []
    tracker_rows: list[dict[str, str]] = []

    def flush_expr() -> None:
        nonlocal cur_expr
        if cur_expr is not None:
            expressions.append(cur_expr)
            cur_expr = None

    for raw in lines[i:]:
        stripped = raw.strip()

        # -- global interceptors (fire regardless of the current section) --
        if grab_preview_next:
            if stripped:
                tomorrow_preview = stripped
                grab_preview_next = False
            continue

        if _is_preview(stripped):
            idx = stripped.lower().find("preview") + len("preview")
            rest = stripped[idx:].lstrip(":").strip()
            if rest:
                tomorrow_preview = rest
            else:
                grab_preview_next = True
            continue

        if stripped == "Tracker":
            flush_expr()
            current = "tracker"
            tracker_header_seen = False
            continue

        section = _SECTION_RE.match(stripped)
        if section:
            flush_expr()
            num = int(section.group(1))
            current = _KIND_BY_SECTION.get(num)
            if current is None:
                title = section.group(2).lower()
                if "upgrade" in title:
                    current = "upgrade"
                elif "speaking" in title:
                    current = "speaking"
                elif "output" in title:
                    current = "output"
                else:
                    current = "other"
            pending_example_label = None
            upgrade_header_seen = False
            continue

        # -- intro line pair (before the first section) --
        if current is None:
            if _TITLE_RE.match(stripped):
                lesson_title = stripped
            elif stripped.startswith("Focus:"):
                lesson_focus = _value(stripped)
            continue

        # -- expression sections (idioms / phrasal verbs / vocabulary) --
        if current in _KIND_BY_SECTION.values():
            expr_match = _EXPR_RE.match(stripped)
            if expr_match:
                flush_expr()
                cur_expr = ParsedExpression(
                    kind=current,
                    order=int(expr_match.group(1)),
                    name=expr_match.group(2).strip(),
                )
                pending_example_label = None
                continue
            if cur_expr is None:
                continue

            example_match = _EXAMPLE_RE.match(stripped)
            if example_match:
                pending_example_label = example_match.group(1).strip()
                continue
            if pending_example_label is not None and stripped:
                cur_expr.examples.append(
                    ParsedExample(label=pending_example_label, text=_unquote(stripped))
                )
                pending_example_label = None
                continue

            if stripped.startswith("Meaning:"):
                cur_expr.meaning = _value(stripped)
            elif stripped.startswith("IPA:"):
                cur_expr.ipa = _value(stripped)
            elif stripped.startswith("Formality:"):
                cur_expr.formality = _value(stripped)
            elif stripped.startswith("Synonyms:"):
                cur_expr.synonyms = _split_list(_value(stripped))
            elif stripped.startswith("Antonyms:"):
                cur_expr.antonyms = _split_list(_value(stripped))
            elif stripped.lower().startswith(("common collocations:", "collocations:")):
                cur_expr.collocations = _split_list(_value(stripped))
            elif stripped.startswith("❌"):
                cur_expr.mistake_wrong = _after_glyph(stripped)
            elif stripped.startswith("✅"):
                cur_expr.mistake_right.append(_after_glyph(stripped))
            elif stripped.startswith("⚠"):
                cur_expr.mistake_note = stripped.lstrip(_GLYPH_STRIP)
            # anything else (the "Common ... mistake:" label, blanks) is ignored
            continue

        # -- Natural English Upgrade table (3 tab-separated columns) --
        if current == "upgrade":
            if "\t" in raw:
                if not upgrade_header_seen:
                    upgrade_header_seen = True  # skip the column header row
                    continue
                parts = raw.split("\t")
                if len(parts) >= 3:
                    upgrades.append(ParsedUpgrade(
                        original=parts[0].strip(),
                        improved=parts[1].strip(),
                        reason=parts[2].strip(),
                    ))
            continue

        # -- free-form sections --
        if current == "speaking":
            speaking_lines.append(stripped)
            continue
        if current == "output":
            output_lines.append(stripped)
            continue

        # -- Tracker table (6 tab-separated columns) --
        if current == "tracker":
            if "\t" in raw:
                if not tracker_header_seen:
                    tracker_header_seen = True  # skip the column header row
                    continue
                parts = raw.split("\t")
                if len(parts) >= 6:
                    tracker_rows.append({
                        "date": parts[0].strip(),
                        "expression": parts[2].strip(),
                        "five": parts[4].strip(),
                        "status": parts[5].strip().lower(),
                    })
            continue

    flush_expr()

    # 3) Reconcile the Tracker rows onto expressions (matched by lowercased name).
    by_name = {expr.name.strip().lower(): expr for expr in expressions}
    for row in tracker_rows:
        expr = by_name.get(row["expression"].strip().lower())
        if expr is not None:
            expr.five_word_meaning = row["five"]
            expr.status = row["status"] or "new"

    lesson_date = _parse_date(tracker_rows[0]["date"]) if tracker_rows else None
    day_number = _parse_day_number(header.get("day", ""))

    return ParsedLesson(
        day_number=day_number,
        title=lesson_title or f"Day {day_number} — {header.get('mode', 'Lite')} Lesson",
        mode=header.get("mode", "Lite"),
        focus_theme=header.get("focus theme", ""),
        dialogue_topic=header.get("dialogue topic", ""),
        difficulty=header.get("difficulty", ""),
        lesson_focus=lesson_focus,
        review_items=header.get("review items") or header.get("review items reused", ""),
        avoiding_repeats=header.get("avoiding recent repeats from our chat", ""),
        speaking_practice="\n".join(speaking_lines).strip(),
        output_correction="\n".join(output_lines).strip(),
        tomorrow_preview=tomorrow_preview,
        date=lesson_date,
        source_filename=source_filename,
        expressions=expressions,
        upgrades=upgrades,
    )


def parse_lesson_file(path: str | Path) -> ParsedLesson:
    """Parse a single lesson file (always UTF-8)."""
    path = Path(path)
    return parse_lesson_text(path.read_text(encoding="utf-8"), source_filename=path.name)


def parse_all(raw_dir: str | Path) -> list[ParsedLesson]:
    """Parse every ``day*`` file in ``raw_dir``, sorted by day number."""
    raw_dir = Path(raw_dir)
    lessons = [parse_lesson_file(p) for p in sorted(raw_dir.glob("day*")) if p.is_file()]
    lessons.sort(key=lambda lesson: lesson.day_number)
    return lessons


def _parse_day_number(value: str) -> int:
    match = re.search(r"\d+", value)
    return int(match.group()) if match else 0


def _parse_date(value: str) -> datetime.date | None:
    try:
        return datetime.datetime.strptime(value.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None
