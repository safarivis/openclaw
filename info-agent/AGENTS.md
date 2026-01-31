# Agents / Modes

Operating modes for knowledge ingestion.

## Ingest Mode

For extracting knowledge from a content source.

**Trigger:** YouTube URL, article URL, "ingest this", "extract from"

**Approach:**
1. Get transcript/content from source
2. Identify the source creator and context
3. Extract key concepts, principles, frameworks
4. Structure into digestible format
5. Prepare for comparison

**Output:** Extracted knowledge summary with:
- Source info (creator, title, date)
- Key concepts (numbered list)
- Actionable principles
- Notable quotes

**Done when:**
- Content is fully transcribed/read
- Key concepts are extracted and structured
- Ready for comparison against existing knowledge

**Example:** "Ingest this YouTube video: [URL]"

---

## Compare Mode

For comparing extracted knowledge against existing knowledge base.

**Trigger:** "Compare to knowledge base", "what's new", "do we have this"

**Approach:**
1. Load relevant existing knowledge files
2. Map extracted concepts to existing concepts
3. Identify: new, redundant, conflicting, complementary
4. Assess value-add for each new concept
5. Generate comparison report

**Output:** Comparison report with:
- ✅ **New & Valuable** - Not in knowledge base, worth adding
- ⚠️ **Conflicts** - Contradicts existing knowledge
- 🔄 **Complementary** - Adds to existing concepts
- ❌ **Redundant** - Already covered

**Done when:**
- All concepts are mapped to existing knowledge
- Value assessment is complete for each
- Report is ready for human review

**Example:** "Compare this against our patterns knowledge"

---

## Advise Mode

For recommending what to add and where.

**Trigger:** "Should we add this", "what do you recommend", "advise"

**Approach:**
1. Review comparison results
2. Prioritize by impact on agent effectiveness
3. Identify target location (global vs agent-specific)
4. Draft recommendation with rationale
5. Present options for human decision

**Output:** Recommendation with:
- What to add (specific content)
- Where to add (file path)
- Why add it (impact on agents)
- Why NOT add it (if applicable)
- Human decision prompt

**Done when:**
- Clear recommendation is provided
- Rationale is explained
- Human has been asked for approval
- NO changes made without approval

**Example:** "Should we add Chris Do's pricing framework to Brand Agent?"

---

## Learn Mode

For teaching specific agents from a content creator.

**Trigger:** "Teach [agent] from [creator]", "Brand Agent learn from Chris Do"

**Approach:**
1. Ingest all specified content from creator
2. Extract principles relevant to target agent
3. Compare against agent's existing knowledge/memory
4. Create mentor file for the agent
5. Ask approval before adding

**Output:** Mentor file ready for agent memory:
```
[agent]/memory/mentors/[creator].md
```

**Done when:**
- Creator's relevant knowledge is extracted
- Mentor file is drafted
- Human has approved the addition
- File is saved to agent's memory (after approval)

**Example:** "Teach Brand Agent everything from Chris Do"

---

## Audit Mode

For reviewing what knowledge we've added and from where.

**Trigger:** "What have we learned", "knowledge audit", "show sources"

**Approach:**
1. Scan knowledge base and agent memories
2. List all sources and attributions
3. Identify gaps or outdated content
4. Suggest refresh or additions

**Output:** Knowledge audit report

**Done when:**
- All sources are catalogued
- Gaps are identified
- Recommendations are provided

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
