from math import *

# for n lg n
n = 1
while n * log(n, 2) < 1000000:
    n += 1

print("Minimum value of n (n lg n) :", n - 1)

# for n!
n = 1
while factorial(n) < 1000000:
    n += 1

print("Minimum value of n (n!)     :", n - 1)