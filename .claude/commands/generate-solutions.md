---
description: Generate complete solutions for a CLRS chapter/section with all deliverables
---

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

- Create branch: `solutions/chapter-{1}-section-{2}`
- Commit with descriptive message
- **DO NOT merge to master** - leave for user review

## Execution:

Work through all steps systematically. Use the TodoWrite tool to track progress through:
1. Reading PDF and extracting exercises
2. Creating each solution file
3. Writing Python code files
4. Generating images
5. Updating toc.json
6. Creating git branch and committing

Report completion with summary of all files created.
