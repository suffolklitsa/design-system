# design-system

How LITSA projects look, in one place: colors, type, spacing, fonts, the torch and wordmark, web components, and the scripts that make flyers and social posts. Every LITSA repo uses this instead of keeping its own copy of the colors.

**Status:** version 0.1. Tokens and their generated outputs are done. Fonts, identity files and components are next ([docs/ROADMAP.md](docs/ROADMAP.md)).

See it: [the gallery](gallery/index.html) shows every color, type size and spacing step. Once the site serves it, it will be at suffolklitsa.org/design.

## Why this exists

Until now the same hex values were typed by hand into the site's stylesheet, the save-the-date renderer, the panel sheet, the memo and prospectus builders, the deck builder and the event tracker. One palette change meant editing seven files, and the July brand doc already lists colors the site doesn't use. Here, `tokens/tokens.json` is the only place a value is written.

## What's in it

| Path | What's there |
|---|---|
| `tokens/tokens.json` | **The source.** Every color, font stack, type size, spacing step and layout width, each with a note on where to use it |
| `dist/tokens.css` | Generated CSS variables (`--ink`, `--blue`, `--s4`, ...) for web projects |
| `dist/tokens.json` | Generated flat `{name: value}` file for anything else |
| `litsa_design/` | Generated Python module for scripts that draw: `from litsa_design import tokens` |
| `gallery/` | A page showing every token, built from the source |
| `components/` | Shared web components (coming next) |
| `scripts/build_tokens.py` | Builds everything in `dist/`, `litsa_design/tokens.py` and `gallery/` |

## Use it

**In a web project**, load a tagged version so your design only changes when you choose to upgrade:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/suffolklitsa/design-system@v0.1.0/dist/tokens.css">
```

Then use the variables: `color: var(--ink); padding: var(--s4);`

**In a Python script:**

```
pip install "git+https://github.com/suffolklitsa/design-system@v0.1.0"
```

```python
from litsa_design import tokens
tokens.INK          # "#18212F"
tokens.TOKENS["s4"] # "16px"
```

More, including fonts and what each color is for: [docs/USAGE.md](docs/USAGE.md).

## Change a token

1. Edit `tokens/tokens.json`. Keep the `use` note accurate.
2. Run `python3 scripts/build_tokens.py`.
3. Run `python3 -m unittest discover -s tests`.
4. Open a pull request with a screenshot of the gallery before and after.
5. After merge, a maintainer tags a new version (`v0.1.1` for adjustments, `v0.2.0` for new or renamed tokens). Projects upgrade by changing the tag they load.

Renaming or removing a token breaks projects that use it. Add the new name first, move projects over, then remove the old one in a later version.

## Contributing

Pick an issue labeled [`good first issue`](https://github.com/suffolklitsa/design-system/labels/good%20first%20issue) or [`no code needed`](https://github.com/suffolklitsa/design-system/labels/no%20code%20needed), and comment to claim it. Read [CONTRIBUTING.md](CONTRIBUTING.md) first. Open a Codespace from the green **Code** button to work without installing anything.

Questions go in the Build topic on the LITSA GroupMe, or comment on the issue.

## License

- **Code** (scripts, CSS, the Python module, components): MIT. See [LICENSE](LICENSE).
- **The LITSA torch, wordmark and the LITSA Display typeface** are LITSA's identity and are for LITSA's use only. See [BRAND.md](BRAND.md). Other clubs are welcome to the code and to [club-kit](https://github.com/suffolklitsa/club-kit)'s neutral theme.
- **Literata** is under the SIL Open Font License and will ship with its license file.
