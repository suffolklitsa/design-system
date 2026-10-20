# AGENTS.md

Instructions for AI coding agents working in this repo, and for the people using them. Read README.md and CONTRIBUTING.md too.

## What this repo is

LITSA's shared design tokens and components. `tokens/tokens.json` is the only hand-edited source of colors, type, spacing and layout; everything in `dist/`, `litsa_design/tokens.py` and `gallery/tokens.*` is generated.

## Commands

```
python3 scripts/build_tokens.py           # regenerate outputs
python3 scripts/build_tokens.py --check   # what CI runs
python3 -m unittest discover -s tests
python3 -m http.server 8000 -d gallery    # see the gallery
```

## Rules for this repo

- **Edit `tokens/tokens.json`, then rebuild.** Never edit generated files.
- **Every token has a `use` note.** Text colors must meet WCAG AA contrast on the backgrounds they're used on; say what you checked.
- **No breaking renames.** Add a new token, migrate projects, remove the old one later.
- **Components use tokens only.** No hard-coded colors or sizes.
- **Identity files** (torch, wordmark, LITSA Display) follow BRAND.md, not the MIT license. Don't add other organizations' logos or fonts.

## Rules for every LITSA repo

- **No secrets.** Never write API keys, tokens or passwords into a file, a commit, an issue or a test. Keys come from environment variables. If you find one committed, stop and tell a maintainer.
- **No personal data.** No real names, emails, student records, sign-in sheets or mailing lists in code, tests, fixtures, screenshots or commit messages. Use made-up examples (`jane.doe@example.edu`).
- **No invented law.** Anything stating a rule, statute, case or requirement must come from a source you can link. Never make up a citation. If you can't find the source, say so in the pull request instead of guessing.
- **Small changes.** One issue per pull request. Don't reformat or rename things the issue didn't ask about.
- **Run the checks** listed above before saying the work is done, and report what they printed. If one fails, fix it or say plainly that it fails.
- **Plain writing.** Docs and messages use short, ordinary sentences a first-year law student would follow.
- **Disclose AI use.** The person opening the pull request notes which AI tools helped, in the description. They own every line either way.
