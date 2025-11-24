# Longest Increasing Subsequence - O(n^2) Algorithm
# Exercise 15.4-5

def lis_quadratic(A):
    """
    Find the longest increasing subsequence using O(n^2) DP.
    Returns the length and the actual subsequence.
    """
    n = len(A)
    if n == 0:
        return 0, []

    # L[i] = length of LIS ending at index i
    L = [1] * n
    # P[i] = predecessor index of element at i in the LIS
    P = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1
                P[i] = j

    # Find the index with maximum L value
    max_length = max(L)
    max_idx = L.index(max_length)

    # Reconstruct the LIS by following predecessors
    lis = []
    idx = max_idx
    while idx != -1:
        lis.append(A[idx])
        idx = P[idx]
    lis.reverse()

    return max_length, lis

# Test examples
test_cases = [
    [10, 22, 9, 33, 21, 50, 41, 60, 80],
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
]

print("Longest Increasing Subsequence - O(n^2) Algorithm")
print("=" * 55)

for A in test_cases:
    length, lis = lis_quadratic(A)
    print(f"Sequence: {A}")
    print(f"  LIS length: {length}")
    print(f"  One LIS:    {lis}")
    print()

# Show the L array for understanding
print("Detailed trace for first example:")
A = test_cases[0]
n = len(A)
L = [1] * n
P = [-1] * n

print(f"Sequence: {A}")
print()

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i] and L[j] + 1 > L[i]:
            L[i] = L[j] + 1
            P[i] = j
    print(f"After processing A[{i}]={A[i]:2d}: L = {L[:i+1]}")

print()
print(f"Final L array: {L}")
print(f"Maximum LIS length: {max(L)}")
