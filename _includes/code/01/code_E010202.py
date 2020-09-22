n = 2
while n > 2 ** (n / 8.0):
    n += 1

print("Minimum value of n for which merge sort runs faster is", n)