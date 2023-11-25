import string
import random

def generate_password(length=12, include_special=True, include_numbers=True, include_uppercase=True):
    """Generate a random, secure password.

    Parameters:
    - length (int, optional): Length of the password. Defaults to 12.
    - include_special (bool, optional): Include special characters. Defaults to True.
    - include_numbers (bool, optional): Include numbers. Defaults to True.
    - include_uppercase (bool, optional): Include uppercase letters. Defaults to True.

    Returns:
    - str: Randomly generated password.
    """
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be included in the password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
