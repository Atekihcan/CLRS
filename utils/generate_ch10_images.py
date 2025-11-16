#!/usr/bin/env python3
"""Generate social media images for all Chapter 10 solutions."""

import sys
sys.path.append('/home/user/CLRS/utils')

from GenerateImage import CreateImage

# Section 10.1: Stacks and queues (7 exercises)
for i in range(1, 8):
    CreateImage(chapter=10, section=1, problem_id=i)
    print(f"Generated image for Exercise 10.1-{i}")

# Section 10.2: Linked lists (8 exercises)
for i in range(1, 9):
    CreateImage(chapter=10, section=2, problem_id=i)
    print(f"Generated image for Exercise 10.2-{i}")

# Section 10.3: Implementing pointers and objects (5 exercises)
for i in range(1, 6):
    CreateImage(chapter=10, section=3, problem_id=i)
    print(f"Generated image for Exercise 10.3-{i}")

# Section 10.4: Representing rooted trees (6 exercises)
for i in range(1, 7):
    CreateImage(chapter=10, section=4, problem_id=i)
    print(f"Generated image for Exercise 10.4-{i}")

# Problems (3 problems)
for i in range(1, 4):
    CreateImage(chapter=10, section=0, problem_id=i)
    print(f"Generated image for Problem 10-{i}")

print("\nAll Chapter 10 images generated successfully!")
