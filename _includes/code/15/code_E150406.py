# Longest Increasing Subsequence - O(n log n) Algorithm
# Exercise 15.4-6

def binary_search(T, length, target):
    """
    Find the largest index i such that T[i] < target.
    Returns 0 if no such index exists.
    """
    lo = 1
    hi = length
    while lo <= hi:
        mid = (lo + hi) // 2
        if T[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo  # Position where target should go

def lis_nlogn(A):
    """
    Find the longest increasing subsequence using O(n log n) algorithm.
    Returns the length and the actual subsequence.
    """
    n = len(A)
    if n == 0:
        return 0, []

    # T[k] = smallest ending value of any LIS of length k
    T = [0] * (n + 1)
    T[0] = float('-inf')  # Sentinel

    # B[k] = index in A of element stored at T[k]
    B = [0] * (n + 1)

    # P[i] = predecessor index of A[i] in the LIS
    P = [-1] * n

    length = 0

    for i in range(n):
        # Binary search for position
        pos = binary_search(T, length, A[i])

        # Update T and B
        T[pos] = A[i]
        B[pos] = i

        # Record predecessor
        if pos > 1:
            P[i] = B[pos - 1]

        # Update length if extended
        if pos > length:
            length = pos

    # Reconstruct LIS
    lis = []
    idx = B[length]
    while idx != -1:
        lis.append(A[idx])
        idx = P[idx]
    lis.reverse()

    return length, lis

# Test examples
test_cases = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [10, 22, 9, 33, 21, 50, 41, 60, 80],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
]

print("Longest Increasing Subsequence - O(n log n) Algorithm")
print("=" * 55)

for A in test_cases:
    length, lis = lis_nlogn(A)
    print(f"Sequence: {A}")
    print(f"  LIS length: {length}")
    print(f"  One LIS:    {lis}")
    print()

# Detailed trace
print("Detailed trace for [3, 1, 4, 1, 5, 9, 2, 6]:")
print("=" * 55)
A = [3, 1, 4, 1, 5, 9, 2, 6]
n = len(A)

T = [float('-inf')] + [float('inf')] * n
length = 0

for i in range(n):
    pos = binary_search(T, length, A[i])
    T[pos] = A[i]
    if pos > length:
        length = pos

    # Show T array (only active portion)
    active_T = [T[j] for j in range(1, length + 1)]
    print(f"Process A[{i}]={A[i]}: T = {active_T}, length = {length}")

print()
print(f"Final LIS length: {length}")
