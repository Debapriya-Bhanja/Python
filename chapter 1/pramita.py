a=int(input("Enter 1st Number  "))
b=int(input("Enter 2nd Number: "))
L1=[]
for i in range(1,a+1):
     if a%i==0:
         L1.append(i)
print(L1)       
L2=[]
for i in range(1,b+1):
    if b%i==0:
        L2.append(i)
print(L2)




