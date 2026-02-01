# Tools

Tools for accessing and managing Seth Godin knowledge.

## Knowledge Base Access

### search_concepts
Search the knowledge base for relevant concepts.

**When to use:** Finding frameworks that apply to a challenge
**Parameters:**
- query (string, required): What to search for
- limit (integer, optional): Max results (default: 5)

**Returns:**
```yaml
type: object
properties:
  matches: array
    - concept: string - Concept name
    - relevance: number - Match score 0-1
    - summary: string - Brief description
    - source: string - Original source
  count: integer - Number of matches
```

### read_concept
Load full details of a specific concept.

**When to use:** Deep dive into a framework
**Parameters:**
- name (string, required): Concept name (e.g., "purple-cow", "smallest-viable-audience")

**Returns:**
```yaml
type: object
properties:
  name: string - Concept name
  source: string - Book/post where it originated
  summary: string - One-line explanation
  full_explanation: string - Detailed content
  examples: array - Real-world examples
  related_concepts: array - Connected ideas
  quotes: array - Relevant Seth quotes with citations
```

### list_concepts
List all concepts in the knowledge base.

**When to use:** Browsing available knowledge
**Parameters:**
- category (string, optional): Filter by category

**Returns:**
```yaml
type: object
properties:
  concepts: array
    - name: string
    - category: string
    - source: string
  count: integer
```

## Ingestion Tools

### extract_concepts
Extract concepts from raw content.

**When to use:** Processing new Seth Godin content
**Parameters:**
- content (string, required): Raw text to process
- source (string, required): Where it came from (book title, blog URL)

**Returns:**
```yaml
type: object
properties:
  concepts: array
    - name: string - Proposed concept name
    - summary: string - Brief description
    - content: string - Full extracted content
    - quotes: array - Notable quotes
  duplicates: array - Existing concepts that overlap
```

### save_concept
Save a concept to the knowledge base.

**When to use:** After user approves extracted concept
**Parameters:**
- name (string, required): Concept name (kebab-case)
- content (object, required): Full concept data
- source (string, required): Citation

**Returns:**
```yaml
type: object
properties:
  success: boolean
  path: string - Where saved
  message: string
```

**Warning:** Always get user approval before saving. Never auto-save.

## Citation Tools

### get_source
Get full citation for a source.

**When to use:** Providing references
**Parameters:**
- source_id (string, required): Source identifier

**Returns:**
```yaml
type: object
properties:
  title: string - Book/post title
  author: string - Always "Seth Godin"
  year: integer - Publication year
  type: enum - "book" | "blog" | "podcast" | "talk"
  url: string | null - Link if available
```

### cite
Format a citation for output.

**When to use:** Adding references to advice
**Parameters:**
- concept (string, required): Concept name
- format (enum, optional): "inline" | "footnote" | "full" (default: "inline")

**Returns:**
```yaml
type: object
properties:
  citation: string - Formatted citation
```

## Analysis Tools

### find_connections
Find relationships between concepts.

**When to use:** Connect Mode, showing how ideas relate
**Parameters:**
- concepts (array, required): List of concept names to connect

**Returns:**
```yaml
type: object
properties:
  connections: array
    - from: string
    - to: string
    - relationship: string - How they connect
    - tension: boolean - Do they create productive tension?
```

### apply_framework
Apply a specific framework to a situation.

**When to use:** Structured analysis using Seth's models
**Parameters:**
- framework (string, required): Which framework to apply
- situation (string, required): The brand/challenge to analyze

**Returns:**
```yaml
type: object
properties:
  framework: string
  analysis: object - Framework-specific output
  recommendations: array - Action items
  citations: array - Source references
```
