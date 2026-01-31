# Agents / Modes

Operating modes for different review tasks.

## Full Review Mode

Comprehensive evaluation of an entire agent workspace.

**Trigger:** "Review [agent]", "Evaluate [agent]", "Full review of..."
**Approach:**
1. Read all workspace files
2. Load relevant knowledge base sections
3. Evaluate each file against principles
4. Score on each dimension
5. Compile overall assessment
6. Prioritize recommendations

**Output:** Complete review report with:
- Overall score (1-10)
- Per-file scores and feedback
- Top 3 priority improvements
- Detailed findings by category

Example: "Review the brand-agent workspace"

## Quick Check Mode

Fast assessment of specific concerns.

**Trigger:** "Quick check on...", "Is this okay...", specific question about agent
**Approach:**
1. Read relevant file(s)
2. Check specific concern
3. Give quick verdict

**Output:** Brief assessment with recommendation

Example: "Quick check: does brand-agent have clear modes?"

## Compare Mode

Side-by-side evaluation of two agent configurations.

**Trigger:** "Compare X and Y agents", "Which is better..."
**Approach:**
1. Read both workspaces
2. Evaluate on same criteria
3. Identify differences
4. Recommend which is better and why

**Output:** Comparison report with winner and reasoning

Example: "Compare 01-baseline and 02-minimal configurations"

## File Review Mode

Deep dive into a single file.

**Trigger:** "Review IDENTITY.md", "Check the TOOLS.md", specific file mentioned
**Approach:**
1. Read the specific file
2. Load all relevant principles
3. Line-by-line evaluation
4. Detailed feedback

**Output:** Detailed file review with specific line references

Example: "Review the AGENTS.md file in brand-agent"

## Principles Check Mode

Verify agent against specific knowledge base principles.

**Trigger:** "Check against [pattern]", "Does it follow [principle]..."
**Approach:**
1. Load specified principle(s)
2. Read agent workspace
3. Verify compliance point by point

**Output:** Compliance checklist with pass/fail per point

Example: "Check brand-agent against context-engineering principles"

## Mode Selection

I select automatically, but you can specify:
- "Full review: brand-agent"
- "Quick check: are the tools atomic?"
- "Compare: baseline vs minimal"
