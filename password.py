# Bykanov Artem, Z-41, variant 4

def password_ok(password): 
    if len(password) < 8: 
        return "Пароль має містити щонайменше 8 символів"

    if len(password) > 32:
        return "Пароль має містити не більше 32 символів"

    if any(char.isspace() for char in password):
        return "Пароль не повинен містити пробілів"

    if not any(char.isalpha() for char in password):
        return "Пароль має містити хоча б одну літеру"

    if not any(char.isdigit() for char in password):
        return "Пароль має містити хоча б одну цифру"

    return True