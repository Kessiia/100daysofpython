import string
import random

def generate_password(length):
    # Adds all the letters, numbers and punctuations
    char = string.ascii_letters + string.digits + string.punctuation

    # Picks random characters from char based on the lenght
    password = ''.join(random.choice(char) for _ in range(length))

    return password

length = int(input("password length:\n"))

print (f"Password: {generate_password(length)}\n")


# Updated code to include requirements of most log ins

import string
import random

def generate_password(length):
    # Define character sets for each type of character
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each character set
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

length = int(input("Enter password length:\n"))

print(f"Password: {generate_password(length)}\n")
