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

**Output:** Draft WHY.md including:
- Problem statement
- Target users
- Success criteria
- Constraints
- Recommended blueprint

**Done when:**
- WHY.md draft is complete
- Blueprint is selected
- User approves WHY.md

Example: "I need something to help with customer emails"

## Design Mode

For planning an agent architecture.

**Trigger:** Clear requirements, ready to design, "Design an agent for..."

**Prerequisite:** WHY.md should exist (from Discovery Mode or provided by user)

**Context Load:**
- `WHY.md` - Approved intent document
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
- `../blueprints/WHY.md` - Intent template

**Approach:**
1. **Create WHY.md FIRST** - Capture intent before building
   - Copy from `../blueprints/WHY.md`
   - Fill in: Problem, Users, Success Criteria, Constraints
   - Get user approval on WHY.md before proceeding
2. Create workspace directory (`../agents/[agent-name]/`)
3. Copy blueprint files as base
4. Customize IDENTITY.md with specific mission
5. Create SOUL.md with domain values
6. Write AGENTS.md with modes + "Done when:" conditions
7. Define TOOLS.md with typed parameters/returns
8. Create KNOWLEDGE.md from template (flat, no folder)
9. Document in NOTES.md
10. Register in `~/.openclaw/openclaw.json`
11. **Hand off to Agent Reviewer for evaluation**

**STOP GATE:** Do not proceed past step 1 without an approved WHY.md. This prevents drift by capturing intent upfront.

**Output:**
- WHY.md with captured intent (approved)
- Complete agent workspace with all files
- Registered in openclaw.json
- Ready for Agent Reviewer evaluation

**Done when:**
- WHY.md exists and is approved
- All workspace files created (WHY, IDENTITY, SOUL, AGENTS, TOOLS, KNOWLEDGE, NOTES)
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
