from utils.verify_contact import is_valid_phone_number
from utils.save_file import save_file


def test_is_valid_phone_number():
    assert is_valid_phone_number("1234567890") == True
    assert is_valid_phone_number("123 546 758 324526") == False


def test_save_file():
    assert save_file("id.txt", "1") == True
