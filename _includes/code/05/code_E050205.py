import random

def count_inversions(arr):
    """
    Count the number of inversions in an array.

    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    """
    n = len(arr)
    inversions = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1

    return inversions

def simulate_expected_inversions(n, num_trials=1000):
    """
    Generate random permutations and compute average inversions.

    Args:
        n: Size of the permutation
        num_trials: Number of random permutations to test

    Returns:
        The empirical average number of inversions
    """
    total_inversions = 0

    for _ in range(num_trials):
        # Create a random permutation of 1 to n
        arr = list(range(1, n + 1))
        random.shuffle(arr)

        total_inversions += count_inversions(arr)

    return total_inversions / num_trials

# Test with different array sizes
print("Expected number of inversions in random permutations")
print("=" * 60)

for size in [5, 10, 20, 50, 100]:
    empirical_average = simulate_expected_inversions(size)
    theoretical_expected = size * (size - 1) / 4

    print(f"n = {size:3d} elements")
    print(f"  Theoretical: {theoretical_expected:.2f}")
    print(f"  Empirical:   {empirical_average:.2f}")
    print(f"  Difference:  {abs(empirical_average - theoretical_expected):.2f}")
    print()

# Examples with specific arrays
print("=" * 60)
print("Examples with n = 5:")
print()

# Sorted array (no inversions)
sorted_arr = [1, 2, 3, 4, 5]
print(f"Sorted array {sorted_arr}")
print(f"  Inversions: {count_inversions(sorted_arr)}")
print()

# Reverse sorted (maximum inversions)
reverse_arr = [5, 4, 3, 2, 1]
max_inversions = 5 * 4 // 2  # n(n-1)/2
print(f"Reverse array {reverse_arr}")
print(f"  Inversions: {count_inversions(reverse_arr)} (maximum = {max_inversions})")
print()

# Random examples
print("Three random permutations:")
for i in range(3):
    random_arr = list(range(1, 6))
    random.shuffle(random_arr)
    inv_count = count_inversions(random_arr)
    print(f"  {random_arr}: {inv_count} inversions")

print(f"\nExpected inversions for n=5: {5 * 4 / 4:.2f}")
