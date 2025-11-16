#!/usr/bin/env python3
"""Generate all social media images for Chapter 12 solutions."""

import sys
sys.path.append('/home/user/CLRS/utils')
from GenerateImage import CreateImage

# Section 12.1 - 5 exercises
for i in range(1, 6):
    CreateImage(chapter=12, section=1, problem_id=i)
    print(f"Generated E12.01-{i:02d}")

# Section 12.2 - 9 exercises
for i in range(1, 10):
    CreateImage(chapter=12, section=2, problem_id=i)
    print(f"Generated E12.02-{i:02d}")

# Section 12.3 - 6 exercises
for i in range(1, 7):
    CreateImage(chapter=12, section=3, problem_id=i)
    print(f"Generated E12.03-{i:02d}")

# Section 12.4 - 5 exercises
for i in range(1, 6):
    CreateImage(chapter=12, section=4, problem_id=i)
    print(f"Generated E12.04-{i:02d}")

# Problems - 4 problems (section=0 for problems)
for i in range(1, 5):
    CreateImage(chapter=12, section=0, problem_id=i)
    print(f"Generated P12-{i:02d}")

print("\nAll Chapter 12 images generated successfully!")
print("Total: 29 images (25 exercises + 4 problems)")
