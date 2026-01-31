# Agent Factory Plan

## Goal

Build an agent factory that uses accumulated knowledge to build and improve agents for running businesses.

## Structure

```
~/clawd-lab/
├── CLAUDE.md                 ← Quick reference
├── PLAN.md                   ← Status and plan (this file)
├── knowledge/                ← Agent-building knowledge base
│   ├── README.md
│   ├── foundations/          ← Core concepts
│   │   └── ai-agents-course.md
│   ├── patterns/             ← Design patterns
│   │   ├── context-engineering.md
│   │   ├── reflection.md
│   │   ├── multi-agent.md
│   │   ├── guardrails.md
│   │   └── memory.md
│   ├── tools/                ← Tool design guides
│   │   └── README.md
│   └── evals/                ← Evaluation methods
│       └── README.md
├── blueprints/               ← Reusable agent templates
│   ├── README.md
│   ├── researcher/           ← Research agent template
│   ├── writer/               ← Writing agent template
│   ├── coder/                ← Coding agent template
│   └── business/             ← Business ops template
├── factory/                  ← Agent Builder workspace
│   ├── IDENTITY.md
│   ├── SOUL.md
│   ├── AGENTS.md
│   ├── TOOLS.md
│   └── NOTES.md
├── brand-agent/              ← First business agent (brand strategy)
│   ├── IDENTITY.md
│   ├── SOUL.md
│   ├── AGENTS.md
│   ├── TOOLS.md
│   └── NOTES.md
├── 01-baseline/              ← Test variant (existing)
└── 02-minimal/               ← Test variant (existing)
```

## Current Status

### Phase 1: Knowledge Base ✅
- [x] Create directory structure
- [x] Write ai-agents-course.md (core concepts)
- [x] Create pattern files (context, reflection, multi-agent, guardrails, memory)
- [x] Document tool design principles
- [x] Create eval guides

### Phase 2: Blueprints ✅
- [x] Create blueprints structure
- [x] Build researcher blueprint
- [x] Build writer blueprint
- [x] Build coder blueprint
- [x] Build business blueprint
- [x] Create blueprint README

### Phase 3: Agent Builder ✅
- [x] Create factory workspace
- [x] Write IDENTITY.md for Agent Builder
- [x] Write SOUL.md, AGENTS.md, TOOLS.md
- [x] Document in NOTES.md

### Phase 4: Integration ✅
- [x] Register Agent Builder in openclaw.json
- [x] Test: Agent Builder creates new agent (Brand Agent from business blueprint)
- [x] Build first business agent (Brand Agent)
- [ ] Test: compare agents with same prompts

## Registered Agents

| Agent | ID | Workspace | Status |
|-------|-----|-----------|--------|
| Agent Builder | `agent-builder` | `/home/louisdup/clawd-lab/factory` | Registered |
| Brand Agent | `brand-agent` | `/home/louisdup/clawd-lab/brand-agent` | Registered |

## Key Concepts (Quick Reference)

| Concept | What It Is |
|---------|-----------|
| ReAct Loop | Reason → Act → Observe → Loop |
| Task Decomposition | Break tasks into LLM-sized pieces |
| Context Engineering | What info agent has access to |
| Tool Design | Interface + implementation |
| Reflection | Self-critique and revise |
| Multi-Agent | Sequential, parallel, hierarchical |
| Guardrails | Quality gates, validation |
| Memory | Short-term, long-term, lessons learned |
| Evals | Component + end-to-end |

## Verification Checklist

- [x] Agent Builder can read knowledge base
- [x] Agent Builder can create new agent from blueprint
- [x] New agent (Brand Agent) runs successfully in OpenClaw
- [ ] Can compare two agent variants with same prompts

## Business Agent Types

| Type | Status | Agent |
|------|--------|-------|
| Brand / Marketing | ✅ Created | `brand-agent` |
| Lead generation / sales | Planned | - |
| Customer support | Planned | - |
| Content creation | Planned | - |
| Market research | Planned | - |
| Operations / automation | Planned | - |
| Financial tracking | Planned | - |

## Next Steps

1. **Test Brand Agent** - Run it and verify it works
2. **Build more business agents** - Lead gen, support, content
3. **Set up agent comparison** - Same prompts, different configs
4. **Add lessons learned** - Feed back into knowledge base
