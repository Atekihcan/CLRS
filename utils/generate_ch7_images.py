#!/usr/bin/env python3
"""Generate all social media preview images for Chapter 7 solutions."""

from GenerateImage import CreateImage

# Chapter 7: Quicksort

# Section 7.1: Description of quicksort (4 exercises)
for i in range(1, 5):
    CreateImage(chapter=7, section=1, problem_id=i)

# Section 7.2: Performance of quicksort (6 exercises)
for i in range(1, 7):
    CreateImage(chapter=7, section=2, problem_id=i)

# Section 7.3: A randomized version of quicksort (2 exercises)
for i in range(1, 3):
    CreateImage(chapter=7, section=3, problem_id=i)

# Section 7.4: Analysis of quicksort (6 exercises)
for i in range(1, 7):
    CreateImage(chapter=7, section=4, problem_id=i)

# Problems (6 problems)
for i in range(1, 7):
    CreateImage(chapter=7, section=0, problem_id=i)

print("✓ Generated all 24 images for Chapter 7")
