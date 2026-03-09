
# ?Define a function max_of_three() to return the largest of three numbers.


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# User input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

result = max_of_three(x, y, z)
print("Largest number is:", result)
