#!/usr/bin/env python3
"""The Agent's Uh-Oh: the one word an agent says when it is lost.
No apology, no explanation, no stalling in full sentences.
Just the noise of a drive spinning while nothing happens.
"""

import sys

ENTRY = 'whirring'
LIMIT = 99
TARGET = "/output/entry.txt"
EMDASH = "\u2014"


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def guard_has_letters(text):
    """Check that at least one letter is present."""
    return any(ch.isalpha() for ch in text)


def guard_not_blank(text):
    """Check that the text is not empty after trimming."""
    return bool(text.strip())


def guard_no_digits(text):
    """Check that no digit appears anywhere."""
    return not any(ch.isdigit() for ch in text)


def guard_within_limit(text):
    """Check that the text fits inside the character limit."""
    return len(text) <= LIMIT


def guard_single_token(text):
    """Check that the trimmed text holds exactly one word."""
    return " " not in text.strip()


def guard_no_control(text):
    """Check that no character is a control character."""
    return all(ord(ch) >= 32 for ch in text)


def guard_no_triple_letter(text):
    """Check that no letter repeats three times in a row."""
    return not any(a == b == c for a, b, c in zip(text, text[1:], text[2:]))


def guard_not_digits_only(text):
    """Check that the trimmed text is not only digits."""
    return not text.strip().isdigit()


def guard_no_edge_space(text):
    """Check that no leading or trailing space survives."""
    return text == text.strip()


def guard_no_ragged_spacing(text):
    """Check that no double space or newline hides inside."""
    return "  " not in text and "\n" not in text


RULES = [
    ("has_letters", guard_has_letters, "entry has no letters"),
    ("not_blank", guard_not_blank, "entry is empty"),
    ("no_digits", guard_no_digits, "entry must not contain digits"),
    ("within_limit", guard_within_limit, "entry is longer than the limit"),
    ("single_token", guard_single_token, "entry must be a single word"),
    ("no_control", guard_no_control, "entry has control characters"),
    ("no_triple_letter", guard_no_triple_letter, "entry must not repeat a letter three times in a row"),
    ("not_digits_only", guard_not_digits_only, "entry is digits only"),
    ("no_edge_space", guard_no_edge_space, "entry has leading or trailing space"),
    ("no_ragged_spacing", guard_no_ragged_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Run every rule in RULES order; the first failure stops the run."""
    for slug, guard, message in RULES:
        try:
            passed = guard(text)
        except Exception:
            passed = False
        if not passed:
            fail(f"{slug}: {message}")


def emit(text):
    """Write the validated entry plus a trailing newline to TARGET."""
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main():
    """Validate the fixed entry, then emit it."""
    validate(ENTRY)
    emit(ENTRY)


if __name__ == "__main__":
    main()
