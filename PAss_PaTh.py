import re

def is_password_strong(password):
    # Check the password length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # Check if the password contains any common patterns (e.g., "123", "password", etc.)
    common_patterns = ["123", "password", "qwerty", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        return False

    return True

if __name__ == "__main__":
    password = input("Enter a password to test its strength: ")

    if is_password_strong(password):
        print("Password is strong.")
    else:
        print("Password is weak. Please use a stronger password.")
