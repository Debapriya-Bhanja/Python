#! Password Generator - Create secure random passwords

import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    """Generate a password based on user preferences."""
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        print("Error: Select at least one character type!")
        return None
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    print()
    
    # Get password length
    length = int(input("Enter password length: "))
    
    if length <= 0:
        print("Error: Password length must be greater than 0!")
        return
    
    print("\nSelect character types to include:")
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate password
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    
    if password:
        print("\nGenerated Password:", password)
        print("Password length:", len(password))

if __name__ == "__main__":
    main()
