import random
import string

def password_generator(num_letters, num_digits):
    letters = string.ascii_letters
    digits = string.digits

    generated_password = ""

    for _ in range(num_letters):
        generated_password += random.choice(letters)

    for _ in range(num_digits):
        generated_password += random.choice(digits)

    return generated_password

def password_to_ascii(password):
    return ' '.join(str(ord(char)) for char in password)

num_letters = int(input("Введите количество букв: "))
num_digits = int(input("Введите количество цифр: "))

generated_password = password_generator(num_letters, num_digits)

print("Сгенерированный пароль:", generated_password)
print("Пароль с измененным регистром:", generated_password.swapcase())

ascii_generated_password = password_to_ascii(generated_password)
print("ASCII код сгенерированного пароля:", ascii_generated_password)
