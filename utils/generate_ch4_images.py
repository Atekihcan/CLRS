#!/usr/bin/env python3
"""Generate images for Chapter 4 Problems"""

from GenerateImage import CreateImage

# Chapter 4 Problems (section = 0 for problems, not exercises)
chapter = 4
section = 0  # 0 indicates these are problems, not section exercises

# Generate images for all 6 problems
for problem_id in range(1, 7):  # Problems 4-1 through 4-6
    CreateImage(chapter, section, problem_id)
    print(f"Generated image for Problem {chapter}-{problem_id}")

print("\nAll Chapter 4 problem images generated successfully!")
