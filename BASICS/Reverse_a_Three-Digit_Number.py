
# !Reverse a three-digit number.


num = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

reverse = ones * 100 + tens * 10 + hundreds

print("Reversed number:", reverse)

