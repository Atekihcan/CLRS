#!/usr/bin/env python3
"""
Script to generate all Chapter 11 solutions
"""

import os
from datetime import datetime

# Base directory for solutions
SOLUTIONS_DIR = "/home/user/CLRS/_solutions/11"

# Template for solution files
TEMPLATE = """---
title:       {title}
published:   {date} 12:00
modified:    {date} 12:00
keywords:    "{keywords}"
description: "{description}"
---

{content}
"""

# Solution content for remaining exercises
SOLUTIONS = {
    "E11.02-03.md": {
        "title": "Exercise 11.2-3",
        "keywords": "sorted lists, chaining, search performance",
        "description": "Professor Marley hypothesizes that he can obtain substantial performance gains by modifying the chaining scheme to keep each list in sorted order. How does the professor's modification affect the running time for successful searches, unsuccessful searches, insertions, and deletions?",
        "content": """> Professor Marley hypothesizes that he can obtain substantial performance gains by modifying the chaining scheme to keep each list in sorted order. How does the professor's modification affect the running time for successful searches, unsuccessful searches, insertions, and deletions?

Keeping the chains sorted by key provides minimal benefit and actually hurts insertion performance. Let's analyze each operation.

**Successful Search:** Maintaining sorted order doesn't help. We still need to search through the chain for the target key. In the average case with load factor $$\\alpha$$, we expect to examine $$\\Theta(1 + \\alpha)$$ elements whether the list is sorted or not. We cannot use binary search because we only have a linked list, not an array.

**Unsuccessful Search:** Sorted order provides a small benefit. When searching for a key $$k$$ that isn't present, we can stop as soon as we encounter a key larger than $$k$$ (assuming sorted order). This improves the constant factors, but the asymptotic running time remains $$\\Theta(1 + \\alpha)$$. On average, we might examine half the chain instead of the full chain, but this is only a factor of 2 improvement.

**Insertion:** Sorted order significantly hurts performance. Instead of inserting at the head in $$O(1)$$ time, we must find the correct position to maintain sorted order. This requires scanning the chain, taking $$\\Theta(1 + \\alpha)$$ time in the average case. This changes insertion from $$O(1)$$ to $$\\Theta(1 + \\alpha)$$, which is a substantial degradation.

**Deletion:** Sorted order doesn't affect deletion performance. With a doubly linked list and a pointer to the element, deletion remains $$O(1)$$ regardless of whether the list is sorted.

**Summary of running times:**

| Operation | Unsorted Chain | Sorted Chain |
|-----------|----------------|--------------|
| Successful Search | $$\\Theta(1 + \\alpha)$$ | $$\\Theta(1 + \\alpha)$$ |
| Unsuccessful Search | $$\\Theta(1 + \\alpha)$$ | $$\\Theta(1 + \\alpha)$$ |
| Insertion | $$O(1)$$ | $$\\Theta(1 + \\alpha)$$ |
| Deletion | $$O(1)$$ | $$O(1)$$ |

Professor Marley's hypothesis is incorrect. The modification provides minimal benefit for searches while significantly degrading insertion performance.

{% capture note %}
**When Sorted Chains Help**

Sorted chains would be beneficial if:
1. Unsuccessful searches are much more common than insertions
2. We need to enumerate keys in sorted order
3. We need range queries (finding all keys in an interval)

However, these scenarios are better served by other data structures like balanced binary search trees, which provide $$O(\\log n)$$ operations.
{% endcapture %}
{% include aside.html title='Design Tradeoffs' %}
"""
    },

    # Continue with more solutions...
}

def create_solution_file(filename, data):
    """Create a solution file with the given data"""
    date = datetime.now().strftime("%Y-%m-%d")

    content = TEMPLATE.format(
        title=data["title"],
        date=date,
        keywords=data["keywords"],
        description=data["description"],
        content=data["content"]
    )

    filepath = os.path.join(SOLUTIONS_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created {filepath}")

def main():
    for filename, data in SOLUTIONS.items():
        create_solution_file(filename, data)

if __name__ == "__main__":
    main()
