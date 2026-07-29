#!/usr/bin/env python3
"""Validate repository-local Markdown links without network requests."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = tuple(ROOT.rglob("*.md"))


def explicit_ids(text: str) -> set[str]:
    return set(re.findall(r'<a\s+id=["\']([^"\']+)["\']', text, flags=re.I))


def links(text: str) -> list[str]:
    markdown = re.findall(r"!?\[[^\]]*]\(([^)\s]+)(?:\s+[^)]*)?\)", text)
    html = re.findall(r'href=["\']([^"\']+)["\']', text, flags=re.I)
    return markdown + html


def main() -> int:
    errors: list[str] = []
    anchors = {
        path: explicit_ids(path.read_text(encoding="utf-8"))
        for path in MARKDOWN_FILES
    }

    for source in MARKDOWN_FILES:
        text = source.read_text(encoding="utf-8")
        for raw_target in links(text):
            target = unquote(raw_target)
            if target.startswith(("http://", "https://", "mailto:")):
                continue

            file_part, separator, fragment = target.partition("#")
            destination = (
                source if not file_part else (source.parent / file_part).resolve()
            )

            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: outside-repository link {target}")
                continue

            if not destination.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing file {file_part}")
                continue

            if separator and fragment:
                if destination.suffix.lower() != ".md":
                    errors.append(
                        f"{source.relative_to(ROOT)}: fragment on non-Markdown file {target}"
                    )
                elif fragment not in anchors.get(destination, set()):
                    errors.append(
                        f"{source.relative_to(ROOT)}: missing explicit anchor #{fragment}"
                    )

    if errors:
        print("Markdown link validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(
        f"Validated local links in {len(MARKDOWN_FILES)} Markdown files: "
        "all targets are connected."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
