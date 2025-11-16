---
description: Review solutions for quality, correctness, and style
---

{% if {2} == 0 %}
Perform a comprehensive review of solutions for **Chapter {1} Problems**.
{% else %}
Perform a comprehensive review of solutions for **Chapter {1}, Section {2}**.
{% endif %}

## Review Process:

{% if {2} == 0 %}
1. Read all problem solution files for Chapter {1} (P{1:02d}-*.md)
{% else %}
1. Read all solution files for Chapter {1}, Section {2} (E{1:02d}.{2:02d}-*.md)
{% endif %}
2. Check each category below
3. Build site locally to verify: `./build.sh`
4. Report findings categorized by severity
5. **Ask for permission before making any changes**

## Review Categories:

### 1. Mechanical Checks (Pass/Fail)

**Files & Configuration:**
- [ ] All solution files exist with correct naming convention
{% if {2} == 0 %}
- [ ] Naming: `P{1:02d}-NN.md` for problems
- [ ] Images exist: `assets/img/{1:02d}/{1}-N.jpg` (no section number)
{% else %}
- [ ] Naming: `E{1:02d}.{2:02d}-NN.md` for exercises
- [ ] Images exist: `assets/img/{1:02d}/{1}.{2}-N.jpg`
{% endif %}
- [ ] Images are ~30-75 KB each
- [ ] `_data/toc.json` updated correctly
{% if {2} == 0 %}
- [ ] Problem count matches actual number of solutions
{% else %}
- [ ] Section name matches book exactly
- [ ] Exercise count matches actual number of solutions
{% endif %}

**Build Verification:**
- [ ] Site builds without errors (`./build.sh`)
- [ ] No broken links or missing references
- [ ] LaTeX renders correctly

**Front Matter:**
- [ ] All files have complete YAML front matter
- [ ] Title format correct
- [ ] Description contains full problem statement
- [ ] Keywords appropriate

### 2. Content Correctness

**Technical Accuracy (CRITICAL - Verify Each Solution):**
- [ ] Problem statements quoted exactly and completely from book
- [ ] **Final answers are correct** (verify all results independently)
- [ ] **Mathematical/algorithmic reasoning is sound:**
  - [ ] All equations and derivations are correct
  - [ ] Verify solutions by substitution or alternative methods when possible
  - [ ] Summations and series calculated correctly
  - [ ] Inequalities and bounds properly justified
  - [ ] Proofs are logically sound and complete
- [ ] **Techniques are accessible to readers at this point in the book:**
  - [ ] Only uses methods covered in CLRS up to this chapter
  - [ ] Advanced techniques (beyond CLRS scope) are in aside boxes with links
  - [ ] References to CLRS equations/theorems are accurate (e.g., "equation (A.7)")
  - [ ] External methods hyperlinked to authoritative sources (Wikipedia, papers)
- [ ] Edge cases and special cases handled appropriately
- [ ] No logical gaps in reasoning

**Code Quality (if applicable):**
- [ ] Python code is Skulpt-compatible
- [ ] Test cases included and working
- [ ] Code produces correct output
- [ ] Comments explain key steps
- [ ] Code properly referenced in solution markdown
- [ ] Practical examples, not just algorithm skeleton
- [ ] **Code performance is optimized for browser execution:**
  - [ ] Default execution completes in < 0.5 seconds (no browser freeze)
  - [ ] Simulation trials: 500-1000 (not 10,000+)
  - [ ] Test sizes: 2-3 examples (not 5-6)
  - [ ] Individual examples: 3-5 iterations (not 10+)
- [ ] **No orphaned code files** - all .py files in `_includes/code/` are referenced in solution markdown
- [ ] Code files only created when they enhance understanding (simulations, randomized algorithms)
- [ ] Code integrated at end of solution with `### Interactive Simulation` section

### 3. Style & Pedagogy

**Intuition-First Approach (Top Priority):**
- [ ] **Intuitive explanation provided BEFORE mathematical analysis**
- [ ] Concrete examples and analogies used (dictionary, cooking, traffic, etc.)
- [ ] Builds progressive understanding
- [ ] Accessible to learners (no assumption of advanced CS background)
- [ ] Explains "why" not just "what"

**Writing Style:**
- [ ] **NO artificial subheadings** like "Intuition:", "Recurrence:", "Solution:"
- [ ] **NO em-dashes (—)** - uses commas, parentheses, or split sentences
- [ ] Text flows naturally in paragraph form
- [ ] Section headers use "### A", "### B" format (not "### Part (a):")
- [ ] Each method/part starts with intuitive explanation before equations

**Pseudocode Formatting:**
- [ ] **Code blocks use plain text - NO LaTeX inside `{% capture code %}`:**
  - [ ] No `$$...$$`, `\textsc`, `\textit`, `**bold**` inside code blocks
  - [ ] Use plain text: `n = A.length`, `Random(1, n)`, `if x ≠ y`
  - [ ] Reference: Check code blocks don't have LaTeX formatting
- [ ] **Pseudocode in blockquotes uses proper pattern:**
  - [ ] Code defined BEFORE blockquote with `{% capture code %}`
  - [ ] Included inside blockquote with `{%- include clrs_code.html title="..." -%}`
  - [ ] **NO hardcoded LaTeX pseudocode** like `> $$\textsc{Procedure}$$($$A$$)` with line numbers
  - [ ] Reference: `_solutions/02/P02-02.md` for correct pattern

**Mathematical Formatting:**
- [ ] **Multi-step equations use `\begin{align*}...\end{align*}`** (not bulleted lists)
- [ ] Single-line equations use `$$...$$`
- [ ] Proper use of `\Theta`, `\Omega`, `O` notation
- [ ] LaTeX formatting is clean and readable

**Ads Placement:**
- [ ] **Moderate to long solutions include `{% include ads.html %}`**
- [ ] Ads placed at natural content breaks (between major parts)
- [ ] For 2-part problems: after Part A, possibly after Part B if long
- [ ] For 3+ part problems: after every 1-2 parts

**Visual Elements:**
- [ ] Asides used for "why" explanations, insights, edge cases
- [ ] Aside titles are descriptive ("Why linear time?", "How bad is this?")
- [ ] Tables formatted properly (if used)
- [ ] Diagrams/images referenced appropriately

**External Links (if any):**
- [ ] Maximum 1-2 links per solution
- [ ] Only for concepts not fully explained in CLRS
- [ ] Using `{:target="_blank"}` format
- [ ] Links to authoritative sources (Wikipedia, academic papers)

**Cross-References:**
- [ ] Related exercises referenced when relevant
- [ ] References use correct format with Jekyll links

### 4. Consistency

{% if {2} == 0 %}
- [ ] All problems follow similar structure and style
- [ ] Tone and approach consistent across problems
- [ ] Formatting conventions uniform
{% else %}
- [ ] All exercises follow similar structure and style
- [ ] Tone and approach consistent across exercises
- [ ] Formatting conventions uniform
{% endif %}

## Report Format:

Provide a detailed report with findings categorized by severity:

### ❌ Critical Issues (Must Fix)
- Build errors
- Incorrect solutions
- Missing files
- Broken configuration

### ⚠️ Important Issues (Should Fix)
- Missing intuition or intuition comes after math
- Artificial subheadings ("Intuition:", etc.)
- Em-dashes present
- Wrong equation formatting (bullets instead of `\begin{align*}`)
- Missing ads in long solutions
- Wrong section headers ("Part (a)" instead of "A")
- Hardcoded LaTeX pseudocode in blockquotes (should use `{% capture code %}` pattern)
- LaTeX formatting inside `{% capture code %}` blocks (should be plain text)
- Code performance issues (execution > 0.5s, too many trials/examples)
- Orphaned code files not referenced in markdown
- Code created for problems that don't benefit from simulation

### 💡 Suggestions (Nice to Have)
- Could use better analogies
- Could add more concrete examples
- Could improve aside usage
- Minor wording improvements
- Additional cross-references

### ✓ Strengths
- What's working well
- Good practices to maintain
- Exemplary sections

## Important:

**DO NOT make changes automatically.** After providing the report:
1. Clearly list all issues discovered
2. Provide specific recommendations with examples
3. Show before/after for suggested changes
4. **Ask: "Would you like me to fix any of these issues?"**
5. Let the user decide which issues to address

Use TodoWrite to track progress through the review checklist.
