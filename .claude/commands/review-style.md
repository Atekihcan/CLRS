---
description: Review existing solutions and suggest style/quality improvements
---

{% if {2} == 0 %}
Review solutions for **Chapter {1} Problems** and provide improvement suggestions.
{% else %}
Review solutions for **Chapter {1}, Section {2}** and provide improvement suggestions.
{% endif %}

## Review Focus Areas:

### 1. Pedagogical Quality
- Does it build intuition before diving into mathematics?
- Is the explanation accessible to learners?
- Does it use progressive complexity building?
- Are there practical examples?

### 2. Content Structure
Check this order:
1. Problem statement (exact quote)
2. Intuitive explanation
3. Approach/strategy
4. Detailed solution
5. Mathematical analysis
6. Implementation
7. Edge cases/insights

### 3. External Resources
- Are there 1-2 helpful external links where concepts need clarification?
- Links to Wikipedia, academic papers, or authoritative tutorials?
- Using `{:target="_blank"}` format?
- Only for concepts not fully explained in CLRS?

### 4. Code Quality
- Is code Skulpt-compatible?
- Are there practical test cases?
- Do comments explain the "why" not just the "what"?

### 5. Visual Elements
- Use of asides for:
  - "Did you notice?" insights
  - Edge cases
  - Interesting observations
  - Performance notes

## Process:

{% if {2} == 0 %}
1. Read all existing problem solutions for Chapter {1} (P{1:02d}-*.md)
2. Analyze current quality and style
3. **Report findings and suggestions**:
   - What's working well
   - What could be improved
   - Specific suggestions for each problem
   - Categorize suggestions (critical, important, nice-to-have)
4. Check consistency across all problem solutions
{% else %}
1. Read all existing solutions for Chapter {1}, Section {2} (E{1:02d}.{2:02d}-*.md)
2. Analyze current quality and style
3. **Report findings and suggestions**:
   - What's working well
   - What could be improved
   - Specific suggestions for each exercise
   - Categorize suggestions (critical, important, nice-to-have)
4. Check consistency across all solutions in the section
{% endif %}

## Important:

**DO NOT make changes automatically.** This is a review and suggestion process:
- Provide specific, actionable suggestions
- Explain WHY each change would improve the solution
- Categorize suggestions by impact
- Show examples of better approaches when suggesting changes
- **Ask for explicit permission** before making any changes
- Avoid nitpicky suggestions - focus on meaningful improvements

## Report Format:

{% if {2} == 0 %}
For each problem, provide:
{% else %}
For each exercise, provide:
{% endif %}
- Overall assessment
- Strengths (what's done well)
- Improvement opportunities (categorized)
- Specific suggestions with examples
- Consistency notes

End with:
- Summary of overall quality
- Priority recommendations
- Ask: "Would you like me to implement any of these suggestions?"

{% if {2} == 0 %}
Use TodoWrite to track progress through each problem.
{% else %}
Use TodoWrite to track progress through each exercise.
{% endif %}
