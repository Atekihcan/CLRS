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
   - Create Skulpt-compatible implementations where applicable
   - Include test cases and examples
   - Add clear comments

3. **Images** (`assets/img/{1:02d}/`)
   - Generate social media preview images for ALL problems
   - Use: `utils/generate_ch{1}_images.py` (create this script)
   - Use `CreateImage(chapter={1}, section=0, problem_id=N)` for problems
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
   - Create Skulpt-compatible implementations where applicable
   - Include test cases and examples
   - Add clear comments

3. **Images** (`assets/img/{1:02d}/`)
   - Generate social media preview images for ALL exercises
   - Use: `utils/generate_ch{1}_images.py` (create this script)
   - Verify all images generated successfully

4. **Table of Contents**
   - Update `_data/toc.json` if this is a new chapter
   - Add section name and exercise count
{% endif %}

## Solution Writing Guidelines:

**Structure:**
1. Problem statement (exact quote from book)
2. Intuitive explanation in plain language
3. Approach/strategy
4. Detailed solution with step-by-step walkthrough
5. Mathematical analysis (if needed)
6. Implementation code (if applicable)
7. Edge cases/insights in aside boxes

**External Links:**
- Optional but valuable for key concepts
- Maximum 1-2 links per solution
- Only for concepts not fully explained in CLRS
- Prefer: Wikipedia, academic papers, authoritative tutorials
- Always use: `{:target="_blank"}` format
- Example: `[convex hull](https://en.wikipedia.org/wiki/Convex_hull){:target="_blank"}`

**Quality Standards:**
- Accessible to learners (don't assume advanced CS background)
- Build progressive understanding
- Use "Did you notice?" asides for insights
- Cross-reference related exercises when relevant
- Test all code implementations

## Git Workflow:

{% if {2} == 0 %}
- Create branch: `solutions/chapter-{1}-problems`
- Commit with descriptive message (e.g., "Add solutions for Chapter {1} problems")
{% else %}
- Create branch: `solutions/chapter-{1}-section-{2}`
- Commit with descriptive message (e.g., "Add solutions for Chapter {1}, Section {2}")
{% endif %}
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
