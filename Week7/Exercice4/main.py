from password_generator import generate_password, validate_password_length

# Example usage
password_length = 32
include_special_characters = True
include_numbers = True
include_uppercase_letters = True

# Validate password length
validate_password_length(password_length)

# Generate a password
password = generate_password(
    length=password_length,
    include_special=include_special_characters,
    include_numbers=include_numbers,
    include_uppercase=include_uppercase_letters
)

print(f"Generated Password: {password}")
