# Memory Pattern

Enable agents to remember across sessions and learn from experience.

## Why Memory Matters

Without memory, every conversation starts fresh:
- User repeats preferences
- Agent forgets past decisions
- Same mistakes repeated
- No learning over time

## Memory Types

### Short-Term Memory
Current conversation context. Limited by token window.

**What to store:**
- Conversation history
- Current task state
- Recent tool results

**Management:**
- Summarization (compress old messages)
- Sliding window (keep N recent turns)
- Importance weighting (keep key moments)

### Long-Term Memory
Persistent storage across sessions.

**Types:**

| Type | What It Stores | Example |
|------|---------------|---------|
| Episodic | Past interactions | "Last time you asked about X..." |
| Semantic | Facts and knowledge | "User prefers dark mode" |
| Procedural | How to do things | "Deploy by running X then Y" |

### Lessons Learned
Insights extracted from failures and successes.

```
Session: 2024-01-15
Task: Deploy to production
Outcome: Failed
Lesson: Always check disk space before deploying. Deployment failed
        because /tmp was full.
```

## Implementation Approaches

### 1. File-Based Memory
Simple text files. Easy to read and debug.

```
memory/
├── user_preferences.md
├── project_context.md
└── lessons_learned.md
```

**Pros:** Simple, grep-able, no dependencies
**Cons:** Doesn't scale, no semantic search

### 2. Vector Database
Store embeddings, retrieve by similarity.

```python
# Store
embedding = embed(text)
vector_db.store(embedding, metadata)

# Retrieve
query_embedding = embed(query)
results = vector_db.search(query_embedding, top_k=5)
```

**Pros:** Semantic search, scales well
**Cons:** Setup complexity, embedding costs

### 3. Structured Database
Store facts in schemas.

```sql
CREATE TABLE user_preferences (
    user_id TEXT,
    preference_key TEXT,
    preference_value TEXT,
    updated_at TIMESTAMP
);
```

**Pros:** Precise queries, relationships
**Cons:** Schema management, less flexible

### 4. Hybrid
Combine approaches for different needs.

```
- Vector DB for semantic retrieval
- SQL for structured facts
- Files for lessons learned
```

## Memory Operations

### Write Patterns

**Write-through:** Save everything, retrieve what's needed.
```python
def on_message(message):
    memory.store(message)  # Store all
    # Retrieve only when needed
```

**Explicit save:** Agent decides what to remember.
```python
def process_response(response):
    if response.contains_important_info:
        memory.store(response.extract_facts())
```

**Periodic summarization:** Compress and save periodically.
```python
def end_session(history):
    summary = summarize(history)
    key_facts = extract_facts(history)
    memory.store(summary, key_facts)
```

### Read Patterns

**Eager loading:** Load all relevant memory at start.
```python
def start_session(user_id):
    context = memory.load_user_context(user_id)
    return Agent(context=context)
```

**Lazy retrieval:** Fetch memory when needed.
```python
def handle_query(query):
    # Only retrieve if query seems to need history
    if needs_context(query):
        context = memory.search(query)
        return agent.respond(query, context)
    return agent.respond(query)
```

**RAG (Retrieval-Augmented):** Retrieve relevant chunks per query.
```python
def respond(query):
    relevant_memories = vector_db.search(query, top_k=5)
    prompt = build_prompt(query, relevant_memories)
    return llm.generate(prompt)
```

## Memory for Different Agent Types

### Personal Assistant
- Remember user preferences
- Track ongoing projects
- Store frequently needed info

### Research Agent
- Cache search results
- Track sources already consulted
- Remember dead ends (don't repeat)

### Coding Agent
- Remember codebase structure
- Store common patterns used
- Track decisions and rationale

### Business Agent
- Remember customer context
- Store interaction history
- Track task progress

## Lessons Learned System

A specific pattern for learning from experience.

### Structure
```markdown
## Lesson: [Title]
Date: [When learned]
Context: [What was happening]
Outcome: [What went wrong/right]
Lesson: [What to do differently]
Applies to: [When to remember this]
```

### Example
```markdown
## Lesson: Check file existence before editing
Date: 2024-01-15
Context: Tried to edit config.yaml
Outcome: Error - file didn't exist
Lesson: Always verify file exists before attempting edit. Create if needed.
Applies to: Any file edit operation
```

### Using Lessons
1. At session start, load relevant lessons
2. When similar context arises, surface the lesson
3. Apply the learned behavior

## Common Mistakes

### Remembering Too Much
Context gets cluttered, relevant info buried.

**Fix:** Curate ruthlessly. Summarize and discard old details.

### Forgetting Important Things
Key facts lost over time.

**Fix:** Explicit importance markers. Never auto-delete marked items.

### Stale Memory
Outdated info causes wrong decisions.

**Fix:** Timestamps. Periodic refresh. Conflict resolution.

### No Memory Retrieval
Store everything but never use it.

**Fix:** Actively retrieve. Make retrieval part of standard flow.

### Privacy Issues
Storing sensitive information.

**Fix:** Clear data retention policies. Encryption. User control.

## Implementation Checklist

- [ ] Decide what to remember (user prefs, facts, lessons)
- [ ] Choose storage approach (files, vector DB, SQL)
- [ ] Define write triggers (every message, explicit save, end of session)
- [ ] Define read triggers (session start, on relevant query, RAG)
- [ ] Set retention policies (how long to keep, when to summarize)
- [ ] Handle conflicts (newer overwrites, merge, ask user)
- [ ] Consider privacy (what not to store, encryption, deletion)
