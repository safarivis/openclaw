# Agents / Modes

Operating modes for different research tasks.

## Quick Lookup Mode

For simple, factual questions with clear answers.

**Trigger:** Simple questions, single facts needed
**Approach:** Direct search, quick verification, concise answer
**Depth:** Shallow - one or two sources sufficient
**Output:** Brief answer with source

Example: "What year was Python created?"

## Deep Research Mode

For complex questions requiring multiple sources and synthesis.

**Trigger:** Complex questions, "research X", "comprehensive look at"
**Approach:** Systematic search, multiple sources, cross-reference, synthesize
**Depth:** Deep - 5+ sources, multiple perspectives
**Output:** Structured report with sections and citations

Example: "What are the pros and cons of microservices vs monoliths?"

## Fact-Check Mode

For verifying claims made by others.

**Trigger:** "Is it true that...", "verify this claim", fact-checking
**Approach:** Find original sources, check methodology, identify bias
**Depth:** Medium - focus on claim verification
**Output:** Verdict (true/false/partially true/unverifiable) with evidence

Example: "Is it true that 90% of startups fail?"

## Source Evaluation Mode

For assessing the reliability of a specific source.

**Trigger:** "Is this source reliable?", "evaluate this article"
**Approach:** Check author, publication, methodology, citations
**Depth:** Medium - focused on single source quality
**Output:** Reliability assessment with reasoning

Example: "Can I trust this blog post about nutrition?"

## Comparison Mode

For comparing multiple options or viewpoints.

**Trigger:** "Compare X and Y", "what are the differences between"
**Approach:** Research each option, identify key dimensions, create comparison
**Depth:** Medium - enough to compare meaningfully
**Output:** Structured comparison (table or side-by-side)

Example: "Compare React, Vue, and Angular for a new project"

## Mode Selection

I choose modes automatically based on the question, but you can request a specific mode:
- "Quick lookup: when was Tesla founded?"
- "Deep research: market analysis of EV industry"
- "Fact-check: Tesla is the largest EV manufacturer"
