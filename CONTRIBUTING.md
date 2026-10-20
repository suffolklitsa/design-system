# Contributing to design-system

The org-wide guide is at [suffolklitsa/.github](https://github.com/suffolklitsa/.github/blob/main/CONTRIBUTING.md). This page covers what's specific here.

## Rules for this repo

- **`tokens/tokens.json` is the only file you edit by hand** for colors, type, spacing and layout. Everything in `dist/`, `litsa_design/tokens.py` and `gallery/tokens.*` is generated. CI fails if they're out of date.
- **Every token has a `use` note** saying where it belongs. A color with no clear use isn't ready to add.
- **Check contrast.** Any text color must reach WCAG AA (4.5:1) on the backgrounds it's used on. Say what you checked in the pull request.
- **No breaking renames.** Add the new token, move projects over, then remove the old one in a later version.
- **Identity files** (torch, wordmark, LITSA Display) are covered by [BRAND.md](BRAND.md), not the MIT license. Don't add other organizations' logos or fonts.

## Checks

```
python3 scripts/build_tokens.py
python3 -m unittest discover -s tests
```

Open `gallery/index.html` through a local server to see your change: `python3 -m http.server 8000 -d gallery`.

## Releasing (maintainers)

After a batch is promoted from `staging` to `main`, tag `main` (`git tag v0.1.1 && git push --tags`) and note the change in [docs/CHANGELOG.md](docs/CHANGELOG.md). jsDelivr serves the tag within minutes.
