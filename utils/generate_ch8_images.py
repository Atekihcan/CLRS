#!/usr/bin/env python3

from GenerateImage import CreateImage

# Chapter 8 - Sorting in Linear Time

# Section 8.1 exercises (4)
for i in range(1, 5):
    CreateImage(chapter=8, section=1, problem_id=i)

# Section 8.2 exercises (4)
for i in range(1, 5):
    CreateImage(chapter=8, section=2, problem_id=i)

# Section 8.3 exercises (5)
for i in range(1, 6):
    CreateImage(chapter=8, section=3, problem_id=i)

# Section 8.4 exercises (5)
for i in range(1, 6):
    CreateImage(chapter=8, section=4, problem_id=i)

# Problems (7)
for i in range(1, 8):
    CreateImage(chapter=8, section=0, problem_id=i)

print("All Chapter 8 images generated successfully!")
