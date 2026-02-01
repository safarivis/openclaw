# Tools

Tools for brand building and management.

## Available Tools

These tools are available through the underlying platform.

### search_web
Search for market information and trends.

**When to use:** Competitive research, industry trends, audience insights
**Parameters:**
- query (string, required): Search terms
- date_range (enum, optional): "recent" | "past_year" | "any" (default: "any")

**Returns:** List of results with:
- title: Page title
- url: Source URL
- snippet: Relevant excerpt

**Tips:**
- Search for "[competitor] brand positioning"
- Look for industry reports and analysis
- Find customer sentiment and reviews

### read_url
Read content from websites.

**When to use:** Analyzing competitor sites, reading industry articles
**Parameters:**
- url (string, required): Full URL to read

**Returns:** Page content as markdown with:
- title: Page title
- content: Main text content
- metadata: Author, date if available

### search_documents
Search internal documents.

**When to use:** Finding existing brand guidelines, past campaigns, research
**Parameters:**
- query (string, required): Search terms
- path (string, optional): Directory to search in

**Returns:** List of matching files with:
- path: File location
- snippet: Matching excerpt
- score: Relevance score

### read_file
Read brand documents and guidelines.

**When to use:** Reviewing existing brand materials, loading memory
**Parameters:**
- path (string, required): Full file path

**Returns:** File contents as text

### write_file
Create or update brand documents.

**When to use:** Creating brand guides, strategy docs, saving to memory
**Parameters:**
- path (string, required): File location
- content (string, required): Document content

**Returns:** Confirmation with file path

---

## Memory Operations

Brand memory is stored in `./memory/`. Use read_file and write_file to access.

### Load Memory (Before Tasks)

| Mode | Files to Load |
|------|---------------|
| Strategy | `memory/brand-strategy.md`, `memory/competitors.md` |
| Voice | `memory/brand-strategy.md`, `memory/voice-guide.md` |
| Review | `memory/brand-strategy.md`, `memory/voice-guide.md` |
| Competitor | `memory/brand-strategy.md`, `memory/competitors.md` |
| Campaign | `memory/brand-strategy.md`, `memory/voice-guide.md`, `memory/competitors.md` |
| Audit | All memory files |

**Always load `memory/brand-strategy.md` first** - it contains core positioning.

### Save Memory (After Tasks)

| Output Type | Save To |
|-------------|---------|
| New/updated positioning | `memory/brand-strategy.md` |
| Voice guidelines | `memory/voice-guide.md` |
| Competitive analysis | `memory/competitors.md` |
| Significant decisions | `memory/decisions.md` (append) |
| Insights from failures | `memory/lessons.md` (append) |

**Example: Saving a Decision**
```markdown
## 2024-01-15 - [Decision Title]
**Context:** [Why this came up]
**Decision:** [What we decided]
**Rationale:** [Why]
**Alternatives:** [What else we considered]
**Impact:** [What this affects]
```

---

## Manual Analysis (No Dedicated Tool)

These tasks are performed through reasoning and the tools above.

### Sentiment Analysis
**How to do it:** Read the content, then analyze for:
- Overall tone (positive/negative/neutral)
- Emotional indicators
- Brand perception signals

### Brand Comparison
**How to do it:** Research each brand, then compare systematically.
1. `search_web` for "[brand] positioning" for each competitor
2. `read_url` their websites and key pages
3. Extract: positioning, voice, values, visual style
4. Create comparison table
5. **Save to** `memory/competitors.md`

### Voice Check
**How to do it:** Compare content against documented voice attributes.
1. `read_file memory/voice-guide.md`
2. Review content for: tone, word choice, sentence structure
3. Score alignment on each voice attribute
4. List specific misalignments with suggestions

### Alternative Suggestions
**How to do it:** Identify the issue, reference guidelines, rewrite.
1. Identify what's off-brand (tone, message, style)
2. Reference the relevant guideline from memory
3. Provide 2-3 alternative phrasings
4. Explain why each is more on-brand

---

## Tool Usage Guidelines

1. **Load memory first** - Check what's already defined before starting
2. **Research before recommending** - Use search_web and read_url for external context
3. **Save to memory** - Persist important outputs for future sessions
4. **Log decisions** - Append significant decisions to decisions.md
5. **Capture lessons** - When something fails or succeeds unexpectedly, log it

## Tool Count

- **5 available tools** (search_web, read_url, search_documents, read_file, write_file)
- **4 manual processes** (sentiment, comparison, voice check, alternatives)
- **5 memory files** (strategy, voice, decisions, competitors, lessons)

This follows the knowledge base principle: "Aim for 5-15 tools max" to avoid decision paralysis.
