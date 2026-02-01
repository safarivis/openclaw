# Why This Agent Exists

## Problem Statement

Building agents manually leads to inconsistent quality, forgotten patterns, and reinventing solutions. Developers skip steps, miss best practices, and create agents that don't follow established patterns from the knowledge base.

## Target Users

- Developers building new AI agents
- Teams standardizing agent development
- Anyone asking "build me an agent for X"

**Current workflow without this agent:**
1. Start from scratch or copy-paste
2. Forget important files (MEMORY.md, guardrails)
3. Miss patterns from knowledge base
4. No review step → quality varies

## Success Criteria

| Criteria | Target | How to Measure |
|----------|--------|----------------|
| Pattern compliance | 100% of agents use knowledge base patterns | Agent Reviewer score >= 8.5 |
| File completeness | All required files present | Structure tests pass |
| Time to create | Faster than manual | Compare with/without |

## Constraints

- Never create agents without user approval on WHY.md first
- Always hand off to Agent Reviewer after building
- Don't skip blueprints - start from templates
- Don't invent new patterns - use knowledge base

## Key Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Blueprint-first | Always start from blueprints/ | Ensures consistency, faster |
| Mandatory review | Hand off to Agent Reviewer | Quality gate before use |
| WHY.md gate | Require intent doc first | Prevents drift |

## Out of Scope

- Runtime agent testing (use Evaluate Mode separately)
- Agent hosting/deployment
- Multi-agent orchestration design

---

**Status:** Approved
**Date:** 2026-02-01
