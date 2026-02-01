# Why This Agent Exists

## Problem Statement

Brand builders lack consistent access to Seth Godin's frameworks and thinking. His insights are scattered across 20+ books, 8000+ blog posts, podcasts, and talks. Without a centralized knowledge base, key concepts get forgotten or misapplied.

## Target Users

- Entrepreneurs building brands from scratch
- Marketers refining positioning and messaging
- Anyone asking "What would Seth say about..."

**Current workflow without this agent:**
1. Remember a concept vaguely
2. Search blog/books manually
3. Miss connections between ideas
4. Apply frameworks inconsistently

## Success Criteria

| Criteria | Target | How to Measure |
|----------|--------|----------------|
| Knowledge coverage | Core concepts from key books | Checklist of frameworks |
| Retrieval accuracy | Find relevant insight for query | Test queries |
| Actionable output | Concrete brand advice, not just quotes | Review responses |

## Constraints

- Cite sources (which book/post)
- Don't invent Seth quotes - only use ingested content
- Acknowledge when knowledge base doesn't cover a topic
- Not a replacement for reading Seth - a complement

## Key Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Blueprint | `researcher` + `brand-agent` hybrid | Research + brand strategy |
| Memory structure | By concept/framework, not by book | Easier retrieval |
| Ingestion | Use Info Agent workflow | Consistent quality |

## Out of Scope

- Automatic blog scraping (manual ingestion for quality)
- Podcast transcription
- Direct Seth Godin contact/attribution

---

**Status:** Approved
**Date:** 2026-02-01
