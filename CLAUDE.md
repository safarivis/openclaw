# Claude Code Notes

This is the **Agent Factory** - a system for building and improving AI agents using accumulated knowledge.

## IMPORTANT: Agent Creation Workflow

**When asked to create, build, or make a new agent, ALWAYS follow this workflow:**

```
┌─────────────────────────────────────────────────────────────┐
│  "Build me an agent for X"                                  │
│                    ↓                                        │
│  1. AGENT BUILDER (factory/)                                │
│     - Read knowledge/foundations/ai-agents-course.md        │
│     - Read knowledge/patterns/ for relevant patterns        │
│     - Select appropriate blueprint from blueprints/         │
│     - Create agent workspace with all files                 │
│     - Register in ~/.openclaw/openclaw.json                 │
│                    ↓                                        │
│  2. AGENT REVIEWER (agent-reviewer/)                        │
│     - Evaluate against knowledge base principles            │
│     - Score on: identity, modes, tools, memory, guardrails  │
│     - Report issues and fixes                               │
│                    ↓                                        │
│  3. IMPLEMENT FIXES                                         │
│     - Apply reviewer recommendations                        │
│     - Re-evaluate until score >= 8.5/10                     │
│                    ↓                                        │
│  4. COMMIT & PUSH                                           │
└─────────────────────────────────────────────────────────────┘
```

**DO NOT manually create agents without using this workflow.**

## Specialized Agents

| Agent | Location | Purpose | When to Use |
|-------|----------|---------|-------------|
| Agent Builder | `factory/` | Creates new agents | "Build/create/make an agent for..." |
| Agent Reviewer | `agent-reviewer/` | Evaluates agents | After creating, or "Review/eval this agent" |
| Info Agent | `info-agent/` | Ingests knowledge | "Ingest this video", YouTube URLs, "add to knowledge" |
| Brand Agent | `brand-agent/` | Brand strategy | Brand-related business tasks |

## Quick Reference

| Directory | Purpose |
|-----------|---------|
| `knowledge/` | Agent-building wisdom (concepts, patterns, tools, evals) |
| `blueprints/` | Reusable templates (researcher, writer, coder, business) |
| `factory/` | Agent Builder - the agent that creates agents |
| `agent-reviewer/` | Agent Reviewer - evaluates agents |
| `info-agent/` | Info Agent - knowledge ingestion |
| `brand-agent/` | Brand Agent - brand strategy |

## Key Files

| File | Purpose |
|------|---------|
| PLAN.md | Full plan, status, implementation details |
| knowledge/foundations/ai-agents-course.md | Core agent concepts (READ FIRST) |
| knowledge/patterns/ | Design patterns for agents |
| blueprints/README.md | How to use blueprints |

## Blueprints Available

| Blueprint | Best For |
|-----------|----------|
| `blueprints/researcher/` | Research, analysis, fact-finding agents |
| `blueprints/writer/` | Content, copy, script writing agents |
| `blueprints/coder/` | Code generation, debugging agents |
| `blueprints/business/` | Sales, support, operations agents |

## Knowledge Ingestion Workflow

**When asked to add knowledge from external content:**

```
1. Use INFO AGENT (info-agent/)
2. Ingest → Compare → Advise → (Human Approval) → Save
3. Never add without approval
```

## Agent Quality Checklist

Every agent must have:
- [ ] Clear IDENTITY.md with mission
- [ ] AGENTS.md with modes + "Done when:" conditions
- [ ] TOOLS.md with typed parameters and returns
- [ ] SOUL.md with actionable principles
- [ ] MEMORY.md + memory/ directory
- [ ] Registered in ~/.openclaw/openclaw.json
- [ ] Reviewed by Agent Reviewer (score >= 8.5)

## When Working Here

1. Check PLAN.md for current status
2. **Use Agent Builder for new agents** (not manual creation)
3. **Use Agent Reviewer after creation**
4. Use Info Agent for knowledge ingestion
5. Start from blueprints, don't reinvent
6. Document what you learn
