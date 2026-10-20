#!/usr/bin/env python3
"""Generate every output from tokens/tokens.json.

    python3 scripts/build_tokens.py          # write dist/ and litsa_design/tokens.py
    python3 scripts/build_tokens.py --check  # fail if any output is out of date (CI)

Outputs:
    dist/tokens.css          CSS custom properties, for web projects
    dist/tokens.json         flat {name: value}, for anything else
    litsa_design/tokens.py   Python constants, for the flyer, deck and spreadsheet scripts
    gallery/tokens.css       copy used by the gallery page
    gallery/tokens.source.json  the source file, which the gallery reads for names and notes
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tokens" / "tokens.json"
NAME = re.compile(r"^[a-z][a-z0-9-]*$")
HEADER = "Generated from tokens/tokens.json by scripts/build_tokens.py. Do not edit; change tokens.json and rebuild."


def load(path: Path = SOURCE) -> dict[str, dict[str, str]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    groups = {k: v for k, v in raw.items() if not k.startswith("$")}
    seen = {}
    for group, tokens in groups.items():
        for name, spec in tokens.items():
            if not NAME.match(name):
                raise ValueError(f"{group}.{name}: names are lowercase letters, digits and hyphens")
            if name in seen:
                raise ValueError(f"{name} appears in both {seen[name]} and {group}")
            if "value" not in spec:
                raise ValueError(f"{group}.{name}: missing value")
            seen[name] = group
    return groups


def flat(groups: dict) -> dict[str, str]:
    return {name: spec["value"] for tokens in groups.values() for name, spec in tokens.items()}


def css(groups: dict) -> str:
    lines = [f"/* {HEADER} */", ":root {"]
    for group, tokens in groups.items():
        lines.append(f"  /* {group} */")
        lines += [f"  --{name}: {spec['value']};" for name, spec in tokens.items()]
    lines.append("}")
    return "\n".join(lines) + "\n"


def python(groups: dict) -> str:
    out = [f'"""{HEADER}"""', "", "TOKENS = {"]
    out += [f"    {name!r}: {value!r}," for name, value in flat(groups).items()]
    out += ["}", "", "# Colors as attributes, for scripts that draw: tokens.INK, tokens.BLUE_DEEP, ..."]
    out += [f"{name.upper().replace('-', '_')} = {spec['value']!r}" for name, spec in groups.get("color", {}).items()]
    return "\n".join(out) + "\n"


def outputs(groups: dict) -> dict[Path, str]:
    c = css(groups)
    return {
        ROOT / "dist" / "tokens.css": c,
        ROOT / "dist" / "tokens.json": json.dumps(flat(groups), indent=2) + "\n",
        ROOT / "litsa_design" / "tokens.py": python(groups),
        ROOT / "gallery" / "tokens.css": c,
        ROOT / "gallery" / "tokens.source.json": SOURCE.read_text(encoding="utf-8"),
    }


def main(argv: list[str]) -> int:
    files = outputs(load())
    if "--check" in argv:
        stale = [p for p, text in files.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        for p in stale:
            print(f"out of date: {p.relative_to(ROOT)}")
        if stale:
            print("Run: python3 scripts/build_tokens.py")
        return 1 if stale else 0
    for path, text in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
