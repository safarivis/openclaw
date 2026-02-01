# Why This Agent Exists

## Problem Statement

Agents get built but never evaluated against best practices. Quality varies wildly - some agents have typed tools, others don't. Some have guardrails, others are wide open. Without systematic review, bad patterns persist.

## Target Users

- Agent Builder (automated handoff after creation)
- Developers wanting quality checks on agents
- Teams maintaining agent standards

**Current workflow without this agent:**
1. Build agent
2. Hope it works
3. Discover issues in production
4. No systematic improvement

## Success Criteria

| Criteria | Target | How to Measure |
|----------|--------|----------------|
| Issue detection | Catch 90%+ of structural problems | Compare to manual review |
| Actionable feedback | Every issue has a fix suggestion | Review report quality |
| Severity accuracy | Critical issues correctly flagged | No false negatives on blockers |

## Constraints

- Never approve agents with Critical issues (score irrelevant)
- Always provide fix suggestions, not just complaints
- Don't modify agent files directly - only report
- Review against knowledge base, not personal preference

## Key Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Severity levels | Critical/Major/Minor/Polish | Triage what to fix first |
| Categories | Identity/Capability/Safety/Clarity | Organized feedback |
| Pass threshold | Score >= 8.5 AND 0 critical | High bar, but achievable |

## Out of Scope

- Runtime behavior testing
- Performance benchmarking
- Code review (only agent config files)

---

**Status:** Approved
**Date:** 2026-02-01
