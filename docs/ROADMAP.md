# Roadmap

## 0.1: tokens (done)

- [x] `tokens.json` with notes on use
- [x] Generated CSS, JSON and Python outputs, checked in CI
- [x] Gallery page

## 0.2: fonts and identity

- [ ] LITSA Display and Literata in `fonts/`, with Literata's license file
- [ ] Torch and wordmark source moved here from the site's `vendor/identity/`
- [ ] Reconcile the July brand doc's extra colors (signal green, alert red) and add any that are in real use, with `use` notes and contrast checks

## 0.3: components

- [ ] Inventory of components the site already has
- [ ] Choose whether to base components on an open-source library
- [ ] Header, footer, buttons, form fields, cards, badges, callouts, tables
- [ ] New components the projects need: survey question card, progress bar, ranked results list, bill card, checklist row
- [ ] Gallery shows every component

## 0.4: print and social

- [ ] The save-the-date, flyer, Instagram and newsletter-header renderers move here and read tokens from `litsa_design`

## Adoption

- [ ] The club site loads `dist/tokens.css` instead of its own copy
- [ ] course-planner, ma-lit-bills and the guides use the published tag
- [ ] The scripts in the LITSA workspace that hard-code colors switch to `litsa_design`
