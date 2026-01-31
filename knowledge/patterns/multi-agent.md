# Multi-Agent Patterns

When one agent isn't enough, coordinate multiple agents.

## When to Use Multi-Agent

- Task requires different types of expertise
- Subtasks can run in parallel (speed matters)
- Single context window can't hold everything needed
- Want checks and balances (one agent reviews another)

## When NOT to Use Multi-Agent

- Single agent can handle it (simpler is better)
- Coordination overhead exceeds benefit
- Subtasks are tightly coupled (constant back-and-forth needed)

## Pattern 1: Sequential (Pipeline)

```
Agent A → output → Agent B → output → Agent C → final
```

Each agent specializes in one stage. Output of one becomes input to next.

### Example: Content Pipeline
```
Research Agent → facts → Writer Agent → draft → Editor Agent → final
```

### Implementation
```python
facts = research_agent.run(topic)
draft = writer_agent.run(facts)
final = editor_agent.run(draft)
```

### Best For
- Clear stages with distinct skills
- Each stage transforms the output
- No need for back-and-forth

### Watch Out For
- Error propagation (bad early output ruins everything)
- Lost context (later agents don't know why earlier choices were made)

## Pattern 2: Parallel (Fan-out/Fan-in)

```
        → Agent A →
Task ─→ → Agent B → → Combine → Result
        → Agent C →
```

Multiple agents work simultaneously, results are merged.

### Example: Research
```
Query → Search Agent (web) →
     → Search Agent (docs) → → Synthesize Agent → Report
     → Search Agent (code) →
```

### Implementation
```python
results = await asyncio.gather(
    web_agent.run(query),
    docs_agent.run(query),
    code_agent.run(query)
)
final = synthesize_agent.run(results)
```

### Best For
- Independent subtasks
- Speed is critical
- Multiple sources/perspectives needed

### Watch Out For
- Combining conflicting results
- Wasted work if one result is sufficient

## Pattern 3: Hierarchical (Manager/Workers)

```
Manager Agent
    ├── Worker A (research)
    ├── Worker B (writing)
    └── Worker C (coding)
```

Manager decomposes task, assigns to workers, integrates results.

### Example: Project Execution
```
Project Manager Agent
    ├── "Research competitor pricing" → Research Agent
    ├── "Draft pricing page copy" → Writer Agent
    └── "Build pricing component" → Coder Agent
```

### Implementation
```python
class ManagerAgent:
    def run(self, task):
        plan = self.decompose(task)
        results = {}
        for subtask in plan:
            worker = self.select_worker(subtask)
            results[subtask] = worker.run(subtask)
        return self.integrate(results)
```

### Best For
- Complex tasks needing coordination
- Mix of skill types
- Dynamic task decomposition

### Watch Out For
- Manager bottleneck
- Poor decomposition (workers get stuck)
- Context loss between manager and workers

## Pattern 4: Debate/Adversarial

```
Agent A (advocate) ←→ Agent B (critic) → Synthesis
```

Agents with opposing roles improve output through debate.

### Example: Decision Making
```
Proposal Agent: "We should use microservices"
Critic Agent: "Microservices add complexity. What about monolith?"
Proposal Agent: "Good point. Modular monolith might be better."
Judge Agent: "Modular monolith recommended for this team size."
```

### Implementation
```python
proposal = advocate.run(task)
for round in range(3):
    critique = critic.run(proposal)
    if critic.is_satisfied():
        break
    proposal = advocate.revise(proposal, critique)
final = judge.decide(proposal, critique)
```

### Best For
- Decisions with tradeoffs
- Need to explore multiple perspectives
- Catching errors and blind spots

### Watch Out For
- Endless debate (need termination condition)
- Artificial disagreement
- Overhead for simple decisions

## Pattern 5: Voting/Ensemble

```
Agent A → answer →
Agent B → answer → → Vote/Aggregate → Final
Agent C → answer →
```

Multiple agents solve same problem, combine answers.

### Example: Code Review
```
Security Agent → issues →
Performance Agent → issues → → Combine → Review Report
Maintainability Agent → issues →
```

### Best For
- High-stakes decisions
- Catching diverse types of issues
- When single agent is unreliable

### Watch Out For
- High cost (multiple runs)
- Combining conflicting assessments

## Coordination Strategies

### Shared Context
All agents see the same background information.

```python
shared_context = load_context()
for agent in agents:
    agent.set_context(shared_context)
```

### Message Passing
Agents communicate through structured messages.

```python
while not done:
    for agent in agents:
        message = agent.step(inbox)
        route_message(message, agents)
```

### Blackboard
Shared workspace all agents read/write.

```python
blackboard = {}
while not done:
    for agent in agents:
        updates = agent.contribute(blackboard)
        blackboard.update(updates)
```

## Common Mistakes

### Too Many Agents
Coordination overhead exceeds benefit.

**Fix:** Start with one agent. Add more only when you hit limits.

### Unclear Roles
Agents overlap or leave gaps.

**Fix:** Define clear responsibilities. Each agent has one job.

### Lost Context
Downstream agents miss important context.

**Fix:** Explicitly pass relevant context. Summarize if needed.

### No Error Handling
One agent fails, whole system fails.

**Fix:** Each agent reports errors. Manager handles failures gracefully.
