# Decisions

**2026-10-20. tokens.json is the single source.** CSS, JSON and Python are generated from it and CI checks they match. No hand-edited copies.

**2026-10-20. Token names match the site's existing CSS variables** (`ink`, `blue-deep`, `s4`), so the site can switch to this file without renaming anything.

**2026-10-20. Versions are git tags served by jsDelivr.** No npm package to maintain. Projects pin a tag.

**2026-10-20. Code is MIT; identity is not.** The torch, wordmark and LITSA Display stay LITSA's (BRAND.md). club-kit carries a neutral theme for other clubs.

**2026-10-19. Components may build on open source.** Whether to adopt a library is an open issue; the deciding factors are size, accessibility and how easily members can learn it.
