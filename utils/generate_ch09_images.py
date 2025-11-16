#!/usr/bin/env python3
"""Generate all images for Chapter 9 solutions."""

import sys
sys.path.append('/home/user/CLRS/utils')

from GenerateImage import CreateImage

# Chapter 9: Medians and Order Statistics

# Section 9.1: Minimum and maximum
CreateImage(chapter=9, section=1, problem_id=1)
CreateImage(chapter=9, section=1, problem_id=2)

# Section 9.2: Selection in expected linear time
CreateImage(chapter=9, section=2, problem_id=1)
CreateImage(chapter=9, section=2, problem_id=2)
CreateImage(chapter=9, section=2, problem_id=3)
CreateImage(chapter=9, section=2, problem_id=4)

# Section 9.3: Selection in worst-case linear time
CreateImage(chapter=9, section=3, problem_id=1)
CreateImage(chapter=9, section=3, problem_id=2)
CreateImage(chapter=9, section=3, problem_id=3)
CreateImage(chapter=9, section=3, problem_id=4)
CreateImage(chapter=9, section=3, problem_id=5)
CreateImage(chapter=9, section=3, problem_id=6)
CreateImage(chapter=9, section=3, problem_id=7)
CreateImage(chapter=9, section=3, problem_id=8)
CreateImage(chapter=9, section=3, problem_id=9)

# Problems
CreateImage(chapter=9, section=0, problem_id=1)
CreateImage(chapter=9, section=0, problem_id=2)
CreateImage(chapter=9, section=0, problem_id=3)
CreateImage(chapter=9, section=0, problem_id=4)

print("All images for Chapter 9 generated successfully!")
