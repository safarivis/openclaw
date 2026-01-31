# AI Agents Course - Core Concepts

Distilled wisdom from the AI Agents course. This is the foundational knowledge for building effective agents.

## What is an AI Agent?

An AI agent is an LLM that can take actions in a loop until a task is complete.

**Key distinction:**
- **Workflow** = Fixed sequence of LLM calls (deterministic)
- **Agent** = LLM decides what to do next (autonomous)

Agents use tools to interact with the world: read files, search the web, execute code, call APIs.

## The ReAct Loop

The fundamental agent pattern: **Reason → Act → Observe → Loop**

```
1. REASON: "I need to find the user's email. Let me search the database."
2. ACT: Call search_database(query="user email")
3. OBSERVE: Got result: "user@example.com"
4. REASON: "Now I have the email. Task complete."
5. STOP: Return result to user
```

**Critical insight:** The LLM sees its previous reasoning. This "thinking out loud" helps it make better decisions.

### When to Stop

Agents need clear stopping conditions:
- Task explicitly complete
- Maximum iterations reached
- Error threshold exceeded
- User intervention requested

Without clear stops, agents can loop forever or take destructive actions.

## Task Decomposition

LLMs work best on focused tasks. Break complex work into LLM-sized pieces.

**Bad:** "Build me a complete e-commerce website"
**Good:** "Create the product listing component that displays title, price, and image"

### Decomposition Strategies

1. **Sequential** - Do A, then B, then C
2. **Parallel** - Do A, B, C simultaneously, combine results
3. **Hierarchical** - Manager assigns subtasks to workers

### The Planning Problem

Agents can plan, but plans often need revision. Two approaches:

1. **Plan-then-execute** - Create full plan, then run it
2. **Incremental planning** - Plan next step based on current state

Incremental is usually better for complex tasks (reality rarely matches the plan).

## Context Engineering

**The most important skill in agent building.**

Context = everything the LLM sees when making a decision:
- System prompt
- Conversation history
- Tool results
- Retrieved documents
- Current state

### Context Principles

1. **Less is more** - Don't dump everything in. Curate ruthlessly.
2. **Relevance matters** - Only include what's needed for THIS decision
3. **Structure helps** - Use clear formatting, headers, separators
4. **Recency bias** - Put important info near the end (closer to the question)

### Managing Long Contexts

- **Summarization** - Compress history periodically
- **RAG** - Retrieve only relevant documents
- **Sliding window** - Keep recent + key moments
- **External memory** - Store facts outside the context

## Tool Design

Tools are how agents act on the world. Design them for LLMs, not humans.

### Tool Anatomy

```
Name: search_database
Description: Search the customer database by name, email, or ID
Parameters:
  - query (string): Search term
  - field (enum): "name" | "email" | "id"
Returns: List of matching customer records
```

### Design Principles

1. **Clear names** - `search_customers` not `sc` or `query_db_v2`
2. **Specific descriptions** - What it does, when to use it, what it returns
3. **Typed parameters** - Enums over free text when possible
4. **Atomic operations** - One tool = one action
5. **Idempotent preferred** - Same input = same output (when possible)

### Common Mistakes

- Too many tools (decision paralysis)
- Vague descriptions (LLM guesses wrong)
- Complex parameters (LLM makes mistakes)
- Side effects without confirmation (dangerous)

## Reflection

Agents improve by critiquing their own output.

### Basic Reflection Loop

```
1. Generate initial output
2. Critique: "What's wrong with this?"
3. Revise based on critique
4. Repeat until satisfied (or max iterations)
```

### Effective Critique Prompts

- "Rate this output 1-10 and explain why"
- "List 3 things that could be improved"
- "Does this fully answer the original question?"
- "What would a senior expert change?"

### When Reflection Helps

- Writing tasks (drafts → polished)
- Code generation (bugs → working)
- Analysis (shallow → deep)

### When Reflection Hurts

- Simple tasks (adds latency, no improvement)
- Highly constrained outputs (format already correct)
- When the LLM can't evaluate quality (domain expertise needed)

## Multi-Agent Patterns

Multiple agents can accomplish what one cannot.

### Sequential (Pipeline)

```
Agent A → output → Agent B → output → Agent C → final
```

Use when: Each stage requires different expertise or context

### Parallel (Fan-out/Fan-in)

```
        → Agent A →
Task ─→ → Agent B → → Combine → Result
        → Agent C →
```

Use when: Subtasks are independent, speed matters

### Hierarchical (Manager/Workers)

```
Manager Agent
    ├── Worker A (research)
    ├── Worker B (writing)
    └── Worker C (coding)
```

Use when: Complex tasks need coordination, different skills needed

### Debate/Adversarial

```
Agent A (advocate) ←→ Agent B (critic) → Synthesis
```

Use when: Need to explore multiple perspectives, catch errors

## Guardrails

Protect against agent mistakes and misuse.

### Input Guardrails

- Validate user input format
- Check for prompt injection attempts
- Verify permissions/authorization
- Rate limiting

### Output Guardrails

- Format validation (JSON, schema)
- Content filtering (PII, harmful content)
- Confidence thresholds
- Human-in-the-loop for high-stakes actions

### Process Guardrails

- Maximum iterations
- Timeout limits
- Cost caps
- Rollback capabilities

### The 80/20 Rule

Focus guardrails on:
1. Actions that can't be undone (delete, send, publish)
2. Actions involving money or sensitive data
3. Actions affecting other users

## Memory

Agents need memory to maintain context and learn.

### Short-Term Memory

The current conversation/context. Limited by context window.

Management strategies:
- Summarization
- Sliding window
- Importance ranking

### Long-Term Memory

Persistent storage across sessions.

Types:
- **Episodic** - Past interactions ("Last time you asked about X...")
- **Semantic** - Facts and knowledge ("User prefers dark mode")
- **Procedural** - How to do things ("To deploy, run X then Y")

### Implementation Options

1. **Vector databases** - Store embeddings, retrieve by similarity
2. **Structured databases** - Store facts in schemas
3. **File-based** - Simple text files, grep-able
4. **Hybrid** - Combine approaches

### Memory Patterns

- **Write-through** - Save everything, retrieve what's needed
- **Explicit save** - Agent decides what to remember
- **Lessons learned** - Extract insights from failures

## Evaluation

You can't improve what you don't measure.

### Component-Level Evals

Test individual pieces:
- Does the tool work correctly?
- Does the agent choose the right tool?
- Does the output match expected format?

### End-to-End Evals

Test the full pipeline:
- Given this input, is the final output correct?
- Does the agent complete the task?
- Is the user satisfied?

### Eval Types

1. **Exact match** - Output must equal expected
2. **Contains** - Output must include key elements
3. **LLM-as-judge** - Another LLM rates the output
4. **Human evaluation** - Gold standard, expensive

### Building Eval Sets

1. Start with 10-20 diverse examples
2. Include edge cases and failure modes
3. Add cases from real user interactions
4. Sample at scale (can't eval everything)

### The Eval Cycle

```
1. Run evals
2. Find failures
3. Fix issues
4. Re-run evals
5. Ensure no regressions
```

## Putting It Together

Building an effective agent:

1. **Define the task clearly** - What does success look like?
2. **Design minimal tools** - Only what's needed
3. **Engineer the context** - Give it what it needs, nothing more
4. **Add guardrails** - Protect against failure modes
5. **Build evals** - Measure what matters
6. **Iterate** - Improve based on eval results

### Common Failure Modes

| Problem | Likely Cause | Fix |
|---------|--------------|-----|
| Agent loops forever | No clear stop condition | Add max iterations, explicit "done" state |
| Wrong tool chosen | Vague tool descriptions | Make descriptions specific and distinct |
| Hallucinated info | Missing context | Add retrieval, give agent the facts |
| Inconsistent output | Ambiguous instructions | Tighten prompt, add examples |
| Slow performance | Too much reflection | Reduce iterations, cache results |

### The Agent Building Checklist

- [ ] Task is well-defined with clear success criteria
- [ ] Tools are atomic, well-described, and minimal
- [ ] Context includes everything needed, nothing more
- [ ] Guardrails protect against high-impact failures
- [ ] Evals measure what matters
- [ ] Stop conditions are explicit
- [ ] Error handling is graceful
