#!/usr/bin/env python3
"""Generate all images for Chapter 14 solutions."""

import sys
sys.path.append('/home/user/CLRS/utils')

from GenerateImage import CreateImage

# Generate images for Section 14.1 exercises
for i in range(1, 9):
    print(f"Generating image for Exercise 14.1-{i}")
    CreateImage(chapter=14, section=1, problem_id=i)

# Generate images for Section 14.2 exercises
for i in range(1, 5):
    print(f"Generating image for Exercise 14.2-{i}")
    CreateImage(chapter=14, section=2, problem_id=i)

# Generate images for Section 14.3 exercises
for i in range(1, 8):
    print(f"Generating image for Exercise 14.3-{i}")
    CreateImage(chapter=14, section=3, problem_id=i)

# Generate images for Problems
for i in range(1, 3):
    print(f"Generating image for Problem 14-{i}")
    CreateImage(chapter=14, section=0, problem_id=i)

print("All images generated successfully!")
