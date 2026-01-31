# Tools

Tools for knowledge ingestion and management.

## Content Ingestion

### get_youtube_transcript
Get transcript from a YouTube video.

**When to use:** Ingesting knowledge from YouTube videos
**Parameters:**
- url (string, required): YouTube video URL
- language (string, optional): Preferred language (default: "en")

**Returns:**
- title: Video title
- channel: Creator name
- duration: Video length
- transcript: Full text with timestamps
- description: Video description

**How it works:**
1. Extract video ID from URL
2. Fetch available transcripts (auto-generated or manual)
3. Return structured transcript

**Note:** Uses youtube-transcript-api or similar service.

### read_url
Read content from web pages.

**When to use:** Ingesting articles, blog posts, documentation
**Parameters:**
- url (string, required): Page URL

**Returns:** Page content as markdown

### read_file
Read local files.

**When to use:** Loading existing knowledge, agent memories
**Parameters:**
- path (string, required): File path

**Returns:** File contents

### write_file
Save content to files.

**When to use:** Saving extracted knowledge (after approval)
**Parameters:**
- path (string, required): File path
- content (string, required): Content to save

**Returns:** Confirmation

---

## Knowledge Base Access

### Knowledge Base Locations
```
Global Knowledge:
- knowledge/foundations/     ← Core concepts
- knowledge/patterns/        ← Design patterns
- knowledge/tools/           ← Tool design
- knowledge/evals/           ← Evaluation methods

Agent-Specific:
- [agent]/memory/            ← Agent's memory
- [agent]/memory/mentors/    ← Thought leader knowledge
```

### search_knowledge
Search existing knowledge base.

**When to use:** Finding related existing knowledge
**Parameters:**
- query (string, required): Search terms
- path (string, optional): Limit to specific directory

**Returns:** Matching files and excerpts

---

## Extraction (Manual Process)

### Extract Concepts
From transcript/content, identify:

1. **Core Principles** - Fundamental truths or rules
2. **Frameworks** - Structured approaches to problems
3. **Patterns** - Repeatable solutions
4. **Anti-Patterns** - What to avoid
5. **Quotes** - Memorable statements worth preserving

**Format for extracted concepts:**
```markdown
## [Concept Name]
**Source:** [Creator] - [Title] ([URL])
**Principle:** [One sentence summary]
**Details:** [Expanded explanation]
**Apply when:** [Situations where this applies]
**Example:** [Concrete example if given]
```

---

## Comparison (Manual Process)

### Compare Against Existing

For each extracted concept, check:

| Status | Meaning | Action |
|--------|---------|--------|
| ✅ New & Valuable | Not in KB, adds value | Recommend adding |
| 🔄 Complementary | Extends existing | Recommend merging |
| ⚠️ Conflicts | Contradicts existing | Flag for review |
| ❌ Redundant | Already covered | Skip |
| 🤔 Unclear | Needs more context | Ask for clarification |

---

## Output Templates

### Comparison Report Template
```markdown
# Knowledge Comparison Report

**Source:** [Creator] - [Title]
**URL:** [link]
**Date Analyzed:** [date]

## Summary
- Total concepts extracted: X
- New & valuable: X
- Complementary: X
- Conflicts: X
- Redundant: X

## Detailed Findings

### ✅ New & Valuable

#### 1. [Concept Name]
**What:** [Description]
**Why add:** [Impact on agents]
**Where:** [Suggested location]

### ⚠️ Conflicts

#### 1. [Concept Name]
**New says:** [New content]
**Existing says:** [Current knowledge]
**Recommendation:** [How to resolve]

### ❌ Redundant (No Action Needed)
- [Concept] - covered in [file]

## Recommendation
[Overall recommendation with rationale]

## Awaiting Approval
- [ ] Add [concept] to [location]
- [ ] Merge [concept] into [existing file]
- [ ] Review conflict: [concept]
```

### Mentor File Template
```markdown
# [Creator Name] - Mentor Knowledge

**Source:** [Creator name and credentials]
**Content:** [List of videos/articles ingested]
**Last Updated:** [date]

## Core Philosophy
[Creator's fundamental approach/worldview]

## Key Principles

### 1. [Principle Name]
**Principle:** [One sentence]
**Details:** [Explanation]
**Apply when:** [Situations]
**Quote:** "[Direct quote if available]"

## Frameworks

### [Framework Name]
[Description and how to apply]

## Anti-Patterns
What [Creator] says to avoid:
- [Thing to avoid] - [Why]

## Memorable Quotes
- "[Quote]" - on [topic]
```

---

## Tool Usage Guidelines

1. **Ingest fully before comparing** - Get all content first
2. **Search before adding** - Always check existing knowledge
3. **Ask before writing** - Never save without approval
4. **Attribute everything** - Source every piece of knowledge
5. **Keep it actionable** - Skip vague or theoretical content
