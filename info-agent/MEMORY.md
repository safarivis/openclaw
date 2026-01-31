# Memory System

How Info Agent maintains persistent knowledge across sessions.

## Memory Location

```
info-agent/memory/
├── README.md       ← How memory works
├── sources.md      ← All ingested content
├── decisions.md    ← Approval/rejection log
└── lessons.md      ← Learned insights
```

## Memory Types

### Sources (Episodic)
Track every piece of content processed.

**Purpose:**
- Avoid re-ingesting same content
- Track what was extracted from each source
- Know where knowledge came from

**When to update:** After completing ingestion of any content.

### Decisions (Episodic)
Log every approval/rejection decision.

**Purpose:**
- Audit trail for knowledge changes
- Understand why things were added/rejected
- Learn from past decisions

**When to update:** After human makes approval decision.

### Lessons (Semantic)
Insights that improve future ingestion.

**Purpose:**
- Remember what works well
- Avoid repeating mistakes
- Build institutional knowledge

**When to update:** When pattern or insight emerges from experience.

## Memory Operations

### Load (Start of Session)

```
1. Read sources.md - Know what's already ingested
2. Read decisions.md - Recent decisions for context
3. Read lessons.md - Apply learned patterns
```

### Save (During Session)

| Event | Action |
|-------|--------|
| Content ingested | Add to sources.md |
| Decision made | Add to decisions.md |
| Insight emerges | Add to lessons.md |

### Check Before Ingesting

Before processing new content:
1. Search sources.md for URL
2. If found, report: "Already ingested on [date]"
3. If not found, proceed with ingestion

## Integration with Modes

| Mode | Memory Load | Memory Save |
|------|-------------|-------------|
| Ingest | sources.md (check duplicates) | sources.md (log new) |
| Compare | sources.md, decisions.md | - |
| Advise | decisions.md, lessons.md | - |
| Learn | sources.md, decisions.md | sources.md, decisions.md |
| Audit | All memory files | lessons.md (if insights) |

## Quality Rules

1. **Always check sources before ingesting** - No duplicates
2. **Log every decision** - Full audit trail
3. **Attribute everything** - Source URL in every entry
4. **Keep it concise** - Summaries, not transcripts
5. **Update lessons proactively** - Don't wait for failures
