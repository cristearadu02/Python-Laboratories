def add(a, b):
    """Addition: Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Subtraction: Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Multiplication: Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Division: Returns the result of dividing two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
