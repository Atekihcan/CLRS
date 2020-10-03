# Bitwise binary addition of two lists
# containing binary digits with least significant bit first
def AddBinary(A, B):
    carry = 0
    n = max(len(A), len(B))
    C = [0 for i in range(n + 1)]
    for i in range(n):
        # One of A and B has length less than n
        # We need to treat index out of bound for that array
        # This is not explicitly handled in pseudocode
        a = A[i] if i < len(A) else 0
        b = B[i] if i < len(B) else 0

        # Modulo for sum and integer division for carry
        C[i] = (a + b + carry) % 2
        carry = (a + b + carry) // 2
    C[n] = carry
    return C

# Utility function for converting decimal to binary
def DecimalToBinary(num):
    if num == 0:
        return [0]
    ret = []
    while num > 0:
        ret.append(num & 1)
        num = num >> 1
    return ret

# Utility function for converting binary to decimal
def BinaryToDecimal(lst):
    num = 0
    for i in range(len(lst)):
        num += lst[i] << i
    return num

# Test
import random

num_failed = 0
total_tests = 100
for i in range(total_tests):
    # Create two random integers
    a = random.randint(0, 10000)
    b = random.randint(0, 10000)
    a_ = DecimalToBinary(a)
    b_ = DecimalToBinary(b)
    sum = BinaryToDecimal(AddBinary(a_, b_))

    # Check if the sum is correct
    if sum != (a + b):
        num_failed += 1
        print(f"#{i:<2} {a} + {b} = {sum} [Expected {(a + b)}]")

if num_failed > 0:
    print(f"\nFailed {num_failed}/{total_tests}")
else:
    print(f"Passed {total_tests}/{total_tests} tests")