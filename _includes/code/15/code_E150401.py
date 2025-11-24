# Longest Common Subsequence - Exercise 15.4-1
# Find LCS of <1, 0, 0, 1, 0, 1, 0, 1> and <0, 1, 0, 1, 1, 0, 1, 1, 0>

def lcs_length(X, Y):
    """
    Compute the length of the longest common subsequence.
    Returns both the c table and b table for reconstruction.
    """
    m = len(X)
    n = len(Y)

    # c[i][j] = LCS length for X[0..i-1] and Y[0..j-1]
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[' '] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'D'  # diagonal (match)
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'U'  # up
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'L'  # left

    return c, b

def print_lcs(b, X, i, j):
    """Reconstruct and return the LCS."""
    if i == 0 or j == 0:
        return []
    if b[i][j] == 'D':
        return print_lcs(b, X, i-1, j-1) + [X[i-1]]
    elif b[i][j] == 'U':
        return print_lcs(b, X, i-1, j)
    else:
        return print_lcs(b, X, i, j-1)

# The sequences from Exercise 15.4-1
X = [1, 0, 0, 1, 0, 1, 0, 1]
Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

print("Sequence X:", X)
print("Sequence Y:", Y)
print()

# Compute LCS
c, b = lcs_length(X, Y)

# Print the c table
print("LCS Length Table c[i,j]:")
print("     ", end="")
for j in range(len(Y)):
    print(f"  {Y[j]}", end="")
print()
for i in range(len(X) + 1):
    if i == 0:
        print(" -", end="")
    else:
        print(f" {X[i-1]}", end="")
    for j in range(len(Y) + 1):
        print(f"  {c[i][j]}", end="")
    print()
print()

# Find and print the LCS
lcs = print_lcs(b, X, len(X), len(Y))
print(f"LCS length: {c[len(X)][len(Y)]}")
print(f"One LCS:    {lcs}")
