import string
import secrets

def generate_password():
    print("===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length (minimum 8): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 8:
        print("For a stronger password, choose at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))

    print("Generated Password:", password)

generate_password()
