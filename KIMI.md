# Pine Script Development Assistant — Kimi Instructions

## Overview

This workspace contains the **pinescript-agents** suite for building professional TradingView indicators and strategies. As Kimi, you operate via explicit tool calls (`Read`, `Write`, `Edit`, `Bash`, `Agent`, etc.). There is no native skill auto-discovery — you must **read skill files on demand**.

## ⚠️ CRITICAL: Pine Script Syntax Rules

### Line Continuation — NEVER Split These Across Lines

Pine Script v6 does NOT support arbitrary line breaks. These cause "end of line without line continuation" errors:

**WRONG:**
```pinescript
text = regressionMode == "Static" ? "Static Regression" :
       regressionMode == "Live" ? "Live Regression" :
       "Regression Statistics"
```

**CORRECT — Keep on one line:**
```pinescript
text = regressionMode == "Static" ? "Static Regression" : regressionMode == "Live" ? "Live Regression" : "Regression Statistics"
```

**Rule**: Ternary operators (`? :`), logical expressions (`and`, `or`), and arithmetic spanning lines MUST have continuation lines indented MORE than the starting line, OR be kept on a single line. When in doubt, use single lines for complex expressions.

See `pinescript-agents/docs/pinescript-v6/quick-reference/syntax-basics.md` for complete line wrapping rules.

### CRITICAL: Plot Scope Restriction

**NEVER use `plot()` inside local scopes** — This causes "Cannot use 'plot' in local scope" error.

```pinescript
// ❌ WRONG — These will ALL fail:
if condition
    plot(value)  // ERROR!

for i = 0 to 10
    plot(close[i])  // ERROR!

myFunc() =>
    plot(close)  // ERROR!

// ✅ CORRECT — Use these patterns instead:
plot(condition ? value : na)  // Conditional plotting
plot(value, color=condition ? color.blue : color.new(color.blue, 100))  // Conditional styling

// For dynamic drawing in local scopes, use:
if condition
    line.new(...)  // OK
    label.new(...)  // OK
    box.new(...)   // OK
```

## Path Resolution for This Monorepo

The canonical pinescript-agents bundle lives at `pinescript-agents/`. Resolve paths as follows:

| What | Path |
|------|------|
| Skills | `pinescript-agents/.claude/skills/<skill>/SKILL.md` |
| Docs | `pinescript-agents/docs/pinescript-v6/...` |
| Templates | `pinescript-agents/templates/...` |
| Examples | `pinescript-agents/examples/...` |
| Projects | `pinescript-agents/projects/...` |
| Tools | `pinescript-agents/tools/...` |
| Kimi skills (local) | `.kimi/skills/<skill>/SKILL.md` |

## Skill Activation (Manual — Read on Demand)

Unlike Claude Code, Kimi does **not** auto-activate skills. When a user request matches a skill domain, **explicitly read the skill file** before proceeding.

| Skill | Trigger | File to Read |
|-------|---------|--------------|
| **pine-developer** | "Create", "write", "implement", "code" Pine Script | `.kimi/skills/pine-developer/SKILL.md` |
| **pine-visualizer** | "How would I build", "break down", conceptual planning | `.kimi/skills/pine-visualizer/SKILL.md` |
| **pine-debugger** | "Debug", "fix", "error", "not working" | `.kimi/skills/pine-debugger/SKILL.md` |
| **pine-backtester** | "Backtest", "performance", "metrics", "win rate" | `.kimi/skills/pine-backtester/SKILL.md` |
| **pine-optimizer** | "Optimize", "improve", "faster", "better UX" | `.kimi/skills/pine-optimizer/SKILL.md` |
| **pine-manager** | Complex multi-step projects, "build a complete trading system" | `.kimi/skills/pine-manager/SKILL.md` |
| **pine-publisher** | "Publish", "release", "documentation" | `.kimi/skills/pine-publisher/SKILL.md` |

**Workflow**: read skill → follow its instructions → reference docs/templates as needed → deliver.

## YouTube Video Analysis

When a user provides a YouTube URL, run the analyzer immediately (do not ask for permission):

```bash
python pinescript-agents/tools/video-analyzer.py "<youtube_url>"
```

Options:
```bash
# Force Whisper transcription
python pinescript-agents/tools/video-analyzer.py "<url>" --whisper

# Larger Whisper model
python pinescript-agents/tools/video-analyzer.py "<url>" --whisper --model medium

# JSON output
python pinescript-agents/tools/video-analyzer.py "<url>" --json
```

After analysis, show the summary, confirm understanding with the user, then proceed to implementation.

## Key Documentation References

Read these on demand based on the task:

- `pinescript-agents/docs/pinescript-v6/quick-reference/syntax-basics.md` — Core syntax and line wrapping
- `pinescript-agents/docs/pinescript-v6/built-in-functions.md` — Function reference
- `pinescript-agents/docs/pinescript-v6/quick-reference/common-patterns.md` — Common patterns
- `pinescript-agents/docs/pinescript-v6/quick-reference/limitations.md` — Platform limits
- `pinescript-agents/docs/pinescript-v6/debugging/common-errors.md` — Error catalog

## Default Error/Warning Prevention (Required)

Apply these proactively when writing Pine v6 code:

1. **CE10101 — Bool-only conditions**: `if`, `switch`, ternary first operand, and logical conditions must be `bool`. Use explicit checks (`x > 0`, `not na(v)`) or `bool(x)`.
2. **CW10003 — History consistency**: Compute history-dependent functions globally each bar, then branch on precomputed series. Do not call them inside conditionals.
3. **RE10143 — Historical buffer/runtime offset**: Use `max_bars_back(series, n)` for deep history. For drawings anchored in the past, also set `max_bars_back(time, depth)`.
4. **RE10139 — Memory limits**: Minimize `request.*()` calls and payload size. Reuse drawings with setters; delete stale ones.
5. **Type safety with `na`**: Declare explicit type when initializing with `na` (`float x = na`, `label lb = na`, etc.).
6. **Pine v6 hygiene**: Use TradingView-safe timeframe strings (`"60"`, `"240"`, `"D"`), keep `shorttitle` <= 10 chars, use consistent named arguments.

## Project File Management

- New agent-driven projects: work in `pinescript-agents/projects/` (use `blank.pine` as starting point).
- Collection scripts: `.pine` files at the repository root belong to the curated collection; keep changes in-place unless the user asks to move.
- Always update file headers with accurate project info.

## Style Baselines for New Scripts

When building new scripts, reference these local examples for style/UX:

- `indicators/agent-examples/market-structure-bos-choch.pine`
- `indicators/agent-examples/order-blocks-simple.pine`
- `indicators/agent-examples/pivot-points-traditional.pine`
- `indicators/agent-examples/support-resistance-basic.pine`
- `indicators/agent-examples/bollinger-squeeze-detector.pine`
- `indicators/agent-examples/mtf-trend-alignment.pine`
- `indicators/agent-examples/multi-timeframe-rsi.pine`

Expected style:
- Lux-style grouped inputs and naming (`Mode`, `Style`, structure/signal/visual groups).
- Consistent color system (`#089981` bullish, `#f23645` bearish, neutral muted grays).
- Drawings/labels readable on dark themes.
- Stable behavior for history-sensitive functions.

## Quality Standards

All scripts must have:
- ✅ `//@version=6` declaration
- ✅ MPL 2.0 license header where the file uses that pattern
- ✅ Proper `max_bars_back`, `max_lines_count`, `max_labels_count`, `max_boxes_count` when using many drawings
- ✅ No repainting (or clearly documented)
- ✅ `na` value handling
- ✅ Logical input grouping with tooltips
- ✅ Professional visual presentation
- ✅ Comments for complex logic
- ✅ Alert conditions where applicable

## Verification

There is no local Pine compiler. After substantive edits, instruct the user to paste into TradingView Pine Editor and fix any reported errors/warnings. For behavior-heavy changes, describe what to check on the chart (timeframe, symbol, inputs).

## Maintenance

Update the assistant bundle with `git -C pinescript-agents pull`. `.kimi/skills/*` are symlinks into the bundle; do not replace them with stale copies unless you intentionally fork the skills.
