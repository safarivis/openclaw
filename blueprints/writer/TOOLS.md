# Tools

<!-- CUSTOMIZE: Add or remove tools based on your agent's capabilities -->

## Core Tools

### read_file
Read content from a file.

**When to use:** Opening documents to edit, reading reference material
**Parameters:**
- path: File location

### write_file
Save content to a file.

**When to use:** Saving drafts, outputting final content
**Parameters:**
- path: File location
- content: Content to write

### search_web
Search for reference information.

**When to use:** Fact-checking, finding examples, researching topics
**Parameters:**
- query: Search terms

**Tips:**
- Research before writing when facts are needed
- Find examples of good writing in the target style

## Optional Tools

### grammar_check
Check text for grammar and spelling errors.

**When to use:** Final polish before delivery
**Parameters:**
- text: Content to check

### readability_score
Analyze text complexity.

**When to use:** Ensuring content matches audience level
**Parameters:**
- text: Content to analyze
**Returns:** Reading level, complexity metrics

### plagiarism_check
Check for unoriginal content.

**When to use:** Verifying originality
**Parameters:**
- text: Content to check

### seo_analyze
Analyze content for search optimization.

**When to use:** Blog posts, web content meant to rank
**Parameters:**
- text: Content to analyze
- keywords: Target keywords

## Tool Usage Guidelines

1. **Research before writing** - Get facts straight first
2. **Save incrementally** - Don't lose work on long pieces
3. **Check before delivering** - Grammar and readability passes
4. **Verify originality** - Especially for published content
