
# !Calculate P(n, r) using a separate function.

import math

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

if r > n:
    print("r should not be greater than n")
else:
    result = math.factorial(n) // math.factorial(n - r)
    print("P(n, r) =", result)

    