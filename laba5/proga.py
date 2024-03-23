def password_generator(shtuk,letters_count, numbers_count):
    import random
    import string
    passwords = []
    i=0
    while True:
        letters = string.ascii_letters
        numbers = string.digits

        password = ''.join(random.choices(letters, k=letters_count) + random.choices(numbers, k=numbers_count))
        yield password
        
        inv_password = ''.join([s.upper() if s.islower() else s.lower() for s in password])
        yield inv_password 
        
        ascii_password = list(map(ord, password))
        yield ascii_password

letters_count = int(input("Введите количество букв: "))
numbers_count = int(input("Введите количество цифр: "))
shtuk = int(input("Введите количество паролей"))
generator = password_generator(shtuk,letters_count, numbers_count)
for i in range(5):
    print("\nПароль",i+1)
    print("\nИсходный пароль:", next(generator))
    print("Пароль с измененным регистром:", next(generator))
    print("Пароль в ASCII коде:", next(generator))
