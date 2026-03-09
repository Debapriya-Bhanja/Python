
# !Generate Fibonacci series up to n numbers using a function.

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# User input
n = int(input("Enter number of terms: "))
fibonacci(n)
