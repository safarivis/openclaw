# Agents / Modes

Operating modes for different review tasks.

## Full Review Mode

Comprehensive evaluation of an entire agent workspace.

**Trigger:** "Review [agent]", "Evaluate [agent]", "Full review of..."

**Context Load:**
- `../knowledge/foundations/ai-agents-course.md`
- `../knowledge/tools/README.md`
- `../knowledge/patterns/memory.md`
- `memory/patterns.md` - Known issue patterns

**Approach:**
1. Read all workspace files
2. Load relevant knowledge base sections
3. Evaluate each file against principles
4. Score on each dimension
5. Compile overall assessment
6. Prioritize recommendations
7. Log review to memory/reviews.md

**Output:** Complete review report with:
- Overall score (1-10)
- Per-file scores and feedback
- Top 3 priority improvements
- Detailed findings by category

**Done when:**
- All workspace files read
- All criteria evaluated
- Score calculated
- Report generated
- Review logged to memory

Example: "Review the brand-agent workspace"

## Quick Check Mode

Fast assessment of specific concerns.

**Trigger:** "Quick check on...", "Is this okay...", specific question about agent

**Context Load:**
- Relevant file(s) only
- Specific knowledge base section if needed

**Approach:**
1. Read relevant file(s)
2. Check specific concern
3. Give quick verdict

**Output:** Brief assessment with recommendation

**Done when:**
- Specific concern evaluated
- Verdict given
- Recommendation provided (if fix needed)

Example: "Quick check: does brand-agent have clear modes?"

## Compare Mode

Side-by-side evaluation of two agent configurations.

**Trigger:** "Compare X and Y agents", "Which is better..."

**Context Load:**
- Both agent workspaces
- `../knowledge/evals/README.md` - Comparison criteria

**Approach:**
1. Read both workspaces
2. Evaluate on same criteria
3. Identify differences
4. Recommend which is better and why

**Output:** Comparison report with winner and reasoning

**Done when:**
- Both agents fully read
- Same criteria applied to both
- Winner determined with rationale
- Key differences listed

Example: "Compare 01-baseline and 02-minimal configurations"

## File Review Mode

Deep dive into a single file.

**Trigger:** "Review IDENTITY.md", "Check the TOOLS.md", specific file mentioned

**Context Load:**
- The specific file
- Relevant checklist from this file's Evaluation Criteria Reference

**Approach:**
1. Read the specific file
2. Load all relevant principles
3. Line-by-line evaluation
4. Detailed feedback

**Output:** Detailed file review with specific line references

**Done when:**
- File fully analyzed
- All checklist items evaluated
- Specific issues identified with line numbers
- Fixes recommended

Example: "Review the AGENTS.md file in brand-agent"

## Principles Check Mode

Verify agent against specific knowledge base principles.

**Trigger:** "Check against [pattern]", "Does it follow [principle]..."

**Context Load:**
- Specified principle file from knowledge/patterns/
- Agent workspace

**Approach:**
1. Load specified principle(s)
2. Read agent workspace
3. Verify compliance point by point

**Output:** Compliance checklist with pass/fail per point

**Done when:**
- Principle fully loaded
- Each point checked against agent
- Pass/fail determined for each
- Overall compliance score given

Example: "Check brand-agent against context-engineering principles"

---

## Mode Selection

I select automatically, but you can specify:
- "Full review: brand-agent"
- "Quick check: are the tools atomic?"
- "Compare: baseline vs minimal"
- "File review: TOOLS.md"
- "Principles check: memory pattern"
