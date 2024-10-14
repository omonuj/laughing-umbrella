import random
import string

def password_generator(length = 12, use_uppercase = True, use_digits = True, use_special = True):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special else ''

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if len(all_characters) == 0:
        raise ValueError('Password generator must have at least one character')

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():

    print("Welcome to password App generator!")
    while True:
        try:
            length = int(input("Enter password length(e.g., 12): "))
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_special = input("Include special characters? (y/n): ").lower() == 'y'

            password = password_generator(length, use_uppercase, use_digits, use_special)
            print(f"Generated password: {password}")
            print("Hope your Fcking like this password cause it was not easy generating it!")
            break
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()