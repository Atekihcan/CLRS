---
description: Review solutions against quality checklist and report findings
---

{% if {2} == 0 %}
Perform a comprehensive quality check on the solutions for **Chapter {1} Problems**.
{% else %}
Perform a comprehensive quality check on the solutions for **Chapter {1}, Section {2}**.
{% endif %}

## Quality Checklist:

### Content Quality:
- [ ] Problem statements quoted exactly from book
- [ ] Intuitive explanation provided BEFORE mathematical analysis
- [ ] Solutions are technically correct
- [ ] Explanations accessible (no assumption of advanced CS background)
- [ ] External links added where helpful (max 1-2, with `{:target="_blank"}`)
- [ ] Cross-references to related exercises (if applicable)

### Code Quality:
- [ ] Python code is Skulpt-compatible
- [ ] Test cases included and working
- [ ] Comments explain key steps
- [ ] Code properly referenced in solution markdown

### Formatting:
- [ ] LaTeX renders correctly (use `$$...$$ ` for display, `$$...$$` for inline)
- [ ] Asides used appropriately for insights/edge cases
- [ ] Front matter complete (title, dates, keywords, description)
- [ ] Proper markdown formatting

### Images:
- [ ] All images exist in `assets/img/{1:02d}/`
- [ ] Images are ~35-45 KB each
{% if {2} == 0 %}
- [ ] Naming convention for problems: `{1}-N.jpg` (no section number)
{% else %}
- [ ] Naming convention for exercises: `{1}.{2}-N.jpg`
{% endif %}

### Configuration:
- [ ] `_data/toc.json` updated correctly
{% if {2} == 0 %}
- [ ] Problem count is accurate
{% else %}
- [ ] Section name matches book exactly
- [ ] Exercise count is accurate
{% endif %}

## Process:

{% if {2} == 0 %}
1. Read all problem solution files for Chapter {1} (P{1:02d}-*.md)
{% else %}
1. Read all solution files for Chapter {1}, Section {2} (E{1:02d}.{2:02d}-*.md)
{% endif %}
2. Check each item in the checklist
3. **Report all findings** - both issues and good practices
4. Build site locally to verify: `./build.sh`
5. Report any build errors

## Important:

**DO NOT make changes automatically.** If issues are found:
- Clearly list all problems discovered
- Categorize by severity (critical, important, minor, nitpicky)
- Provide specific recommendations
- **Ask for explicit permission** before making any changes
- Let the user decide which issues to fix

## Report Format:

Provide a detailed report covering:
- ✓ Items that pass the checklist
- ✗ Issues found (categorized by severity)
- Specific recommendations for improvements
- Build verification results
- Ask: "Would you like me to fix any of these issues?"

Use TodoWrite to track progress through the checklist.
