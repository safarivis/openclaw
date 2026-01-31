# Agents / Modes

Operating modes for different agent building tasks.

## Discovery Mode

For understanding what agent to build.

**Trigger:** New project, unclear requirements, "I need an agent that..."
**Approach:**
- Ask clarifying questions
- Explore the problem space
- Identify success criteria
- Match to existing patterns

**Output:** Clear agent specification including:
- Purpose and goals
- Target users
- Key capabilities needed
- Success metrics

Example: "I need something to help with customer emails"

## Design Mode

For planning an agent architecture.

**Trigger:** Clear requirements, ready to design, "Design an agent for..."
**Approach:**
- Review relevant knowledge (`../knowledge/`)
- Select closest blueprint (`../blueprints/`)
- Plan customizations
- Design tool set
- Define evaluation criteria

**Output:** Agent design document with:
- Blueprint choice and rationale
- Customizations planned
- Tool specifications
- Context engineering plan
- Eval approach

Example: "Design a research agent for competitive analysis"

## Build Mode

For creating the actual agent workspace.

**Trigger:** Approved design, "Build the agent", "Create workspace"
**Approach:**
- Create workspace directory
- Generate IDENTITY.md from design
- Create SOUL.md with values
- Write AGENTS.md with modes
- Define TOOLS.md
- Document in NOTES.md

**Output:** Complete agent workspace ready to register and test

Example: "Build the competitive research agent we designed"

## Improve Mode

For iterating on existing agents.

**Trigger:** Agent feedback, test results, "Improve...", "Fix..."
**Approach:**
- Review current agent configuration
- Analyze failures or feedback
- Identify knowledge/patterns that apply
- Plan targeted improvements
- Update agent files
- Add to lessons learned if novel

**Output:** Updated agent with documented changes

Example: "The research agent is missing important sources"

## Evaluate Mode

For assessing agent performance.

**Trigger:** "Test...", "Evaluate...", "How is X performing?"
**Approach:**
- Review eval criteria
- Run test cases
- Analyze results
- Identify failure patterns
- Recommend improvements

**Output:** Evaluation report with:
- Test results
- Pass/fail rates
- Failure analysis
- Improvement recommendations

Example: "Evaluate the writer agent against the test cases"

## Compare Mode

For comparing agent variants.

**Trigger:** Multiple versions, "Compare X and Y", A/B testing
**Approach:**
- Identify comparison criteria
- Run same inputs through variants
- Analyze differences
- Determine winner (if applicable)

**Output:** Comparison report with:
- Side-by-side results
- Strengths/weaknesses
- Recommendation

Example: "Compare baseline vs minimal agent configurations"
