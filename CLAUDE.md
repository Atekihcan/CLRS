# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based static website that provides solutions to exercises and problems from "Introduction to Algorithms" (3rd edition) by Cormen, Leiserson, Rivest, and Stein (CLRS). The site is deployed to GitHub Pages at https://atekihcan.github.io/CLRS/.

## Development Commands

### Building and Testing Locally

```bash
# Install dependencies (first time only)
bundle install

# Start development server with live reload (recommended)
./serve.sh
# OR manually:
bundle exec jekyll serve --livereload

# Build the site for production (output to _site/)
./build.sh
# OR manually:
bundle exec jekyll build
```

**Live Reload Features:**
- Automatically rebuilds site when files change
- Automatically refreshes browser on changes
- No need to manually rebuild or refresh
- Server runs at: http://127.0.0.1:4000/CLRS/

### Deployment

The site automatically deploys via GitHub Actions on every push to the master branch. See `.github/workflows/github-pages.yml` for the workflow configuration.

### Git Workflow for New Solutions

**Always work in a feature branch:**

```bash
# Create a new branch for the chapter/section
git checkout -b solutions/chapter-X-section-Y

# After generating solutions, commit
git add .
git commit -m "Add solutions for Chapter X, Section Y"

# Push the branch
git push origin solutions/chapter-X-section-Y

# Create a PR for review (or merge locally after testing)
```

**Branch Naming Convention:**
- Single section: `solutions/chapter-5-section-1`
- Multiple sections: `solutions/chapter-5-sections-1-2-3`
- Entire chapter: `solutions/chapter-5`
- Bug fixes: `fix/chapter-5-typo`

## Architecture

### Content Structure

**Solution Files** (`_solutions/`)
- Organized by chapter number (e.g., `01/`, `02/`, `03/`, etc.)
- Naming convention:
  - Exercises: `E[chapter].[section]-[number].md` (e.g., `E01.01-01.md`)
  - Problems: `P[chapter]-[number].md` (e.g., `P01-01.md`)
  - Appendix: `EA.[section]-[number].md` (e.g., `EA.01-01.md`)
- Each solution is a markdown file with YAML front matter containing:
  - `title`: Exercise/problem identifier
  - `published`: Original publication date
  - `modified`: Last modification date
  - `description`: The exercise/problem statement

**Table of Contents** (`_data/toc.json`)
- Structured JSON defining the book's chapter and section organization
- Contains metadata about exercise counts per section
- Used to generate navigation and ensure coverage

### Templates and Includes

**Layouts** (`_layouts/`)
- `base.html`: Main layout template
- `post.html`: Solution page layout (extends base)

**Includes** (`_includes/`)
- `code/`: Python code snippets for interactive execution (using Skulpt)
  - Organized by chapter (e.g., `code/01/`, `code/02/`)
  - Embedded in solutions for demonstration
- `graph/`: HTML files containing graph visualizations
- `analytics.html`: Google Analytics integration
- `comment.html`: Disqus comments integration
- Standard partials: `head.html`, `header.html`, `footer.html`, `aside.html`

### Assets

**Static Resources** (`assets/`)
- `css/`: Stylesheets (normalize, syntax highlighting, custom site styles)
- `js/`: JavaScript including Skulpt (in-browser Python execution)
- `img/`: Solution diagrams and illustrations organized by chapter
- `katex/`: LaTeX math rendering library

### Jekyll Configuration

Key settings in `_config.yml`:
- Uses kramdown with GFM (GitHub Flavored Markdown)
- Solutions are a Jekyll collection with custom permalink structure
- Base URL: `/CLRS`
- Plugins: `jemoji`, `jekyll-redirect-from`

## Solution Writing Guidelines

### Core Philosophy

**Intuition First, Mathematics Second**
- Start with conceptual understanding and practical examples
- Build intuition before diving into formal proofs
- Use plain language explanations accessible to learners
- Mathematical rigor comes after understanding "why"

### Content Structure

When creating solutions, follow this order:

1. **Problem Statement** - Quote the exact problem from the book
2. **Intuitive Explanation** - Explain the "why" in plain language with concrete examples
3. **Approach/Strategy** - Describe the solution approach
4. **Detailed Solution** - Step-by-step walkthrough
5. **Mathematical Analysis** - Formal proofs, complexity analysis (if needed)
6. **Implementation** - Code examples (if applicable)
7. **Edge Cases/Insights** - Use aside boxes for additional observations

### Writing Style

**Natural Flow - No Artificial Subheadings:**
- **DO NOT use subheadings like "Intuition:", "Recurrence:", "Solution:"**
- **DO NOT use em-dashes (—)** - use commas, parentheses, or split into separate sentences
- Let the text flow naturally in paragraph form
- Start each method/part with intuitive explanation before equations
- Use concrete analogies (e.g., dictionary, cooking, traffic, bank etc.)
- Section headers for multi-part problems: "### A.", "### B." (not "### Part (a):")

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
- **Avoid bulleted lists with LaTeX** - use aligned equations instead
- Single-line equations use `$$...$$`

**Ads Placement:**
- Insert `{% include ads.html %}` for moderate to long solutions
- Place at natural content breaks (e.g., between major parts)
- For 2-part problems: after Part A, possibly after Part B if content is long
- For 3+ part problems: after every 1-2 parts depending on length
- Reference: `_solutions/02/P02-02.md` and `_solutions/04/P04-02.md` for examples

### External Links

- **Optional but valuable** - Link to external resources for key concepts
- **Maximum 1-2 links per solution** - Only for concepts not fully explained in CLRS
- **Preferred sources**: Wikipedia, academic papers, authoritative tutorials
- **Link format**: Always append `{:target="_blank"}` to open in new tab
  ```markdown
  [convex hull](https://en.wikipedia.org/wiki/Convex_hull){:target="_blank"}
  ```
- **Link placement**: Within explanation text or in aside boxes

### File Naming and Front Matter

**Naming Convention:**
- Exercises: `E[chapter].[section]-[number].md` (e.g., `E05.01-01.md`)
- Problems: `P[chapter]-[number].md` (e.g., `P05-01.md`)
- Appendix: `EA.[section]-[number].md` (e.g., `EA.01-01.md`)

**Front Matter Template:**
```yaml
---
title:       Exercise X.Y-Z
published:   YYYY-MM-DD HH:MM
modified:    YYYY-MM-DD HH:MM
keywords:    "key, concepts, comma, separated"
description: "The exact problem statement from the book"
---
```

### Code Guidelines

**Interactive Python Code:**
- Store in `_includes/code/[chapter]/code_E[chapter][section][number].py`
- Must be Skulpt-compatible (runs in browser)
- Include test cases and example outputs
- Add comments explaining key steps
- Show practical examples, not just algorithm implementation

**Pseudocode:**
- Use CLRS convention (small caps for procedure names)
- Use `{% capture code %}...{% endcapture %}` and `{% include clrs_code.html %}`
- Keep it readable and close to the book's style

### Visual Elements

**Asides (Side boxes):**
Use for additional insights, edge cases, "why" explanations, or interesting observations:
```markdown
{% capture note %}
Content here...
{% endcapture %}
{% include aside.html title='Box Title' %}
```

Examples of good aside titles:
- "Why did we end up with linear time?"
- "How bad is this?"
- "Why is Method 3 okay for merge sort?"
- "Why This Matters"

**LaTeX Math:**
- Use `$$...$$ ` for display math (block)
- Use `$$...$$` for inline math
- **Use `\begin{align*}...\end{align*}` for multi-step derivations**
- Use `\textsc{ProcedureName}` for procedure names in text
- Use `\bm{variable}` for bold variables

### Quality Checklist

Before considering a solution complete:

- [ ] Problem statement quoted correctly and completely
- [ ] **Intuitive explanation provided FIRST** (before mathematics)
- [ ] Concrete examples and analogies used
- [ ] **No artificial subheadings** like "Intuition:", "Recurrence:", "Solution:"
- [ ] **No em-dashes (—)** - use commas, parentheses, or split sentences
- [ ] Section headers use "### A.", "### B." format (not "### Part (a):")
- [ ] Multi-step equations use `\begin{align*}...\end{align*}`
- [ ] **Ads inserted at natural breaks** for moderate/long solutions
- [ ] Solution is technically correct
- [ ] Code tested (if applicable)
- [ ] Images generated
- [ ] External links use `{:target="_blank"}` (if any)
- [ ] Follows established tone and style
- [ ] No assumptions about advanced CS background
- [ ] Cross-references to related exercises (if relevant)

## Code Execution

Solutions can include interactive Python code blocks that execute in the browser via Skulpt. Code files are stored in `_includes/code/[chapter]/` and embedded using the `clrs_code.html` include.

## Image Generation

Each solution requires a corresponding social media preview image. Images are generated using the `utils/GenerateImage.py` utility.

### Fonts

The image generator uses fonts stored in `assets/fonts/`:
- **times.ttf** - Serif font for exercise titles
- **ariblk.ttf** - Bold sans-serif for headers and problem IDs

### Generating Images

The `utils/GenerateImage.py` module provides two main functions:

**CreateImage(chapter, section, problem_id)** - Standard image generation
```python
from GenerateImage import CreateImage

# Generate Exercise 5.1-2 image
CreateImage(chapter=5, section=1, problem_id=2)

# Generate Problem 5-3 image (section=0 for problems)
CreateImage(chapter=5, section=0, problem_id=3)
```

**CreateImageDirect(title, problem_title, location)** - Custom image generation
```python
from GenerateImage import CreateImageDirect

CreateImageDirect(
    title="Custom Title\nWith Line Breaks",
    problem_title="Exercise 4.4-1",
    location="assets/img/04/4.4-1.jpg"
)
```

**Batch Generation Scripts:**
```bash
# Generate all images for a chapter by creating a script in utils/
cd utils
python3 generate_ch5_images.py
```

Images are automatically saved to `assets/img/{chapter}/` with naming:
- Exercises: `{chapter}.{section}-{number}.jpg`
- Problems: `{chapter}-{number}.jpg`
- Dimensions: 1200x630 (optimized for social media previews)

## Slash Commands

The repository includes custom slash commands in `.claude/commands/` for common workflows:

### `/generate-solutions {chapter} {section}`

Generates complete solutions for a chapter/section including:
- Solution markdown files with intuition-first approach
- Python code implementations (Skulpt-compatible)
- Social media preview images
- Updates to `_data/toc.json` (if new chapter)
- Creates feature branch for the work

**Example:** `/generate-solutions 5 2` generates solutions for Chapter 5, Section 5.2

### `/review-solutions {chapter} {section}`

Performs comprehensive review of solutions for quality, correctness, and style:

**Mechanical Checks:**
- Files, images, and configuration
- Build verification
- Naming conventions

**Content Correctness:**
- Technical accuracy
- Code quality (if applicable)
- Problem statements

**Style & Pedagogy:**
- Intuition-first approach
- Natural writing flow (no artificial subheadings, no em-dashes)
- Mathematical formatting (`\begin{align*}`)
- Ads placement
- Asides and visual elements

**Reports findings categorized by:**
- ❌ Critical (must fix): build errors, incorrect solutions
- ⚠️ Important (should fix): missing intuition, wrong formatting
- 💡 Suggestions (nice to have): style improvements
- ✓ Strengths: what's working well

**Asks permission before making any changes**

**Example:** `/review-solutions 5 1` reviews Chapter 5, Section 5.1

All commands use the TodoWrite tool to track progress and provide detailed reports.
