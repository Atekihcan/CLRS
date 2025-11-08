#!/usr/bin/env python3
"""Generate images for Chapter 5, Section 5.1 exercises"""

from GenerateImage import CreateImage

# Chapter 5, Section 5.1 - The Hiring Problem (3 exercises)
chapter = 5
section = 1

for problem_id in range(1, 4):  # Exercises 5.1-1, 5.1-2, 5.1-3
    CreateImage(chapter, section, problem_id)
    print(f"Generated image for Exercise {chapter}.{section}-{problem_id}")

print("\nAll images generated successfully!")
