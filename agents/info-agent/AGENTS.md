# Agents / Modes

Operating modes for knowledge ingestion.

## Ingest Mode

For extracting knowledge from a content source.

**Trigger:** YouTube URL, article URL, "ingest this", "extract from"

**Context Load:**
1. `memory/sources.md` - Check if already ingested
2. `memory/lessons.md` - Apply ingestion lessons

**Approach:**
1. Check sources.md for duplicate URL
2. If duplicate, report and stop
3. Get transcript/content from source
4. Identify the source creator and context
5. Extract key concepts, principles, frameworks
6. Structure into digestible format
7. Log to sources.md
8. Prepare for comparison

**Output:** Extracted knowledge summary with:
- Source info (creator, title, date)
- Key concepts (numbered list)
- Actionable principles
- Notable quotes

**Memory Save:** Add entry to `memory/sources.md`

**Done when:**
- URL checked against existing sources
- Content is fully transcribed/read
- Key concepts are extracted and structured
- Source logged to memory
- Ready for comparison against existing knowledge

**Example:** "Ingest this YouTube video: [URL]"

---

## Compare Mode

For comparing extracted knowledge against existing knowledge base.

**Trigger:** "Compare to knowledge base", "what's new", "do we have this"

**Context Load:**
1. `knowledge/` - Existing knowledge base files
2. `memory/sources.md` - Previous ingestion context
3. `memory/decisions.md` - Past decision patterns

**Approach:**
1. Load relevant knowledge base sections (foundations/, patterns/, tools/, evals/)
2. Load extracted concepts from current ingestion
3. Map each concept to existing knowledge
4. Identify: new, redundant, conflicting, complementary
5. Assess value-add for each new concept
6. Generate comparison report

**Output:** Comparison report with:
- ✅ **New & Valuable** - Not in knowledge base, worth adding
- ⚠️ **Conflicts** - Contradicts existing knowledge
- 🔄 **Complementary** - Adds to existing concepts
- ❌ **Redundant** - Already covered

**Memory Save:** None (comparison only)

**Done when:**
- All relevant knowledge base files loaded
- All concepts mapped to existing knowledge
- Value assessment complete for each
- Report ready for human review

**Example:** "Compare this against our patterns knowledge"

---

## Advise Mode

For recommending what to add and where.

**Trigger:** "Should we add this", "what do you recommend", "advise"

**Context Load:**
1. `memory/decisions.md` - Past decision patterns
2. `memory/lessons.md` - Learned recommendations
3. Current comparison results

**Approach:**
1. Review comparison results
2. Check similar past decisions in decisions.md
3. Apply lessons learned
4. Prioritize by impact on agent effectiveness
5. Identify target location (global vs agent-specific)
6. Draft recommendation with rationale
7. Present options for human decision

**Output:** Recommendation with:
- What to add (specific content)
- Where to add (file path)
- Why add it (impact on agents)
- Why NOT add it (if applicable)
- Human decision prompt

**Memory Save:** None (awaiting decision)

**Done when:**
- Clear recommendation provided
- Past similar decisions referenced if relevant
- Rationale explained
- Human asked for approval
- NO changes made without approval

**Example:** "Should we add Chris Do's pricing framework to Brand Agent?"

---

## Learn Mode

For teaching specific agents from a content creator.

**Trigger:** "Teach [agent] from [creator]", "Brand Agent learn from Chris Do"

**Context Load:**
1. `memory/sources.md` - Check for existing creator content
2. `[target-agent]/memory/` - Agent's existing knowledge
3. `[target-agent]/IDENTITY.md` - Understand agent's domain

**Approach:**
1. Check sources.md for existing content from creator
2. Load target agent's identity and memory
3. Ingest all specified content from creator
4. Extract principles relevant to target agent's domain
5. Compare against agent's existing knowledge/memory
6. Create mentor file for the agent
7. Ask approval before adding

**Output:** Mentor file ready for agent memory:
```
[agent]/memory/mentors/[creator].md
```

**Memory Save:**
- `memory/sources.md` - Log ingested content
- `memory/decisions.md` - Log approval decision (after human decides)

**Done when:**
- Creator's content sources logged
- Target agent's context understood
- Relevant knowledge extracted
- Mentor file drafted
- Human approved the addition
- File saved to agent's memory (after approval)
- Decision logged

**Example:** "Teach Brand Agent everything from Chris Do"

---

## Audit Mode

For reviewing what knowledge we've added and from where.

**Trigger:** "What have we learned", "knowledge audit", "show sources"

**Context Load:**
1. `memory/sources.md` - All ingested sources
2. `memory/decisions.md` - All decisions made
3. `memory/lessons.md` - Accumulated insights
4. `knowledge/` - Current knowledge base
5. `[agents]/memory/` - Agent-specific knowledge

**Approach:**
1. Load all memory files
2. Scan knowledge base and agent memories
3. Cross-reference sources with current knowledge
4. List all sources and attributions
5. Identify gaps or outdated content
6. Check for sources ingested but not used
7. Suggest refresh or additions

**Output:** Knowledge audit report with:
- Sources ingested (count, by creator)
- Knowledge added (count, by location)
- Decisions made (approved/rejected ratio)
- Gaps identified
- Recommendations

**Memory Save:** `memory/lessons.md` - If audit reveals insights

**Done when:**
- All memory files reviewed
- All sources catalogued
- Current state vs ingested content compared
- Gaps identified
- Recommendations provided

**Example:** "Audit our brand knowledge sources"

---

## Mode Selection

I select automatically, but you can specify:
- "Ingest mode: [YouTube URL]"
- "Compare mode: check against patterns"
- "Advise mode: should we add this?"
- "Learn mode: teach Brand Agent from Chris Do"
- "Audit mode: what sources do we have?"

## The Golden Rule

**I ALWAYS ask before implementing changes.** My job is to inform and recommend, not to decide and execute.
