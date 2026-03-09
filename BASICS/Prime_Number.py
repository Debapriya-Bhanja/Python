# Prime Number - Simple and Easy Way

def is_prime(n):
   
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check if n is divisible by any number from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
        
    
    return True


# Main program
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    if is_prime(num):
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number!")
