n = 2
while 2 ** (n / 8.0) < n:
    n += 1

print("Maximum value of n for which insertion sort beats merge sort is", n - 1)