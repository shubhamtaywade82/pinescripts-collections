# Pine Script Development Workspace

This workspace is configured with the **Pine Script Agents** suite to assist in building professional TradingView indicators and strategies.

## 🛠️ Specialized Skills

The following skills are available and will be automatically activated based on your requests:

- **pine-developer**: Writes production-quality Pine Script v6 code.
- **pine-visualizer**: Breaks down trading ideas into components.
- **pine-debugger**: Adds debugging tools and troubleshoots issues.
- **pine-backtester**: Implements comprehensive testing metrics.
- **pine-optimizer**: Optimizes performance and user experience.
- **pine-manager**: Orchestrates complex multi-part projects.
- **pine-publisher**: Prepares scripts for TradingView publication.

## 📚 Documentation & Reference

Comprehensive Pine Script v6 documentation is available in the `pinescript-agents/docs/` directory:
- [Syntax Basics](pinescript-agents/docs/pinescript-v6/quick-reference/syntax-basics.md)
- [Function Index](pinescript-agents/docs/pinescript-v6/reference-tables/function-index.md)
- [Execution Model](pinescript-agents/docs/pinescript-v6/core-concepts/execution-model.md)
- [Avoiding Repainting](pinescript-agents/docs/pinescript-v6/core-concepts/repainting.md)

## 🎥 YouTube Video Analysis

You can analyze trading strategy videos using the provided tool:
```bash
python3 pinescript-agents/tools/video-analyzer.py "<youtube_url>"
```
*Note: Requires `pip install -r pinescript-agents/requirements.txt`*

## 📁 Project Structure

- `pinescript-agents/`: Core suite with docs, templates, and tools.
- `.cursor/skills/`: Gemini CLI skill definitions migrated from the suite.
- `*.pine`: Your Pine Script files.

## ⚠️ Pine Script v6 Best Practices

- **Version**: Always use `//@version=6`.
- **Line Continuation**: Ensure continuation lines are indented more than the starting line.
- **Ternary Operators**: Keep complex ternary expressions on a single line to avoid syntax errors.
- **Plotting**: Never use `plot()` inside local scopes (if/for/functions). Use conditional plotting instead.
