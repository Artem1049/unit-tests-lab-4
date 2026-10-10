from password import password_ok


def test_valid_password():
    assert password_ok("hello123") is True

def test_password_with_7_characters():
    assert password_ok("abc1234") == "Пароль має містити щонайменше 8 символів"

def test_password_with_exactly_8_characters():
    assert password_ok("abcd1234") is True

def test_password_with_space():
    assert password_ok("abcd 1234") == "Пароль не повинен містити пробілів"

def test_password_without_digit():
    assert password_ok("abcdefgh") == "Пароль має містити хоча б одну цифру"

def test_password_longer_than_32():
    assert password_ok("a1" * 17) == "Пароль має містити не більше 32 символів"

def test_password_without_letter():
    assert password_ok("12345678") == "Пароль має містити хоча б одну літеру"