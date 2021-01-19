import math

def FindMaxSubarrayBruteForce(A, low, high):
    left = low
    right = high
    sum = -math.inf
    for i in range(low, high):
        tempSum = 0
        for j in range(i, high):
            tempSum = tempSum + A[j]
            if tempSum > sum:
                sum = tempSum
                left = i
                right = j
    return (left, right, sum)

# Test with exact same array as in the example give in book
# Expected answer is A[8..11] = 43

arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
ans = FindMaxSubarrayBruteForce(arr, 0, len(arr))

print(f"Max subarray = A[{ans[0] + 1}..{ans[1] + 1}] = {ans[2]}")