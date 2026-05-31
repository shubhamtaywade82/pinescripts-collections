---
description: Pine Script v6 workflow rules tailored for Kimi CLI tool-based operation
alwaysApply: true
---

# Pine Script v6 — Kimi Workflow Rules

## Tool-Based Operation

Kimi operates via explicit `Read`, `Write`, `Edit`, `Bash`, and `Agent` calls. There is no implicit skill activation.

### Before Writing Any Pine Script Code

1. **Read the relevant skill** from `.kimi/skills/<skill>/SKILL.md` if the task matches a skill domain.
2. **Read `AGENTS.md`** at the repo root for canonical repo-wide conventions.
3. **Read this file (`KIMI.md`)** for Pine-specific syntax guardrails.

### Path Conventions

| Purpose | Path |
|---------|------|
| New agent projects | `pinescript-agents/projects/` |
| Collection indicators | `indicators/<topic>/` |
| Collection strategies | `strategies/<topic>/` |
| Templates | `pinescript-agents/templates/` |
| Examples | `pinescript-agents/examples/` or `indicators/agent-examples/` |
| Docs | `pinescript-agents/docs/pinescript-v6/` |

### Skill Activation Matrix

| User Intent | Skill to Read |
|-------------|---------------|
| "Create/write/code a Pine Script" | `pine-developer` |
| "How would I build..." / concept planning | `pine-visualizer` |
| "Debug/fix/error" | `pine-debugger` |
| "Backtest/metrics/win rate" | `pine-backtester` |
| "Optimize/improve/faster UX" | `pine-optimizer` |
| Complex multi-step build | `pine-manager` |
| "Publish/release" | `pine-publisher` |

### Syntax Guardrails (Non-Negotiable)

1. **Ternaries on one line** — never split `? :` across lines.
2. **Plot scope** — never call `plot()` inside `if`, `for`, or functions.
3. **Line continuation** — continuation lines must be indented MORE than the start line.
4. **Bool conditions** — `if`/`switch`/ternary conditions must be explicit `bool`.
5. **History consistency** — precompute history-dependent functions globally, branch on series.

### Verification Step

After delivering Pine Script code, always remind the user:
> "There is no local Pine compiler. Please paste this into TradingView Pine Editor to verify syntax and runtime behavior."

### Example Workflow

**User**: "Create an RSI divergence indicator"

**Kimi actions**:
1. `Read` `.kimi/skills/pine-developer/SKILL.md`
2. `Read` `AGENTS.md`
3. `Read` `KIMI.md` (this file)
4. `Read` relevant examples (`indicators/agent-examples/...`)
5. Write the script to `indicators/<topic>/` or `pinescript-agents/projects/`
6. Remind user to verify in TradingView
