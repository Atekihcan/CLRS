import random
import math

def Random01():
    """Simulates RANDOM(0, 1) - returns 0 or 1 with equal probability"""
    return random.randint(0, 1)

def RandomAB(a, b):
    """
    Generates a random integer in [a, b] using only Random01()

    Args:
        a: lower bound (inclusive)
        b: upper bound (inclusive)

    Returns:
        Random integer in [a, b]
    """
    n = b - a + 1
    k = math.ceil(math.log2(n))

    while True:
        # Generate k random bits to form a number in [0, 2^k - 1]
        r = 0
        for i in range(k):
            r = 2 * r + Random01()

        # Accept if r < n, otherwise reject and try again
        if r < n:
            return a + r

# Test the implementation
print("Testing Random(3, 7):")
print("Generating 20 random numbers in [3, 7]:")

results = []
for _ in range(20):
    results.append(RandomAB(3, 7))

print(results)

# Verify distribution (generate many samples)
print("\nDistribution test with 10000 samples:")
counts = {i: 0 for i in range(3, 8)}
for _ in range(10000):
    counts[RandomAB(3, 7)] += 1

for value, count in sorted(counts.items()):
    percentage = (count / 10000) * 100
    bar = '█' * int(percentage / 2)
    print(f"{value}: {count:4d} ({percentage:5.2f}%) {bar}")

print("\nExpected: Each number should appear ~20% of the time (2000/10000)")
