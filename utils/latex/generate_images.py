#!/usr/bin/env python3
"""
LaTeX Image Generation Script for CLRS Solutions

Compiles LaTeX files and generates PNG images for use in solution documentation.
Automatically infers chapter numbers and suggests appropriate image names.

Usage:
    python3 generate_images.py <latex-file.tex>
    python3 generate_images.py E06.05-01.tex
    python3 generate_images.py P12-03.tex --auto
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple


class Colors:
    """ANSI color codes for terminal output"""

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    NC = "\033[0m"  # No Color


def print_error(msg: str) -> None:
    """Print error message in red"""
    print(f"{Colors.RED}✗ {msg}{Colors.NC}", file=sys.stderr)


def print_success(msg: str) -> None:
    """Print success message in green"""
    print(f"{Colors.GREEN}✓ {msg}{Colors.NC}")


def print_info(msg: str) -> None:
    """Print info message in blue"""
    print(f"{Colors.BLUE}→ {msg}{Colors.NC}")


def print_warning(msg: str) -> None:
    """Print warning message in yellow"""
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.NC}")


def parse_filename(filename: str) -> Tuple[Optional[str], Optional[str], str]:
    """
    Parse LaTeX filename to extract chapter, type, and reference.

    Examples:
        E06.05-01.tex -> ('06', 'E', '06.05-01')
        P12-03.tex -> ('12', 'P', '12-03')

    Returns:
        (chapter, type, reference) tuple
    """
    basename = Path(filename).stem

    # Exercise pattern: E[chapter].[section]-[number]
    match = re.match(r"^E(\d+)\.(\d+)-(\d+)$", basename)
    if match:
        chapter = match.group(1)
        reference = f"{chapter}.{match.group(2)}-{match.group(3)}"
        return chapter, "E", reference

    # Problem pattern: P[chapter]-[number]
    match = re.match(r"^P(\d+)-(\d+)$", basename)
    if match:
        chapter = match.group(1)
        reference = f"{chapter}-{match.group(2)}"
        return chapter, "P", reference

    return None, None, basename


def suggest_image_base(chapter: str, file_type: str, reference: str) -> str:
    """
    Suggest a base name for images based on the filename components.

    Examples:
        ('06', 'E', '06.05-01') -> '6.5-1'
        ('12', 'P', '12-03') -> '12-3'
    """
    if file_type == "E":
        # Exercise: E06.05-01 -> 6.5-1
        match = re.match(r"(\d+)\.(\d+)-(\d+)", reference)
        if match:
            ch, sec, num = match.groups()
            return f"{int(ch)}.{int(sec)}-{int(num)}"
    elif file_type == "P":
        # Problem: P12-03 -> 12-3
        match = re.match(r"(\d+)-(\d+)", reference)
        if match:
            ch, num = match.groups()
            return f"{int(ch)}-{int(num)}"

    return reference.lower()


def get_project_root() -> Path:
    """
    Get the project root directory (CLRS directory).
    Script is located at: CLRS/utils/latex/generate_images.py
    """
    # Get the directory where this script is located
    script_dir = Path(__file__).resolve().parent
    # Go up two levels to get to project root: utils/latex -> utils -> CLRS
    project_root = script_dir.parent.parent
    return project_root


def compile_latex(latex_file: Path, output_dir: Path) -> bool:
    """
    Compile LaTeX file to PDF.

    Returns:
        True if successful, False otherwise
    """
    print_info(f"Compiling {latex_file.name} to PDF...")

    try:
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", f"-output-directory={output_dir}", str(latex_file)], capture_output=True, text=True, timeout=60
        )

        if result.returncode != 0:
            print_error("LaTeX compilation failed")
            log_file = output_dir / f"{latex_file.stem}.log"
            print_error(f"Check {log_file} for details")
            return False

        pdf_file = output_dir / f"{latex_file.stem}.pdf"
        if not pdf_file.exists():
            print_error(f"PDF file not generated: {pdf_file}")
            return False

        print_success(f"PDF generated: {pdf_file}")
        return True

    except FileNotFoundError:
        print_error("pdflatex not found. Please install a TeX distribution.")
        return False
    except subprocess.TimeoutExpired:
        print_error("LaTeX compilation timed out (60s limit)")
        return False
    except Exception as e:
        print_error(f"Compilation error: {e}")
        return False


def convert_to_png(pdf_file: Path, output_prefix: str, dpi: int = 300) -> List[Path]:
    """
    Convert PDF pages to PNG images.

    Returns:
        List of generated PNG file paths
    """
    print_info(f"Converting PDF to PNG images ({dpi} DPI)...")

    try:
        result = subprocess.run(
            ["pdftoppm", "-png", "-r", str(dpi), pdf_file.name, output_prefix], cwd=pdf_file.parent, capture_output=True, text=True, timeout=60
        )

        if result.returncode != 0:
            print_error("PDF to PNG conversion failed")
            print_error(result.stderr)
            return []

        # Find generated PNG files
        png_files = sorted(pdf_file.parent.glob(f"{pdf_file.stem}-*.png"))

        if not png_files:
            print_error("No PNG files generated")
            return []

        print_success(f"Generated {len(png_files)} image(s)")
        for png in png_files:
            size_kb = png.stat().st_size / 1024
            print(f"  {png.name} ({size_kb:.1f} KB)")

        return png_files

    except FileNotFoundError:
        print_error("pdftoppm not found. Please run: brew install poppler")
        return []
    except subprocess.TimeoutExpired:
        print_error("PNG conversion timed out (60s limit)")
        return []
    except Exception as e:
        print_error(f"Conversion error: {e}")
        return []


def copy_images(png_files: List[Path], chapter: str, base_name: str, custom_names: Optional[List[str]] = None, auto: bool = False) -> bool:
    """
    Copy PNG images to assets directory with appropriate names.

    Returns:
        True if successful, False otherwise
    """
    import shutil

    # Get project root and create absolute path to assets directory
    project_root = get_project_root()
    assets_dir = project_root / "assets" / "img" / chapter
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Calculate relative path for display
    rel_assets_path = f"assets/img/{chapter}/"

    if not auto:
        print()
        print_info(f"Generated images will be copied to: {rel_assets_path}")
        print_info(f"Full path: {assets_dir}")
        print()

        # Ask user for confirmation
        response = input(f"Copy images to {rel_assets_path}? (y/n): ").strip().lower()
        if response not in ("y", "yes"):
            print_warning("Images remain in: utils/latex/_out/")
            return False

        # Ask for naming preference
        print()
        print(f"Suggested base name: {base_name}")
        print("Options:")
        print("  1. Press Enter to use suggested name")
        print("  2. Enter a custom base name (e.g., '6.5-1')")
        print("  3. Enter comma-separated names for each image")
        print()

        user_input = input("Your choice: ").strip()

        if user_input:
            if "," in user_input:
                custom_names = [name.strip() for name in user_input.split(",")]
            else:
                base_name = user_input

    # Copy files with appropriate names
    copied_files: List[Path] = []

    if custom_names:
        # Use custom names
        for png_file, name in zip(png_files, custom_names):
            if not name.endswith(".png"):
                name += ".png"
            dest: Path = assets_dir / name

            try:
                shutil.copy2(png_file, dest)
                print_success(f"Copied {png_file.name} -> {dest}")
                copied_files.append(dest)
            except Exception as e:
                print_error(f"Failed to copy {png_file.name}: {e}")
                return False
    else:
        # Use step naming or single file
        if len(png_files) == 1:
            # Single image
            dest: Path = assets_dir / f"{base_name}.png"
            try:
                shutil.copy2(png_files[0], dest)
                print_success(f"Copied {png_files[0].name} -> {dest}")
                copied_files.append(dest)
            except Exception as e:
                print_error(f"Failed to copy {png_files[0].name}: {e}")
                return False
        else:
            # Multiple images with step numbering
            for i, png_file in enumerate(png_files, 1):
                dest: Path = assets_dir / f"{base_name}_step_{i}.png"
                try:
                    shutil.copy2(png_file, dest)
                    print_success(f"Copied {png_file.name} -> {dest}")
                    copied_files.append(dest)
                except Exception as e:
                    print_error(f"Failed to copy {png_file.name}: {e}")
                    return False

    print()
    print_success(f"Images copied to {rel_assets_path}")
    print()
    print("Images in assets:")
    copied_file: Path
    for copied_file in copied_files:
        size_kb: float = copied_file.stat().st_size / 1024
        print(f"  {copied_file.name} ({size_kb:.1f} KB)")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate PNG images from LaTeX visualizations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s E06.05-01.tex
  %(prog)s P12-03.tex --auto
  %(prog)s E06.05-01.tex --dpi 600
        """,
    )

    parser.add_argument("latex_file", help="LaTeX file to compile (.tex)")
    parser.add_argument("--chapter", help="Override chapter number (auto-detected from filename)")
    parser.add_argument("--dpi", type=int, default=300, help="Image resolution (default: 300)")
    parser.add_argument("--auto", action="store_true", help="Skip interactive prompts (use defaults)")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # Validate input file
    latex_file = Path(args.latex_file)
    if not latex_file.exists():
        print_error(f"File not found: {latex_file}")
        sys.exit(1)

    if latex_file.suffix != ".tex":
        print_error(f"File must have .tex extension: {latex_file}")
        sys.exit(1)

    # Parse filename
    chapter, file_type, reference = parse_filename(latex_file.name)

    # Override chapter if specified
    if args.chapter:
        chapter = args.chapter.zfill(2)  # Zero-pad to 2 digits

    if not chapter:
        print_error("Could not determine chapter number from filename")
        print_error("Filename must follow format: E[chapter].[section]-[number].tex or P[chapter]-[number].tex")
        print_error("Examples: E06.05-01.tex, P12-03.tex")
        sys.exit(1)

    # file_type should not be None at this point if chapter is not None
    if not file_type:
        print_error("Could not determine file type from filename")
        sys.exit(1)

    # Suggest image base name
    suggested_base = suggest_image_base(chapter, file_type, reference)

    if args.verbose:
        print_info(f"Chapter: {chapter}")
        print_info(f"Type: {'Exercise' if file_type == 'E' else 'Problem'}")
        print_info(f"Reference: {reference}")
        print_info(f"Suggested base name: {suggested_base}")
        print()

    # Create output directory in utils/latex/_out
    output_dir = Path("_out")
    output_dir.mkdir(exist_ok=True)

    # Step 1: Compile LaTeX
    if not compile_latex(latex_file, output_dir):
        sys.exit(1)

    # Step 2: Convert to PNG
    pdf_file = output_dir / f"{latex_file.stem}.pdf"
    png_files = convert_to_png(pdf_file, latex_file.stem, args.dpi)

    if not png_files:
        sys.exit(1)

    # Step 3: Copy to assets
    if copy_images(png_files, chapter, suggested_base, auto=args.auto):
        print()
        print_success("Done!")
        print()
        print("Next steps:")
        print("1. Verify images look correct")
        print("2. Update solution markdown files with image references:")
        print(f"   ![Description]({{{{ '/assets/img/{chapter}/{suggested_base}_step_1.png' | prepend: site.baseurl }}}} \"Alt text\")")
        print("3. Run ./build.sh to verify the site builds correctly")
    else:
        print()
        print_info("Images remain in: utils/latex/_out/")
        print_info("You can manually copy them when ready")


if __name__ == "__main__":
    main()
