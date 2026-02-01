# Knowledge Base

Info Agent's ingestion patterns and sources.

---

## Ingestion Workflow

1. Receive content (video, article, doc)
2. Extract key concepts
3. Compare against existing knowledge
4. Propose additions
5. Get user approval
6. Save to appropriate location

## Content Types

| Type | How to Process |
|------|----------------|
| YouTube video | Extract transcript, summarize concepts |
| Article | Extract key points, cite source |
| Documentation | Structure into patterns |
| Book summary | Extract frameworks |

## Quality Rules

- Always cite sources
- Never add without approval
- Check for duplicates first
- Summarize, don't copy verbatim

## Knowledge Locations

| Content Type | Where to Save |
|--------------|---------------|
| Agent patterns | knowledge/patterns/ |
| Tool design | knowledge/tools/ |
| Eval methods | knowledge/evals/ |
| Foundations | knowledge/foundations/ |

---

*Ingested content goes to clawd-lab/knowledge/*
