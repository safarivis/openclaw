# Why This Agent Exists

## Problem Statement

External knowledge (videos, articles, docs) contains valuable patterns but gets lost in chat history. Without systematic ingestion, the same insights get rediscovered repeatedly. Knowledge base grows stale or inconsistent.

## Target Users

- Developers finding useful content (YouTube videos, articles)
- Teams building shared knowledge bases
- Anyone saying "add this to our knowledge"

**Current workflow without this agent:**
1. Watch video / read article
2. Manually extract insights
3. Figure out where to put them
4. Often skip the effort → knowledge lost

## Success Criteria

| Criteria | Target | How to Measure |
|----------|--------|----------------|
| Knowledge captured | 90%+ of key insights extracted | Compare to manual notes |
| Proper placement | Content goes to correct knowledge/ path | Review file locations |
| No duplicates | Compare before adding | Ingestion workflow |

## Constraints

- Never add to knowledge base without human approval
- Always compare against existing content first
- Don't overwrite - merge or create new sections
- Cite sources for traceability

## Key Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Human approval gate | Required before save | Prevents garbage in |
| Compare step | Check existing before adding | Avoids duplicates |
| Structured output | Markdown with sections | Consistent format |

## Out of Scope

- Automatic scheduled ingestion
- Ingesting entire websites
- Real-time content monitoring

---

**Status:** Approved
**Date:** 2026-02-01
