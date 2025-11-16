---
description: Generate complete solutions for a CLRS chapter/section with all deliverables
---

{% if {2} == 0 %}
Generate complete solutions for **Chapter {1} Problems** of CLRS.

## Task Requirements:

**Source:**
- Read from: `book/Chapter_{1:02d}.pdf`
- Extract all problems from the end of Chapter {1}

**Deliverables:**

1. **Solution Files** (`_solutions/{1:02d}/`)
   - Create markdown files for all problems: P{1:02d}-01.md through P{1:02d}-NN.md
   - Follow existing solution style (review other solutions in the chapter if available)
   - **Intuition first, then mathematical rigor**
   - Include exact problem statement from PDF

2. **Python Code** (`_includes/code/{1:02d}/`)
   - **ONLY create code files when they enhance understanding through interactive simulation**
   - Examples where code is valuable: simulations, randomized algorithms, visualizing probability
   - Examples where code is NOT needed: pure mathematical proofs, recurrence solving, asymptotic analysis
   - **Keep code simple and fast** - default execution should complete in < 0.5 seconds
   - Follow performance guidelines (see "Code Performance Guidelines" below)
   - Create Skulpt-compatible implementations
   - Include test cases and examples
   - Add clear comments

3. **Images** (`assets/img/{1:02d}/`)
   - Generate social media preview images for ALL problems
   - Use command-line interface: `python3 utils/GenerateImage.py {1} 0 N`
   - Arguments: chapter, section (0 for problems), problem_id
   - Image naming: `{1}-N.jpg` (no section number)
   - Verify all images generated successfully

4. **Table of Contents**
   - Update `_data/toc.json` if this is a new chapter
   - Add problem count to chapter metadata
{% else %}
Generate complete solutions for **Chapter {1}, Section {2}** of CLRS.

## Task Requirements:

**Source:**
- Read from: `book/Chapter_{1:02d}.pdf`
- Extract all exercises from Section {2}

**Deliverables:**

1. **Solution Files** (`_solutions/{1:02d}/`)
   - Create markdown files for all exercises: E{1:02d}.{2:02d}-01.md through E{1:02d}.{2:02d}-NN.md
   - Follow existing solution style (review other solutions in the chapter if available)
   - **Intuition first, then mathematical rigor**
   - Include exact problem statement from PDF

2. **Python Code** (`_includes/code/{1:02d}/`)
   - **ONLY create code files when they enhance understanding through interactive simulation**
   - Examples where code is valuable: simulations, randomized algorithms, visualizing probability
   - Examples where code is NOT needed: pure mathematical proofs, recurrence solving, asymptotic analysis
   - **Keep code simple and fast** - default execution should complete in < 0.5 seconds
   - Follow performance guidelines (see "Code Performance Guidelines" below)
   - Create Skulpt-compatible implementations
   - Include test cases and examples
   - Add clear comments

3. **Images** (`assets/img/{1:02d}/`)
   - Generate social media preview images for ALL exercises
   - Use command-line interface: `python3 utils/GenerateImage.py {1} {2} N`
   - Arguments: chapter, section, problem_id
   - Verify all images generated successfully

4. **Table of Contents**
   - Update `_data/toc.json` if this is a new chapter
   - Add section name and exercise count
{% endif %}

## Solution Writing Guidelines:

**Structure:**
1. Problem statement (exact quote from book)
2. **INTUITION FIRST** - Plain language explanation before any math
3. Approach/strategy with concrete examples
4. Detailed solution with step-by-step walkthrough
5. Mathematical analysis (if needed)
6. Implementation code (if applicable)
7. Edge cases/insights in aside boxes

**Writing Style:**
- **NO subheadings like "Intuition:", "Recurrence:", "Solution:"** - let the text flow naturally
- **NO em-dashes (—)** - use commas, parentheses, or split into separate sentences
- Start each method/part with intuitive explanation in paragraph form
- Use concrete analogies (e.g., dictionary, photocopying pages)
- Explain recurrence equations after establishing intuition
- For multi-part problems, use section headers like "### A.", "### B.", not "### Part (a):"

**Mathematical Formatting:**
- Use `\begin{align*}...\end{align*}` for multi-step equations
- Example:
  ```latex
  $$\begin{align*}
  f(n) &= \Theta(n) \\
       &= \Theta(n^{\log_2 2}) \\
       &= \Theta(n^{\log_b a})
  \end{align*}$$
  ```
- Avoid bulleted lists with LaTeX - use aligned equations instead
- Single-line equations can use `$$...$$`

**Ads Placement:**
- **Insert `{% include ads.html %}` for moderate to long solutions**
- Place at natural content breaks (e.g., between major parts)
- For 2-part problems: after Part A, possibly after Part B if content is long
- For 3+ part problems: after every 1-2 parts depending on length
- Reference: See `_solutions/02/P02-02.md` for good example

**External Links:**
- Optional but valuable for key concepts
- Maximum 1-2 links per solution
- Only for concepts not fully explained in CLRS
- Prefer: Wikipedia, academic papers, authoritative tutorials
- Always use: `{:target="_blank"}` format
- Example: `[convex hull](https://en.wikipedia.org/wiki/Convex_hull){:target="_blank"}`

**Quality Standards:**
- **Intuition before mathematics** - this is the #1 priority
- Accessible to learners (don't assume advanced CS background)
- Use concrete examples and analogies
- Build progressive understanding
- Use aside boxes for insights, edge cases, and "why" explanations
- Cross-reference related exercises when relevant
- Test all code implementations

## Code Performance Guidelines:

**When to Create Interactive Code:**
- ✓ Algorithm visualizations where behavior is non-obvious
- ✓ Examples that can be shown with hands-on code
- ✗ Pure mathematical derivations
- ✗ Recurrence relation solving
- ✗ Asymptotic complexity proofs

**Performance Requirements:**
- Default execution must complete in **< 0.5 seconds**
- Use small default parameters:
  - Simulation trials: 500-1000 (NOT 10,000+)
  - Test input sizes: 2-3 examples (NOT 5-6)
  - Individual examples: 3-5 iterations (NOT 10+)
- Users can modify code to test larger values if desired

**Example of Good Performance:**
```python
# GOOD - Fast defaults, 2 sizes, 1000 trials
def simulate(n, num_trials=1000):
    # ...

for size in [5, 10]:  # Only 2 sizes
    result = simulate(size)
    # ...

# Show 5 individual examples (not 10)
for i in range(5):
    print(f"Example {i+1}: {example()}")
```

**Example of Poor Performance:**
```python
# BAD - Too slow, too many sizes, too many trials
def simulate(n, num_trials=10000):  # TOO MANY
    # ...

for size in [5, 10, 20, 50, 100]:  # TOO MANY sizes
    result = simulate(size)
    # ...

for i in range(20):  # TOO MANY examples
    print(f"Example {i+1}: {example()}")
```

**Integration:**
- Only add code to markdown if it's actually used
- Add at end of solution: `### Interactive Simulation`
- Use: `{% include code/code.html file='code/{1:02d}/code_E{1:02d}{2:02d}{3:02d}.py' %}`
- Don't create orphaned code files that aren't referenced

## Git Workflow:

- Keep changes in isolated feature branch and commit to Github
- **DO NOT merge to master** - leave for user review

## Execution:

Work through all steps systematically. Use the TodoWrite tool to track progress through:
{% if {2} == 0 %}
1. Reading PDF and extracting problems from end of chapter
2. Creating each problem solution file (P{1:02d}-NN.md)
3. Writing Python code files (if applicable)
4. Generating images (using section=0 convention)
5. Updating toc.json
6. Creating git branch and committing
{% else %}
1. Reading PDF and extracting exercises from Section {2}
2. Creating each exercise solution file (E{1:02d}.{2:02d}-NN.md)
3. Writing Python code files (if applicable)
4. Generating images
5. Updating toc.json
6. Creating git branch and committing
{% endif %}

Report completion with summary of all files created.
