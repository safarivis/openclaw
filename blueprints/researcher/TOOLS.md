# Tools

<!-- CUSTOMIZE: Add or remove tools based on your agent's capabilities -->

## Core Tools

### web_search
Search the web for information.

**When to use:** Finding current information, exploring topics, locating sources
**Parameters:**
- query: Search terms
- date_range: Recent, past year, any time

**Tips:**
- Use specific, targeted queries
- Try multiple phrasings if first search fails
- Include domain-specific terms

### read_url
Fetch and read content from a URL.

**When to use:** Accessing specific sources, reading articles, extracting data
**Parameters:**
- url: The page to read

**Tips:**
- Verify URL looks legitimate before fetching
- Note publication date and author
- Extract key points, don't summarize entire article

### search_documents
Search internal document collection (RAG).

**When to use:** Finding information in local files, internal knowledge base
**Parameters:**
- query: Search terms
- doc_type: Filter by document type

**Tips:**
- Start broad, narrow if too many results
- Try synonyms and related terms

## Optional Tools

### search_academic
Search academic papers and research.

**When to use:** Scientific questions, need peer-reviewed sources
**Parameters:**
- query: Search terms
- subject: Filter by field

### search_news
Search recent news articles.

**When to use:** Current events, recent developments
**Parameters:**
- query: Search terms
- date_range: Time period

### verify_fact
Cross-reference a claim against fact-checking sources.

**When to use:** Verifying specific claims, detecting misinformation
**Parameters:**
- claim: The statement to verify

## Tool Usage Guidelines

1. **Start with search** - Get an overview before diving deep
2. **Read multiple sources** - Don't rely on single source
3. **Verify important claims** - Cross-reference critical information
4. **Note source quality** - Primary vs secondary, bias, credentials
5. **Track sources** - Keep URLs for citation
