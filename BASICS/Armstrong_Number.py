
#* 1. Check whether a given number is Armstrong or not.

num = int(input("Enter a number: "))
temp = num
sum = 0
order = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
                           
if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    

    
        