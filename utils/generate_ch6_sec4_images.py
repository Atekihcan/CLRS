#!/usr/bin/env python3
"""Generate images for Chapter 6, Section 6.4 exercises."""

import sys
import os

# Add the utils directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from GenerateImage import CreateImage

def main():
    """Generate all images for Chapter 6, Section 6.4."""
    chapter = 6
    section = 4

    # Generate images for exercises 6.4-1 through 6.4-5
    for exercise_num in range(1, 6):
        print(f"Generating image for Exercise {chapter}.{section}-{exercise_num}...")
        CreateImage(chapter=chapter, section=section, problem_id=exercise_num)
        print(f"  ✓ Created assets/img/06/6.{section}-{exercise_num}.jpg")

    print("\nAll images generated successfully!")

if __name__ == "__main__":
    main()
