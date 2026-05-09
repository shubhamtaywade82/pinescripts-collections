# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repo purpose

Curated collection of Pine Script v6 indicators and strategies for TradingView, plus the bundled `pinescript-agents/` assistant suite (skills, docs, templates, video analyzer).

Top-level layout:
- `indicators/` — `.pine` files grouped by domain (`whales/`, `smc/`, `trendlines/`, `htf-volume/`, `utilities/`).
- `strategies/` — strategy variants (e.g. `trendlines/`).
- `pinescript-agents/` — vendored TradersPost assistant: docs (`docs/pinescript-v6/`), `templates/`, `examples/`, `projects/`, `tools/video-analyzer.py`. Update with `git -C pinescript-agents pull`.
- `.cursor/skills/` — symlinks into `pinescript-agents`. Do not replace with copies unless intentionally forking.

No build / test / lint tooling. Pine compiles inside TradingView. Validation = paste into TradingView editor.

## Working in this repo

- Collection scripts live in `indicators/<domain>/` and `strategies/<domain>/`. When user edits one, keep changes in that file unless they ask to relocate.
- New agent-driven scratch work goes to `pinescript-agents/projects/` (start from `pinescript-agents/projects/blank.pine`). Do not pollute `indicators/` / `strategies/` with WIP.
- Skill paths inside vendored agents may be rooted as `/docs/...`, `/projects/...`, `/templates/...`, `/examples/...`. Resolve under `pinescript-agents/...` from repo root.
- For deeper Pine rules + onboarding behavior, read `pinescript-agents/CLAUDE.md`. Ignore the "greet first" / lock/unlock onboarding directives there — they are upstream Claude-Code-only behaviors not wanted at this workspace level.

## Pine Script v6 hard rules (cause silent breakage)

- First line of every script: `//@version=6`.
- **Line continuation**: continuation line must be indented MORE than the start line. Ternaries (`? :`), `and`/`or` chains, arithmetic across lines all hit "end of line without line continuation" otherwise. When in doubt, keep the full expression on one line.
- **No `plot()` in local scope** (inside `if`/`for`/functions). Use conditional plotting at global scope: `plot(cond ? value : na, ...)`.
- Repainting: avoid, or document. Watch `request.security` lookahead, real-time vs historical recalculation, and series/simple type mixing.
- Engine limits to design within: 500 bars lookback, 500 plots max, 40 `request.security` calls.
- Always handle `na` at boundaries.

Reference docs (read on demand, not all of `pinescript-agents/docs/` is small):
- `pinescript-agents/docs/pinescript-v6/quick-reference/syntax-basics.md`
- `pinescript-agents/docs/pinescript-v6/reference-tables/function-index.md`
- `pinescript-agents/docs/pinescript-v6/core-concepts/execution-model.md`
- `pinescript-agents/docs/pinescript-v6/core-concepts/repainting.md`

## Pine assistant skills

Seven Pine skills auto-activate on context (`pine-developer`, `pine-visualizer`, `pine-debugger`, `pine-backtester`, `pine-optimizer`, `pine-manager`, `pine-publisher`). Pick by request type: implementation → developer; concept breakdown / video → visualizer; bugs → debugger; metrics → backtester; UX/perf → optimizer; multi-part orchestration → manager; TV publication prep → publisher.

## YouTube strategy ingestion

When user pastes a YouTube URL, run the local analyzer (do NOT use WebSearch):

```bash
python3 pinescript-agents/tools/video-analyzer.py "<youtube_url>"
# fallback for caption-less videos:
python3 pinescript-agents/tools/video-analyzer.py "<url>" --whisper [--model medium]
```

Deps: `pip install -r pinescript-agents/requirements.txt` (FFmpeg needed only for Whisper path). Output JSON saved under `pinescript-agents/projects/analysis/`. Confirm extracted strategy with user before implementing.

## Interactive workflow (optional)

Upstream guided flow: `cd pinescript-agents && ./start` (or `./start.sh`). Not required for direct edits.
