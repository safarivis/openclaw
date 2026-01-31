# Context Engineering Pattern

**The most important skill in agent building.**

Context = everything the LLM sees when making a decision. Get this right, and the agent works. Get it wrong, and no amount of clever prompting will help.

## Core Principle

**Give the agent exactly what it needs to make this decision, nothing more.**

## What Goes in Context

### System Prompt
- Agent identity and role
- Core instructions and constraints
- Output format expectations
- Available tools and when to use them

### Conversation History
- Previous turns (summarized if long)
- Key decisions and their reasoning
- User preferences learned so far

### Dynamic Context
- Tool results
- Retrieved documents
- Current state (files open, progress made)

### Task-Specific Information
- User's current request
- Relevant data for this request
- Examples of desired output

## Context Management Strategies

### For Short Conversations
Keep everything. No management needed.

### For Long Conversations
**Summarization:** Periodically compress history into key points.

```
Original: 50 messages of back-and-forth
Compressed: "User is building a Python API. We've completed auth module.
            User prefers type hints. Current task: add rate limiting."
```

**Sliding Window:** Keep last N messages + summary of earlier context.

**Importance Ranking:** Keep messages marked as important, summarize the rest.

### For Large Codebases
**Focused retrieval:** Only include files relevant to current task.

```
Bad: Dump entire codebase into context
Good: Include only: current file, directly imported files, relevant tests
```

### For Multiple Documents
**RAG (Retrieval-Augmented Generation):**
1. Embed documents into vector store
2. When query comes in, retrieve top-k relevant chunks
3. Include only those chunks in context

## Positioning Matters

LLMs have **recency bias** - information near the end gets more attention.

**Good structure:**
```
1. System prompt (identity, general rules)
2. Background context (history, retrieved docs)
3. Current state (what's happening now)
4. User's question (most recent, gets most attention)
```

## Common Mistakes

### Too Much Context
- Agent gets confused by irrelevant information
- Important details get lost in the noise
- Token limits exceeded

**Fix:** Curate ruthlessly. Ask "Does the agent need THIS to make THIS decision?"

### Too Little Context
- Agent hallucinates missing information
- Makes wrong assumptions
- Asks obvious questions

**Fix:** Trace through the decision. What facts does it need? Are they present?

### Unstructured Context
- Agent can't find what it needs
- Misinterprets boundaries between sections

**Fix:** Use clear headers, separators, formatting. Make structure obvious.

### Stale Context
- Agent acts on outdated information
- Contradicts more recent facts

**Fix:** Timestamp information. Summarize and refresh periodically.

## Implementation Checklist

- [ ] System prompt defines role and constraints
- [ ] Context is structured with clear sections
- [ ] Only relevant information is included
- [ ] Important information is positioned near the end
- [ ] Long conversations are summarized
- [ ] Stale information is refreshed
- [ ] Token limits are respected
