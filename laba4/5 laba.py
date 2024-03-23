import random

def generate_password(num_letters, num_digits):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    
    password = ''.join(random.choices(letters, k=num_letters) + random.choices(digits, k=num_digits))
    inverted_password = password.swapcase()
    
    print("Исходный пароль:", password)
    print("Инвертированный пароль: ", inverted_password)
    
    return password

num_letters = int(input("Введите количество букв в пароле: "))
num_digits = int(input("Введите количество цифр в пароле: "))

generated_password = generate_password(num_letters, num_digits)

ascii_password = list(map(ord, generated_password))
print(f"ASCII коды символов пароля: ", ascii_password)