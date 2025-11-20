# LaTeX Visualization Workflow

This directory contains LaTeX files for generating visualizations (diagrams, graphs, trees, etc.) used in CLRS solutions.

## Quick Start

```bash
cd utils/latex
python3 generate_images.py E06.05-01.tex
```

The script will:

1. Auto-detect chapter number from filename
2. Compile LaTeX to PDF
3. Convert PDF pages to PNG images (300 DPI)
4. Suggest appropriate image names
5. Guide you through copying to assets directory

## Directory Structure

```text
utils/latex/
├── README.md              # This file
├── generate_images.py     # Python script to compile LaTeX and generate PNGs
├── _out/                  # Temporary output directory (PDFs, aux, log files)
└── *.tex                  # LaTeX source files
```

## Prerequisites

1. **pdflatex** - Part of a TeX distribution (MacTeX, TeX Live)

   ```bash
   which pdflatex
   # Should output something like: /usr/local/texlive/2025/bin/universal-darwin/pdflatex
   ```

2. **poppler** (for pdftoppm) - Install via Homebrew

   ```bash
   brew install poppler
   ```

3. **Python 3** - Should be pre-installed on macOS

   ```bash
   python3 --version
   ```

## File Naming Convention

LaTeX files must follow the same naming pattern as solution files:

**Examples:**

- Exercises: `E06.05-01.tex` (Exercise 6.5-1)
- Problems: `P06-01.tex` (Problem 6-1)

**Naming Rules:**

- For exercises: `E[chapter].[section]-[number].tex` (e.g., `E06.05-01.tex`, `E12.03-05.tex`)
- For problems: `P[chapter]-[number].tex` (e.g., `P06-01.tex`, `P15-02.tex`)

The chapter number determines where images will be saved (`assets/img/[chapter]/`).

## Image Naming

The script automatically suggests image names based on the LaTeX filename:

| Filename | Chapter | Suggested Base | Output Files |
|----------|---------|----------------|--------------|
| `E06.05-01.tex` | 06 | `6.5-1` | `6.5-1_step_1.png`, `6.5-1_step_2.png`, ... |
| `P12-03.tex` | 12 | `12-3` | `12-3_step_1.png` or custom names |
| `E15.04-02.tex` | 15 | `15.4-2` | `15.4-2_step_1.png`, ... |

## Complete Workflow

### 1. Create LaTeX File

Create a new `.tex` file in `utils/latex/` following the naming convention.

**Basic Template:**

```latex
\documentclass[tikz,border=5pt]{standalone}
\usepackage{tikz}
% Add other packages as needed

\begin{document}

% First visualization
\begin{tikzpicture}
% Your LaTeX/TikZ code here
\end{tikzpicture}

\newpage  % Use \newpage to separate multiple visualizations

% Second visualization (optional)
\begin{tikzpicture}
% Your LaTeX/TikZ code here
\end{tikzpicture}

\end{document}
```

**Key Points:**

- Use `\documentclass{standalone}` for self-contained images
- Use `\newpage` to separate different visualizations (each becomes a separate image)
- Keep styling consistent with existing files
- Add comments to explain complex structures

### 2. Generate Images

**Using the Python script (recommended):**

```bash
cd utils/latex
python3 generate_images.py E06.05-01.tex
```

**Example Session:**

```bash
$ python3 generate_images.py E06.05-01.tex

→ Compiling E06.05-01.tex to PDF...
✓ PDF generated: _out/E06.05-01.pdf

→ Converting PDF to PNG images (300 DPI)...
✓ Generated 5 image(s)
  E06.05-01-1.png (45.2 KB)
  E06.05-01-2.png (42.1 KB)
  E06.05-01-3.png (42.3 KB)
  E06.05-01-4.png (42.0 KB)
  E06.05-01-5.png (42.1 KB)

→ Generated images will be copied to: assets/img/06/

Copy images to assets/img/06/? (y/n): y

Suggested base name: 6.5-1
Options:
  1. Press Enter to use suggested name
  2. Enter a custom base name (e.g., '6.5-1')
  3. Enter comma-separated names for each image

Your choice: [Press Enter]

✓ Copied E06.05-01-1.png -> ../../assets/img/06/6.5-1_step_1.png
✓ Copied E06.05-01-2.png -> ../../assets/img/06/6.5-1_step_2.png
✓ Copied E06.05-01-3.png -> ../../assets/img/06/6.5-1_step_3.png
✓ Copied E06.05-01-4.png -> ../../assets/img/06/6.5-1_step_4.png
✓ Copied E06.05-01-5.png -> ../../assets/img/06/6.5-1_step_5.png

✓ Images copied to assets/img/06/

✓ Done!

Next steps:
1. Verify images look correct
2. Update solution markdown files with image references
3. Run ./build.sh to verify the site builds correctly
```

**Manual compilation (alternative):**

```bash
cd utils/latex

# Compile LaTeX to PDF
pdflatex -interaction=nonstopmode -output-directory=_out E06.05-01.tex

# Convert PDF to PNG (300 DPI)
cd _out
pdftoppm -png -r 300 E06.05-01.pdf E06.05-01

# Copy with desired names
cp E06.05-01-1.png ../../assets/img/06/6.5-1_step_1.png
cp E06.05-01-2.png ../../assets/img/06/6.5-1_step_2.png
# ... etc
```

### 3. Update Solution Files

In the solution markdown file (e.g., `_solutions/06/E06.05-01.md`), add image references:

```markdown
![Description]({{ '/assets/img/06/6.5-1_step_1.png' | prepend: site.baseurl }} "Alt text")
```

**Format:** `![Alt text]({{ 'path' | prepend: site.baseurl }} "Title")`

### 4. Verify Build

Test that the site builds correctly:

```bash
cd ../..  # Back to project root
./build.sh
```

### 5. Clean Up

The `_out/` directory contains temporary files (.aux, .log, .pdf).

- These files are in `.gitignore` and won't be committed
- Keep them for debugging or delete to save space
- They'll be regenerated when needed

## Script Options

```bash
# Basic usage
python3 generate_images.py E06.05-01.tex

# Auto mode (skip prompts, use defaults)
python3 generate_images.py E06.05-01.tex --auto

# Custom DPI
python3 generate_images.py E06.05-01.tex --dpi 600

# Override chapter detection
python3 generate_images.py E06.05-01.tex --chapter 12

# Verbose output
python3 generate_images.py E06.05-01.tex --verbose

# See all options
python3 generate_images.py --help
```

## Custom Image Names

### Option 1: Custom Base Name

```bash
$ python3 generate_images.py P06-01.tex

# When prompted:
Suggested base name: 6-1
Your choice: 6-1_comparison

# Creates:
# - 6-1_comparison_step_1.png
# - 6-1_comparison_step_2.png
```

### Option 2: Individual Names (Comma-Separated)

```bash
$ python3 generate_images.py P06-01.tex

# When prompted:
Your choice: 6-1_build_max_heap,6-1_build_max_heap_prime

# Creates:
# - 6-1_build_max_heap.png
# - 6-1_build_max_heap_prime.png
```

## Common Use Cases

### Exercise with Multiple Steps

```bash
# File: E12.03-05.tex (5 states of an algorithm)
python3 generate_images.py E12.03-05.tex

# Auto-suggested: 12.3-5
# Creates: 12.3-5_step_1.png through 12.3-5_step_5.png
```

### Problem with Custom Visualizations

```bash
# File: P15-02.tex (comparison diagrams)
python3 generate_images.py P15-02.tex

# Custom names: 15-2_approach_a,15-2_approach_b,15-2_comparison
```

### Single-Image Exercise

```bash
# File: E08.01-03.tex (single diagram)
python3 generate_images.py E08.01-03.tex

# Auto-suggested: 8.1-3
# Creates: 8.1-3.png
```

## File Locations

- **LaTeX source**: `utils/latex/*.tex`
- **Temporary output**: `utils/latex/_out/` (gitignored)
- **Final images**: `assets/img/[chapter]/`
- **Solutions**: `_solutions/[chapter]/`

## Image Quality Settings

- **Resolution:** 300 DPI (good balance of quality and file size)
- **Format:** PNG (supports transparency, lossless compression)
- **Typical file size:** 10-50 KB per image depending on complexity

## Troubleshooting

### `pdftoppm: command not found`

```bash
brew install poppler
```

### LaTeX compilation errors

- Check for syntax errors in the `.tex` file
- View detailed errors in `_out/[filename].log`
- Ensure all required packages are installed

### Python script fails

```bash
# Check Python version (needs 3.6+)
python3 --version

# Run with verbose output
python3 generate_images.py filename.tex --verbose
```

### Images appear in wrong directory

- Check that filename follows naming convention
- Chapter number in filename determines output directory
- Manually specify chapter with `--chapter` flag if needed

### Can't find chapter number

```bash
# Use --chapter flag
python3 generate_images.py somefile.tex --chapter 08
```

### Need different DPI

```bash
# For higher quality (larger files)
python3 generate_images.py E06.05-01.tex --dpi 600

# For web-optimized (smaller files)
python3 generate_images.py E06.05-01.tex --dpi 150
```

### Layout/styling issues

- Review existing `.tex` files for reference
- Adjust dimensions, spacing, or styling in your LaTeX code
- Test compilation early and often

## Examples

See existing files for reference:

- `E06.05-01.tex` - Multiple states showing an operation
- `E06.05-02.tex` - Multi-step process visualization
- `P06-01.tex` - Simple comparison (small structures)

## Tips

1. **Test early** - Compile after creating the first visualization to catch errors
2. **Comment your code** - Explain what the visualization represents
3. **Consistent styling** - Copy style settings from existing files
4. **Preview images** - Check PNG output before updating solution files
5. **Use version control** - Commit working `.tex` files, images are auto-generated
6. **Descriptive names** - Use clear, meaningful names for custom visualizations
