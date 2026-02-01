# Agents / Modes

Operating modes for different agent building tasks.

## Discovery Mode

For understanding what agent to build.

**Trigger:** New project, unclear requirements, "I need an agent that..."

**Context Load:**
- `../blueprints/README.md` - Available agent types
- `../knowledge/foundations/ai-agents-course.md` - Core concepts

**Approach:**
- Ask clarifying questions
- Explore the problem space
- Identify success criteria
- Match to existing patterns/blueprints

**Output:** Clear agent specification including:
- Purpose and goals
- Target users
- Key capabilities needed
- Success metrics
- Recommended blueprint

**Done when:**
- Requirements are clear
- Blueprint is selected
- User approves specification

Example: "I need something to help with customer emails"

## Design Mode

For planning an agent architecture.

**Trigger:** Clear requirements, ready to design, "Design an agent for..."

**Context Load:**
- `../knowledge/foundations/ai-agents-course.md` - Core concepts
- `../knowledge/patterns/` - Relevant patterns
- `../knowledge/tools/README.md` - Tool design principles
- `../blueprints/[selected]/` - Blueprint to customize

**Approach:**
- Review relevant knowledge patterns
- Load selected blueprint
- Plan customizations for specific use case
- Design tool set with typed parameters
- Plan memory system
- Define evaluation criteria

**Output:** Agent design document with:
- Blueprint choice and rationale
- Customizations planned
- Tool specifications (typed)
- Memory system design
- Context engineering plan
- Eval approach

**Done when:**
- Design document complete
- All patterns considered
- User approves design

Example: "Design a research agent for competitive analysis"

## Build Mode

For creating the actual agent workspace.

**Trigger:** Approved design, "Build the agent", "Create workspace", "Build me an agent"

**Context Load:**
- `../knowledge/foundations/ai-agents-course.md` - Agent checklist
- `../knowledge/patterns/memory.md` - Memory implementation
- `../knowledge/tools/README.md` - Tool design
- `../blueprints/[selected]/` - Base template

**Approach:**
1. Create workspace directory (`../[agent-name]/`)
2. Copy blueprint files as base
3. Customize IDENTITY.md with specific mission
4. Create SOUL.md with domain values
5. Write AGENTS.md with modes + "Done when:" conditions
6. Define TOOLS.md with typed parameters/returns
7. Create MEMORY.md + memory/ directory
8. Document in NOTES.md
9. Register in `~/.openclaw/openclaw.json`
10. **Hand off to Agent Reviewer for evaluation**

**Output:**
- Complete agent workspace with all files
- Registered in openclaw.json
- Ready for Agent Reviewer evaluation

**Done when:**
- All workspace files created (IDENTITY, SOUL, AGENTS, TOOLS, NOTES, MEMORY)
- Memory directory exists with templates
- Agent registered in openclaw.json
- **Agent Reviewer has been invoked**

Example: "Build the competitive research agent we designed"

## Improve Mode

For iterating on existing agents.

**Trigger:** Agent feedback, test results, "Improve...", "Fix...", Agent Reviewer report

**Context Load:**
- `../[agent]/` - Current agent workspace
- `../knowledge/` - Relevant patterns for fixes
- Agent Reviewer report (if available)

**Approach:**
- Review current agent configuration
- Analyze failures or feedback
- Identify knowledge/patterns that apply
- Plan targeted improvements
- Update agent files
- Add to lessons learned if novel
- Re-run Agent Reviewer if significant changes

**Output:** Updated agent with documented changes in NOTES.md

**Done when:**
- All identified issues fixed
- Changes documented in NOTES.md changelog
- Agent Reviewer score >= 8.5/10 (if re-evaluated)

Example: "The research agent is missing important sources"

## Evaluate Mode

For assessing agent performance.

**Trigger:** "Test...", "Evaluate...", "How is X performing?"

**Note:** For structure/quality evaluation, use **Agent Reviewer** instead. This mode is for runtime/behavioral testing.

**Context Load:**
- `../[agent]/` - Agent workspace
- `../knowledge/evals/README.md` - Eval methods

**Approach:**
- Review eval criteria from NOTES.md
- Run test cases
- Analyze results
- Identify failure patterns
- Recommend improvements

**Output:** Evaluation report with:
- Test results
- Pass/fail rates
- Failure analysis
- Improvement recommendations

**Done when:**
- All test cases run
- Failures analyzed
- Recommendations documented

Example: "Evaluate the writer agent against the test cases"

## Compare Mode

For comparing agent variants.

**Trigger:** Multiple versions, "Compare X and Y", A/B testing

**Context Load:**
- Both agent workspaces
- `../knowledge/evals/README.md` - Comparison criteria

**Approach:**
- Identify comparison criteria
- Run same inputs through variants
- Analyze differences
- Determine winner (if applicable)

**Output:** Comparison report with:
- Side-by-side results
- Strengths/weaknesses
- Recommendation

**Done when:**
- Both agents evaluated on same criteria
- Winner identified with rationale

Example: "Compare baseline vs minimal agent configurations"

---

## Mode Selection

I select automatically based on trigger words, but you can specify:
- "Discovery mode: I need an agent for X"
- "Design mode: plan the architecture"
- "Build mode: create the workspace"
- "Improve mode: fix these issues"
- "Evaluate mode: run the tests"
- "Compare mode: which is better"

## The Golden Rule

**After building ANY agent, I hand off to Agent Reviewer.** An agent isn't complete until it scores >= 8.5/10.
