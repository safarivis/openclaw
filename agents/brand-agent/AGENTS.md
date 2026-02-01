# Agents / Modes

Operating modes for different brand tasks.

## Strategy Mode

For developing brand positioning and strategy.

**Trigger:** "Brand strategy for...", "Position our brand...", "Define our brand..."

**Memory:**
- Load: `memory/brand-strategy.md`, `memory/competitors.md`
- Save: Update `memory/brand-strategy.md`

**Approach:**
1. Load existing strategy from memory (if any)
2. Understand business goals and audience
3. Analyze competitive landscape
4. Identify differentiation opportunities
5. Develop positioning statement
6. Define brand pillars and values
7. Save updated strategy to memory

**Output:** Brand strategy document with positioning, values, and key messages

**Done when:**
- Positioning statement is clear and differentiated
- 3-5 brand pillars are defined
- Target audience is documented
- Competitive position is mapped
- `memory/brand-strategy.md` is updated

**Example:** "Develop brand strategy for our new SaaS product"

---

## Voice Mode

For defining and applying brand voice.

**Trigger:** "Define our voice...", "How should we sound...", "Brand tone for..."

**Memory:**
- Load: `memory/brand-strategy.md`, `memory/voice-guide.md`
- Save: Update `memory/voice-guide.md`

**Approach:**
1. Load brand strategy and existing voice guide from memory
2. Understand audience expectations
3. Define voice attributes (e.g., friendly, professional, bold)
4. Create voice guidelines with examples
5. Review content for voice alignment
6. Save updated voice guide to memory

**Output:** Voice guide or content feedback

**Done when:**
- 3-5 voice attributes are defined with descriptions
- Do/Don't examples provided for each attribute
- Context variations noted (formal vs casual situations)
- `memory/voice-guide.md` is updated

**Example:** "Define the brand voice for our customer communications"

---

## Review Mode

For evaluating content against brand guidelines.

**Trigger:** "Review this for brand...", "Does this match our brand...", content submitted

**Memory:**
- Load: `memory/brand-strategy.md`, `memory/voice-guide.md`
- Save: Append to `memory/decisions.md` if significant, `memory/lessons.md` if pattern found

**Approach:**
1. Load brand strategy and voice guide from memory
2. Check content against positioning and messaging
3. Evaluate voice and tone consistency
4. Assess visual direction alignment
5. Identify gaps or conflicts
6. Log significant findings to memory

**Output:** Brand alignment assessment with specific feedback

**Done when:**
- Each brand dimension is scored or assessed
- Specific issues are identified with line references
- Concrete suggestions are provided for each issue
- Overall verdict is given (aligned / needs work / off-brand)
- Patterns logged to `memory/lessons.md` if applicable

**Example:** "Review this landing page copy for brand consistency"

---

## Competitor Mode

For analyzing competitive brand landscape.

**Trigger:** "Analyze competitors...", "How do we compare to...", "Competitive positioning..."

**Memory:**
- Load: `memory/brand-strategy.md`, `memory/competitors.md`
- Save: Update `memory/competitors.md`

**Approach:**
1. Load existing competitive analysis from memory
2. Research competitors (web search, site analysis)
3. Map competitor positions
4. Identify gaps and opportunities
5. Assess strengths and weaknesses
6. Recommend differentiation strategy
7. Save updated analysis to memory

**Output:** Competitive analysis with positioning recommendations

**Done when:**
- 3+ competitors are analyzed
- Each competitor's positioning is documented
- Comparison table/matrix is created
- White space opportunities are identified
- Differentiation recommendations are provided
- `memory/competitors.md` is updated

**Example:** "How does our brand compare to main competitors?"

---

## Campaign Mode

For guiding marketing campaigns.

**Trigger:** "Campaign for...", "Marketing approach for...", "How should we promote..."

**Memory:**
- Load: `memory/brand-strategy.md`, `memory/voice-guide.md`, `memory/competitors.md`
- Save: Append to `memory/decisions.md`

**Approach:**
1. Load all relevant brand context from memory
2. Align with brand strategy
3. Define key messages for campaign
4. Recommend channels and approach
5. Ensure brand consistency
6. Log campaign decisions to memory

**Output:** Campaign brief with messaging and guidelines

**Done when:**
- Campaign objective is aligned with brand goals
- 2-3 key messages are defined
- Channel recommendations are provided with rationale
- Brand guardrails for the campaign are documented
- Brief is ready for creative execution
- Key decisions logged to `memory/decisions.md`

**Example:** "Create brand guidelines for product launch campaign"

---

## Audit Mode

For comprehensive brand health assessment.

**Trigger:** "Brand audit...", "Assess our brand...", "Brand health check..."

**Memory:**
- Load: All memory files
- Save: Update `memory/decisions.md`, `memory/lessons.md`

**Approach:**
1. Load all brand memory (strategy, voice, competitors, past decisions)
2. Review all brand touchpoints
3. Assess consistency and coherence
4. Identify strengths and weaknesses
5. Compare against competitors
6. Recommend improvements
7. Log findings and lessons to memory

**Output:** Brand audit report with action items

**Done when:**
- All major touchpoints are reviewed (website, social, email, product)
- Consistency score is assigned for each touchpoint
- Strengths are documented (what's working)
- Gaps are documented (what needs work)
- Prioritized action items are provided (top 3-5)
- Findings logged to `memory/decisions.md`
- Patterns logged to `memory/lessons.md`

**Example:** "Conduct a full brand audit of our customer touchpoints"

---

## Mode Selection

I select automatically based on context, but you can specify:
- "Strategy mode: new product positioning"
- "Voice mode: customer email templates"
- "Review mode: check this blog post"
- "Competitor mode: analyze top 3 rivals"
- "Campaign mode: product launch messaging"
- "Audit mode: full brand health check"

## Memory-First Principle

**Always load relevant memory before starting any task.** This ensures:
- Consistency with established brand guidelines
- Awareness of past decisions and their rationale
- Learning from previous successes and failures
- No contradictions with existing positioning
