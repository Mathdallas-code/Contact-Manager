import re


def is_valid_phone_number(phone_number: str):
    """
    Validates a phone number.
    A valid phone number must be 10 digits long and can include optional separators like spaces, dashes, or parentheses.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    pattern = re.compile(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    return bool(pattern.match(phone_number))


if __name__ == "__main__":
    test_numbers = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "1234567890",
        "123.456.7890",
        "123-45-6789",  # Invalid
        "12-3456-7890",  # Invalid
    ]

    for number in test_numbers:
        print(f"{number}: {'Valid' if is_valid_phone_number(number) else 'Invalid'}")
