"""
Image generation utility for CLRS solution social media previews.

This module generates 1200x630 preview images for exercises and problems
from the CLRS (Introduction to Algorithms) textbook. Each image includes:
- A purple header with "CLRS SOLUTIONS"
- The exercise/problem identifier
- The section/problem title from toc.json

Usage:
    from GenerateImage import CreateImage, CreateImageDirect

    # Generate an exercise image
    CreateImage(chapter=5, section=1, problem_id=2)

    # Generate a custom image
    CreateImageDirect(
        title="Custom Title\\nWith Line Breaks",
        problem_title="Exercise 1.1-1",
        location="assets/img/01/1.1-1.jpg"
    )

The images are automatically saved to assets/img/{chapter}/ with naming
convention: {chapter}.{section}-{problem_id}.jpg for exercises, or
{chapter}-{problem_id}.jpg for problems.
"""

import json
import os
from typing import Any, Union
from PIL import Image, ImageDraw, ImageFont

# Image dimensions
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630

# Color scheme
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (71, 41, 163)
COLOR_DARK_PURPLE = (45, 25, 120)
COLOR_BLACK = (0, 0, 0)

# Layout constants
HEADER_Y = 50
HEADER_HEIGHT = 70
TITLE_Y = 180
CONTENT_Y = 360
HEADER_WIDTH = 520

# Font sizes
FONT_SIZE_HEADER = 40
FONT_SIZE_TITLE = 52
FONT_SIZE_CONTENT = 120

# Get the base directory (repo root)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
fonts_dir = os.path.join(repo_root, "assets", "fonts")

# Load fonts from the repo's fonts directory
times_120 = ImageFont.truetype(os.path.join(fonts_dir, "times.ttf"), FONT_SIZE_CONTENT)
arial_black_40 = ImageFont.truetype(os.path.join(fonts_dir, "ariblk.ttf"), FONT_SIZE_HEADER)
arial_black_52 = ImageFont.truetype(os.path.join(fonts_dir, "ariblk.ttf"), FONT_SIZE_TITLE)

# Load TOC JSON
toc_path = os.path.join(repo_root, "_data", "toc.json")
with open(toc_path, encoding="utf-8") as f:
    toc_data: dict[str, Any] = json.load(f)


def _wrap_title(title: str, max_chars_per_line: int = 12) -> str:
    """
    Wrap a title string to fit within image bounds.

    Args:
        title: The title text to wrap
        max_chars_per_line: Maximum characters per line before wrapping

    Returns:
        Title with newlines inserted at appropriate positions
    """
    title_parts = title.split(" ")
    wrapped_title = ""
    num_chars = 0

    for part in title_parts:
        wrapped_title += part + " "
        num_chars += len(part)
        if num_chars > max_chars_per_line:
            num_chars = 0
            wrapped_title += "\n"

    return wrapped_title


def _draw_image_template(
    draw: ImageDraw.ImageDraw,
    problem_title: str,
    content_title: str
) -> None:
    """
    Draw the standard CLRS solution image template.

    Args:
        draw: PIL ImageDraw object to draw on
        problem_title: The exercise/problem identifier (e.g., "Exercise 5.1-2")
        content_title: The main content title to display
    """
    center_x = IMAGE_WIDTH / 2

    # Header background rectangle
    draw.rectangle(
        [center_x - HEADER_WIDTH/2, HEADER_Y, center_x + HEADER_WIDTH/2, HEADER_Y + HEADER_HEIGHT],
        fill=COLOR_PURPLE
    )

    # "CLRS SOLUTIONS" text
    draw.text(
        (center_x, HEADER_Y + HEADER_HEIGHT/2),
        "CLRS SOLUTIONS",
        font=arial_black_40,
        fill=COLOR_WHITE,
        anchor="ms"
    )

    # Problem/Exercise title
    draw.text(
        (center_x, TITLE_Y),
        problem_title,
        font=arial_black_52,
        fill=COLOR_DARK_PURPLE,
        anchor="ms"
    )

    # Border under header
    draw.rectangle(
        [center_x - HEADER_WIDTH/2, HEADER_Y + HEADER_HEIGHT, center_x + HEADER_WIDTH/2, HEADER_Y + 150],
        outline=COLOR_PURPLE,
        width=4
    )

    # Content title
    draw.text(
        (center_x, CONTENT_Y),
        content_title,
        font=times_120,
        fill=COLOR_BLACK,
        align="center",
        anchor="ms",
        spacing=20
    )


def CreateImageDirect(title: str, problem_title: str, location: str) -> None:
    """
    Create a custom CLRS solution image with direct title specification.

    Args:
        title: The main content title to display (can include \\n for line breaks)
        problem_title: The exercise/problem identifier (e.g., "Exercise 4.4-1")
        location: Full file path where the image should be saved

    Example:
        CreateImageDirect(
            title="Recursion-tree Method\\nfor Solving Recurrences",
            problem_title="Exercise 4.4-1",
            location="assets/img/04/4.4-1.jpg"
        )
    """
    # Create image
    img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color=COLOR_WHITE)
    draw = ImageDraw.Draw(img)

    # Draw template
    _draw_image_template(draw, problem_title, title)

    # Save image
    img.save(location)


def CreateImage(chapter: Union[int, str], section: int, problem_id: int) -> None:
    """
    Create a CLRS solution image using chapter/section metadata from toc.json.

    Args:
        chapter: Chapter number (int) or appendix letter (str, e.g., "A")
        section: Section number (use 0 for chapter problems vs section exercises)
        problem_id: The exercise/problem number within the section

    Example:
        # Generate image for Exercise 5.1-2
        CreateImage(chapter=5, section=1, problem_id=2)

        # Generate image for Problem 5-3
        CreateImage(chapter=5, section=0, problem_id=3)

        # Generate image for Appendix A Exercise A.1-1
        CreateImage(chapter="A", section=1, problem_id=1)

    The function automatically:
    - Looks up the section/problem title from _data/toc.json
    - Creates the output directory if needed
    - Saves to assets/img/{chapter}/ with correct naming convention
    """
    # Determine image folder
    if isinstance(chapter, int):
        image_folder = os.path.join(repo_root, "assets", "img", f"{chapter:02d}")
    else:
        image_folder = os.path.join(repo_root, "assets", "img", chapter)

    # Ensure output directory exists
    os.makedirs(image_folder, exist_ok=True)

    # Build problem title and look up content title
    title: str
    if section > 0:
        # Exercise (not a problem)
        problem_title = f"Exercise {chapter}.{section}-{problem_id}"
        image_filename = f"{chapter}.{section}-{problem_id}.jpg"

        if isinstance(chapter, int):
            title = str(toc_data["chapters"][chapter - 1]["sections"][section - 1]["name"])
        else:
            title = str(toc_data["appendices"][ord(chapter) - ord("A")]["sections"][section - 1]["name"])
    else:
        # Problem (section = 0)
        problem_title = f"Problem {chapter}-{problem_id}"
        image_filename = f"{chapter}-{problem_id}.jpg"

        if isinstance(chapter, int):
            title = str(toc_data["chapters"][chapter - 1]["problems"][problem_id - 1]["name"])
        else:
            title = str(toc_data["appendices"][ord(chapter) - ord("A")]["problems"][problem_id - 1]["name"])

    # Wrap title for display
    wrapped_title = _wrap_title(title)

    # Create image
    img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color=COLOR_WHITE)
    draw = ImageDraw.Draw(img)

    # Draw template
    _draw_image_template(draw, problem_title, wrapped_title)

    # Save image
    output_path = os.path.join(image_folder, image_filename)
    img.save(output_path)
