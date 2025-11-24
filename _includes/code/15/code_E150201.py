# Matrix-Chain Multiplication - Finding Optimal Parenthesization
# Exercise 15.2-1: Dimensions <5, 10, 3, 12, 5, 50, 6>

def matrix_chain_order(p):
    """
    Compute optimal parenthesization for matrix chain.
    p: list of dimensions [p0, p1, ..., pn] for n matrices
       where matrix Ai has dimensions p[i-1] x p[i]
    Returns: (m, s) tables
    """
    n = len(p) - 1  # number of matrices

    # m[i][j] = min scalar mults for Ai...Aj
    # s[i][j] = optimal split point for Ai...Aj
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # Chain length l = 2 to n
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')

            # Try all split points
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    """Return string showing optimal parenthesization."""
    if i == j:
        return "A" + str(i)
    else:
        left = print_optimal_parens(s, i, s[i][j])
        right = print_optimal_parens(s, s[i][j] + 1, j)
        return "(" + left + right + ")"

# Exercise 15.2-1 dimensions
p = [5, 10, 3, 12, 5, 50, 6]
n = len(p) - 1

print("Matrix dimensions:")
for i in range(1, n + 1):
    print(f"  A{i}: {p[i-1]} x {p[i]}")
print()

# Compute optimal solution
m, s = matrix_chain_order(p)

print("Minimum costs m[i,j]:")
for i in range(1, n + 1):
    row = [str(m[i][j]).rjust(5) for j in range(1, n + 1)]
    print(f"  i={i}: {' '.join(row)}")
print()

print(f"Optimal cost: {m[1][n]} scalar multiplications")
print(f"Optimal parenthesization: {print_optimal_parens(s, 1, n)}")
