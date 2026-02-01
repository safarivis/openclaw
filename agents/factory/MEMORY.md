# Memory System

How Agent Builder maintains persistent knowledge.

## Memory Location

```
factory/memory/
├── README.md         ← How memory works
├── agents-built.md   ← All agents created
└── lessons.md        ← Build lessons learned
```

## Memory Types

### Agents Built (Episodic)
Track every agent created.

**Purpose:**
- Reference past builds
- Track patterns that work
- Know what exists

**When to update:** After completing any agent build.

### Lessons Learned (Semantic)
Insights that improve future builds.

**Purpose:**
- Remember what works
- Avoid repeating mistakes
- Build institutional knowledge

**When to update:** When insight emerges from build experience.

## Memory Operations

| Event | Action |
|-------|--------|
| Agent created | Add to agents-built.md |
| Review completed | Update agent entry with score |
| Insight learned | Add to lessons.md |
