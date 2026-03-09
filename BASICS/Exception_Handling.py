
# ?Write a Python program using exception handling.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
    