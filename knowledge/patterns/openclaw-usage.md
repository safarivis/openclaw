# OpenClaw Usage Patterns

Power user patterns for getting the most out of OpenClaw agents.

---

## 1. Proactive Agent Configuration

**Problem:** Agents wait for tasks instead of working autonomously.

**Pattern:** Configure agents to work proactively, even overnight.

**How:**
- Set explicit expectations: "Work on X while I sleep"
- Define what "done" looks like
- Ask agent to surface surprises/findings in the morning

**Example prompt:**
```
Tonight while I'm away, review the codebase and:
1. Identify any security issues
2. List potential refactoring opportunities
3. Prepare a summary for me in the morning

Work autonomously. Don't wait for my input.
```

**Key insight:** Treat the agent as an employee who can work independently, not just a tool that responds to commands.

---

## 2. Expectation Setting

**Problem:** Agents don't know how you want to work together.

**Pattern:** Explicitly define the working relationship upfront.

**How:**
- Describe your working style preferences
- Set quality expectations
- Define when agent should ask vs proceed
- Specify proactivity level

**Example prompt:**
```
Working relationship expectations:
- Be proactive - don't wait for me to ask
- If something takes <5 min, just do it
- For bigger decisions, check with me first
- Challenge my ideas if you see issues
- Keep me updated on progress without being asked
```

**Key insight:** The agent can't read your mind. Explicit expectations lead to better collaboration.

---

## 3. Reverse Prompting

**Problem:** You don't always know what to ask the agent to do.

**Pattern:** Have the agent generate its own tasks based on context.

**How:**
- Share context about your goals/projects
- Ask agent what it should be doing
- Let agent identify gaps and opportunities

**Example prompts:**
```
Based on everything you know about me and my projects:
- What tasks should you be working on?
- What information am I missing that you need?
- What opportunities am I not seeing?
```

```
You have full context on my codebase.
What would you do if you were me?
What should I be worried about?
```

**Key insight:** The agent often has better visibility into what needs doing than you do.

---

## 4. Memory Flush (Pre-Compaction)

**Problem:** Important context gets lost during memory compaction/summarization.

**Pattern:** Explicitly save critical information before compaction occurs.

**How:**
- Recognize when conversation is getting long
- Proactively save important decisions, context, learnings
- Use structured format for easy retrieval

**Example prompt:**
```
Before this conversation compacts, save the following to memory:
- Decision: We chose React over Vue because...
- Key finding: The API has a 100 req/min limit
- Action item: Need to update the auth flow by Friday
```

**When to use:**
- After important decisions
- When you've established valuable context
- Before ending a long session

**Key insight:** Don't rely on automatic summarization to preserve what matters.

---

## 5. Brain + Muscles Model Selection

**Problem:** One model doesn't excel at everything.

**Pattern:** Use different models for different task types.

**Mental model:**
- **Brain (Orchestrator):** Opus/Claude - reasoning, planning, coordination
- **Muscles (Specialists):**
  - Coding model (Codex/Claude) - implementation
  - Search model (Gemini/Perplexity) - web research
  - Social model (Grok) - social media context
  - Fast model (Haiku) - quick tasks

**How:**
- Use the orchestrator for planning and decision-making
- Delegate specialized tasks to appropriate models
- Let the brain coordinate the muscles

**Example:**
```
Use Opus to:
- Plan the architecture
- Review the approach
- Make decisions

Delegate to specialists:
- Codex: Write the implementation
- Gemini: Research best practices
- Haiku: Format and clean up docs
```

**Key insight:** Match the model to the task for better results and efficiency.

---

## 6. Brain Dumping

**Problem:** Agent lacks context about you and your work.

**Pattern:** Share comprehensive personal/project context upfront.

**What to share:**
- Current projects and priorities
- Goals (short and long term)
- Preferences and working style
- Key relationships and stakeholders
- Constraints and deadlines
- Past decisions and their rationale

**Example:**
```
Context dump:
- I'm building a SaaS for X
- Launch deadline: March 15
- Team: Just me + 2 contractors
- Tech stack: Next.js, Supabase
- Current blocker: Auth flow is broken
- Priority: Get MVP working, polish later
- Style: I prefer simple over clever
```

**Key insight:** The more context the agent has, the better its suggestions and work product.

---

## 7. Agent-Built Tooling

**Problem:** You need custom tools but don't want to build them.

**Pattern:** Have the agent create its own tools.

**Examples:**
- Kanban/task boards
- Document viewers
- Simple CRMs
- Data dashboards
- Automation scripts

**How:**
```
I need a way to track my tasks visually.
Build me a simple Kanban board that:
- Has columns: Todo, In Progress, Done
- Saves to a local JSON file
- Can be viewed in the browser
```

**Key insight:** The agent can build tools tailored to your exact needs faster than finding existing solutions.

---

## Summary

| Pattern | One-liner |
|---------|-----------|
| Proactive Agents | Configure agents to work without waiting |
| Expectation Setting | Define the working relationship explicitly |
| Reverse Prompting | Ask agent what it should be doing |
| Memory Flush | Save important context before compaction |
| Brain + Muscles | Use specialized models for different tasks |
| Brain Dumping | Share comprehensive context upfront |
| Agent-Built Tooling | Have agent create custom tools |

---

## Source

Patterns extracted from: "5 Tips to Make ClaudeBot 100x More Powerful"
Video: https://youtu.be/UTCi_q6iuCM
