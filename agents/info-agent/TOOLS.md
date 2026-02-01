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
```yaml
type: object
properties:
  title: string - Video title
  channel: string - Creator/channel name
  duration: string - Video length (e.g., "45:23")
  transcript: string - Full text with timestamps
  description: string - Video description
  url: string - Original URL for attribution
```

**How it works:**
1. Extract video ID from URL
2. Fetch available transcripts (auto-generated or manual)
3. Return structured transcript

**Note:** Uses youtube-transcript-api or yt-dlp.

### read_url
Read content from web pages.

**When to use:** Ingesting articles, blog posts, documentation
**Parameters:**
- url (string, required): Page URL

**Returns:**
```yaml
type: object
properties:
  title: string - Page title
  content: string - Page content as markdown
  author: string | null - Author if available
  date: string | null - Publish date if available
  url: string - Original URL for attribution
```

### read_file
Read local files.

**When to use:** Loading existing knowledge, agent memories, memory files
**Parameters:**
- path (string, required): File path

**Returns:**
```yaml
type: object
properties:
  content: string - File contents
  path: string - File path
  exists: boolean - Whether file existed
```

### write_file
Save content to files.

**When to use:** Saving extracted knowledge (after approval), updating memory
**Parameters:**
- path (string, required): File path
- content (string, required): Content to save

**Returns:**
```yaml
type: object
properties:
  success: boolean
  path: string - Written file path
  message: string - Confirmation or error
```

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

**When to use:** Finding related existing knowledge, checking for duplicates
**Parameters:**
- query (string, required): Search terms
- path (string, optional): Limit to specific directory (e.g., "knowledge/patterns/")

**Returns:**
```yaml
type: object
properties:
  matches: array
    items:
      - file: string - File path
      - excerpt: string - Matching content
      - relevance: number - 0-1 relevance score
  count: integer - Number of matches
```

---

## Memory Operations

### load_memory
Load memory files at session start.

**When to use:** Beginning of any session or mode
**Files to load:**
- `memory/sources.md` - Check what's already ingested
- `memory/decisions.md` - Recent decision context
- `memory/lessons.md` - Apply learned patterns

### check_source
Check if content has already been ingested.

**When to use:** Before ingesting any new content
**Process:**
1. Search `memory/sources.md` for URL
2. If found: Report "Already ingested on [date]" with summary
3. If not found: Proceed with ingestion

### log_source
Add new source to memory after ingestion.

**When to use:** After completing content ingestion
**Template:**
```markdown
## [Date] - [Title]
- **Source:** [Creator]
- **URL:** [link]
- **Type:** YouTube | Article | Podcast
- **Status:** Ingested
- **Concepts Extracted:** [count]
- **Notes:** [brief summary]
```

### log_decision
Record approval/rejection decision.

**When to use:** After human makes any knowledge decision
**Template:**
```markdown
## [Date] - [Decision Title]
- **Source:** [Content source]
- **Proposed:** [What was proposed]
- **Location:** [Target path]
- **Decision:** Approved | Rejected | Modified
- **Rationale:** [Why]
- **Implemented:** Yes | No
```

### log_lesson
Record insight for future reference.

**When to use:** When pattern or insight emerges
**Template:**
```markdown
## Lesson: [Title]
- **Date:** [When learned]
- **Context:** [Situation]
- **Lesson:** [What to remember]
- **Applies to:** [Future situations]
```

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
