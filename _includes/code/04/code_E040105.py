import math

def FindMaxSubarrayLinear(A, low, high):
    best = -math.inf
    current = 0
    left = 0
    right = 0
    current_left = 0
    for i in range(low, high):
        current += A[i]
        if current > best:
            # Update best sum
            best = current
            left = current_left
            right = i
        
        if current < 0:
            # Reset current sum
            current = 0
            current_left = i + 1
    return (left, right, best)

# Test with exact same array as in the example give in book
# Expected answer is A[8..11] = 43

arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
ans = FindMaxSubarrayLinear(arr, 0, len(arr))

print(f"Max subarray = A[{ans[0] + 1}..{ans[1] + 1}] = {ans[2]}")