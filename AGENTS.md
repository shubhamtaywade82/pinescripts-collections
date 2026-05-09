# AGENTS.md — pinescripts-collections

Instructions for AI coding agents working in this repository.

## Purpose

This repo holds **TradingView Pine Script** sources: a curated **indicator/strategy collection** plus the **`pinescript-agents`** toolkit (docs, templates, examples, and Claude-oriented automation). All scripts are **broker-agnostic**; they do not call exchange or broker APIs.

## Layout

| Path | Role |
|------|------|
| `indicators/` | `indicator()` scripts, grouped by topic (`htf-volume/`, `smc/`, `trendlines/`, `whales/`, `utilities/`, …) |
| `strategies/` | `strategy()` scripts (e.g. `strategies/trendlines/`) |
| `pinescript-agents/` | Pine v6 reference docs, `examples/`, `projects/`, `templates/`, tooling — **not** a separate git repo (no nested `.git` here) |

When adding a new script, place it under the closest topic folder inside `indicators/` or `strategies/`. Prefer a short, stable subdirectory name (kebab-case) if you introduce a new category.

## Pine Script defaults

- Target **`//@version=6`** unless the file is explicitly legacy.
- Preserve or add the **MPL 2.0** license header and author line where the rest of the file uses that pattern.
- Set **`max_bars_back`**, **`max_lines_count`**, **`max_labels_count`**, **`max_boxes_count`** when using many drawings so TradingView does not hit runtime limits.
- **Syntax:** Pine has strict line-continuation rules; long ternaries and chained expressions often must stay on one line or use explicit continuation indentation. See `pinescript-agents/docs/pinescript-v6/quick-reference/syntax-basics.md`.
- **History-sensitive functions:** If the compiler warns that a user-defined function must run every bar, assign its result to a series variable at global scope and use that in conditions (do not rely on short-circuit `and`/`or` skipping the call).
- **`plotshape` / `plotchar` `size`:** The `size` argument must be a **const** (e.g. `size.small`). You cannot pass a value derived from `input.string` or a helper that returns `size.*`; use separate `plotshape` calls per size or fixed literals.
- **Tables vs drawings:** Pine cannot force another study’s UI above yours. For readability, prefer fewer full-chart `box` fills or gate heavy overlays behind inputs.

## Git

- **Do not** add a nested `.git` under `pinescript-agents/` (or anywhere inside this repo). One top-level `.git` only; otherwise `git add` records a gitlink and clones miss real files.
- Use **`git mv`** when reorganizing `.pine` paths so renames stay traceable.

## Verification

- There is no local Pine compiler in this repo. After substantive edits, the user should paste into **TradingView Pine Editor** and fix any reported errors/warnings.
- For behavior-heavy changes, describe what to check on the chart (timeframe, symbol, inputs).

## Related docs

- In-repo Pine assistant onboarding and rules: `pinescript-agents/CLAUDE.md`
- v6 language and patterns: `pinescript-agents/docs/pinescript-v6/`

## Default implementation references (required)

When building any **new Pine indicator or strategy** in this repo, agents must reference both:

1. `pinescript-agents` skills/docs (workflow + syntax/behavior guidance), and
2. the local advanced examples under `indicators/agent-examples/` as style/UX baselines.

Use these local files as default implementation/style references unless the user explicitly asks otherwise:

- `indicators/agent-examples/market-structure-bos-choch.pine`
- `indicators/agent-examples/order-blocks-simple.pine`
- `indicators/agent-examples/pivot-points-traditional.pine`
- `indicators/agent-examples/support-resistance-basic.pine`
- `indicators/agent-examples/bollinger-squeeze-detector.pine`
- `indicators/agent-examples/mtf-trend-alignment.pine`
- `indicators/agent-examples/multi-timeframe-rsi.pine`

Expected style alignment for new scripts:

- Lux-style grouped inputs and naming (`Mode`, `Style`, structure/signal/visual groups).
- Consistent color system (`#089981` bullish, `#f23645` bearish, neutral muted grays).
- Drawings/labels that remain readable on dark themes.
- Stable behavior for history-sensitive functions (compute series globally when needed).
