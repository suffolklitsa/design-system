# Using the design system

## Colors and where they go

| Token | Value | Use |
|---|---|---|
| `ink` | #18212F | Main text and headings |
| `ink-2` | #3A4657 | Secondary text |
| `ink-3` | #657282 | Captions, metadata, placeholders |
| `line` | #D5DBE3 | Borders and dividers |
| `line-soft` | #E6EAEF | Subtle dividers inside cards |
| `paper` | #F7F8FA | Page background |
| `paper-2` | #FFFFFF | Cards, panels, inputs |
| `blue` | #1769E0 | Primary buttons and actions |
| `blue-deep` | #0F4FAB | Links and accent text on light backgrounds |
| `gold` | #E5AD2D | The torch accent and focus outlines. Never body text. |

The source of truth is `tokens/tokens.json`; this table is a reading aid.

## Type

- **Display** (`--display`): LITSA Display, for headings, labels and the wordmark.
- **Body** (`--body`): Literata, for running text.
- Sizes run `t-xs` (12px) to `t-5xl` (82px). Body text on the site is `t-md` (18px); interfaces use `t-base` (16px).
- Keep running text within `--measure` (58ch).

## Fonts

Until the fonts move into this repo, projects served from suffolklitsa.org load them from the site:

```css
@font-face { font-family: "LITSA Display"; src: url("/static/font/LITSADisplay.woff2") format("woff2"); font-display: swap; }
@font-face { font-family: "Literata"; src: url("/static/font/literata-roman.woff2") format("woff2"); font-display: swap; }
```

Projects elsewhere fall back to the next font in each stack.

## Versions

Load a tag (`@v0.1.0`), never `@main`, so a change here can't surprise a live project. The changelog is in `docs/CHANGELOG.md`.
