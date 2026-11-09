"""Simple calculator used to demonstrate Continuous Integration with Jenkins."""


def add_numbers(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract_numbers(a, b):
    """Return a minus b."""
    return a - b


def multiply_numbers(a, b):
    """Return the product of a and b."""
    return a * b


def divide_numbers(a, b):
    """Return a divided by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Application started")
    print("2 + 3 =", add_numbers(2, 3))
    print("7 - 4 =", subtract_numbers(7, 4))
    print("6 * 5 =", multiply_numbers(6, 5))
    print("8 / 2 =", divide_numbers(8, 2))
