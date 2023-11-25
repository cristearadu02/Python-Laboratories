def validate_password_length(length):
    """Validate that the specified password length is non-negative."""
    if length < 0:
        raise ValueError("Password length must be a non-negative integer.")
