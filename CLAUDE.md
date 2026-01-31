# Claude Code Notes

This is the **Agent Factory** - a system for building and improving AI agents using accumulated knowledge.

## Quick Reference

| Directory | Purpose |
|-----------|---------|
| `knowledge/` | Agent-building wisdom (concepts, patterns, tools, evals) |
| `blueprints/` | Reusable templates (researcher, writer, coder, business) |
| `factory/` | Agent Builder - the agent that creates agents |
| `01-baseline/` | Test variant: baseline EVA config |
| `02-minimal/` | Test variant: minimal rules |

## Key Files

| File | Purpose |
|------|---------|
| PLAN.md | Full plan, status, implementation details |
| knowledge/README.md | How to use the knowledge base |
| blueprints/README.md | How to use blueprints |
| factory/IDENTITY.md | Agent Builder identity |

## How It Works

```
1. Knowledge + Blueprints → Agent Builder
2. Agent Builder → New Agents
3. New Agents → Business Value
4. Learnings → Knowledge (loop)
```

## Getting Started

**To create a new agent:**
1. Go to `factory/` and work with Agent Builder
2. Or copy a blueprint: `cp -r blueprints/researcher/ my-agent/`
3. Customize the files
4. Register in `~/.openclaw/openclaw.json`

**To understand agent patterns:**
- Start with `knowledge/foundations/ai-agents-course.md`
- Browse patterns in `knowledge/patterns/`

**To improve agents:**
- Run evals (see `knowledge/evals/`)
- Document lessons learned
- Update agent configuration

## When Working Here

1. Check PLAN.md for current status
2. Use knowledge base before making decisions
3. Start from blueprints, don't reinvent
4. Document what you learn
