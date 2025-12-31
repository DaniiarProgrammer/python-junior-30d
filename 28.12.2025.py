#1 задача Счет скорости решений задач
"""
try:
    a = float(input("Задач решил: "))
    b = float(input("За сколько (в минутах): "))
    c = a/b
    if c>32:
        print(f"Новый рекорд! Поздравляю. Ваша скорость {c} задач в минуту")
    else:
        print(f"Неплохо, продолжай! Ваша скорость {c} задач в минуту")
except ZeroDivisionError:
    print("Ошибка, 0 писать нельзя!")
except ValueError:
    print("Ошибка, вы ввели не число!")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
"""


#2 задача секунды в чч:мм:cc
'''
try:
    a = int(input("Сколько секунд?: "))
    d = a // 3600 // 24
    h = a // 3600
    m = a // 60 % 60
    s = a % 60
    if h<10 and m<10 and s<10:
        print(f"0{h}:0{m}:0{s}")
    elif h<10 and m<10:
        print(f"0{h}:0{m}:{s}")
    elif m<10 and s<10:
        print(f"{h}:0{m}:0{s}")
    elif h<10 and s<10:
        print(f"0{h}:{m}:0{s}")
    else:
        print(f"{h}:{m}:{s}")
    print(f"В днях {d}")
except ValueError:
    print("Введите целое число!")
except Exception as e:
    print("Неизвестная ошибка!")
'''


#3 задача Анализатор предложений
'''
a = input("Введите предложение: ")
print(f"Количество символов: {len((a).replace(" ", ""))}")

print(f"Количество слов: {len(a.split())}")
z = a.count("!") + a.count("?") + a.count(".")
if z>0:
    print(f"Количество предложений: {z}")
else:
    print("Количество предложений: 0")
'''


#4 задача Счетчик ИМТ
'''
try:
    weight = int(input("Вес (кг): "))
    height = float(int(input("Рост (см): ")) / 100)
    IMT = round(weight / height**2, 2)
    print(f"""Ваш вес: {weight}
    Ваш рост: {height}
    ИМТ: {IMT}""")

    if IMT<18.5:
        print("Категория: Недостаточный вес")
    elif IMT>=18.5 and IMT<=24.9:
        print("Категория: Норма")
    elif IMT>=25 and IMT<=29.9:
        print("Категория: Избыточный вес")
    elif IMT>=30:
        print("Категория: Ожирение")
except ValueError:
    print("Нужно вводить числа!")
except ZeroDivisionError:
    print("Рост не может быть 0 см!")
'''

#Задача 5 Шифр Цезаря
"""
result = ""
a = input("Введите предложение которое надо зашифровать: ")
for hz in a:
    if hz.isalpha():
        if hz == "я":
            newcode = ord(hz)-31
            result+=(chr(newcode))
        elif hz == "z":
            newcode = ord(hz)-25
            result+=(chr(newcode))
        elif hz == "Я":
            result+="А"
        elif hz == "Z":
            result += "A"
        else:            
            newcode = ord(hz) + 1
            result+=(chr(newcode))
    else:
        result+=hz

print(result)
"""

#Задача 6 Фильтр Списка
"""
import random
result=[]
while len(result)<10:
    a = random.randint(1,100)
    result.append(a)
print(f"Список случайных цифр: {result}")
total=0
del2=[]
for hz in result:
    if hz%2==0:
        del2.append(hz)
        sum+=hz
print(f"Чётные числа: {del2}")
print(f"Их сумма: {total}") 
"""

#Задача 7 Проверка пароля
"""
passw = input("Введите пароль: ")
has_upper = any(char.isupper() for char in passw)
has_lower = any(char.islower() for char in passw)
has_digit = any(char.isdigit() for char in passw)
has_special = any(char in "!@#$%^&*" for char in passw)
lengh = len(passw)>=8

if all([has_upper, has_lower, has_digit, has_special, length_ok]):
    print("Пароль надёжный!")
else:
    print("Пароль ненадёжный!")
"""

#Задача 8 Автопароль + проверка
"""
import random
import string
password = []
while len(password)<12:
    letter = random.choice(string.ascii_letters)
    number = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    password.append(letter)
    password.append(number)
    password.append(special)
random.shuffle(password)
totalpassword = "".join(password)
print(totalpassword)

has_upper = any(char.isupper() for char in totalpassword)
has_lower = any(char.islower() for char in totalpassword)
has_digit = any(char.isdigit() for char in totalpassword)
has_special = any(char in "!@#$%^&*" for char in totalpassword)
lenght = len(totalpassword) >= 12

if all([has_upper, has_lower, has_digit, has_special, lenght]) is True:
    print("Надежный пароль!")
else:
    print("Ненадёжный пароль")
"""

#Задача 9. 10 Автопаролей + проверка
"""
import random
import string
goodpassword = 0
badpassword = 0
for i in range(10):
    password = []
    while len(password)<12:
        letter = random.choice(string.ascii_letters)
        number = random.choice(string.digits)
        special = random.choice("!@#$%^&*")

        password.append(letter)
        password.append(number)
        password.append(special)
    random.shuffle(password)
    totalpassword = "".join(password)
    print(totalpassword)

    has_upper = any(char.isupper() for char in totalpassword)
    has_lower = any(char.islower() for char in totalpassword)
    has_digit = any(char.isdigit() for char in totalpassword)
    has_special = any(char in "!@#$%^&*" for char in totalpassword)
    lenght = len(totalpassword) >= 12


    if all([has_upper, has_lower, has_digit, has_special, lenght]) is True:
        goodpassword+=1
    else:
        badpassword+=1
print(f"Сгенерировано 10 паролей.")
print(f"Надежных: {goodpassword}")
print(f"Ненадежных: {badpassword}")
"""


# Задача 10 повышенной сложности. 5 автопаролей + проверка + запись в текстовый файл

import random
import string
badpassword = 0
goodpassword = 0
vsego = 5
all_passwords = []
for i in range(vsego):
    password = []
    while len(password)<24:
        numbers = random.choice(string.digits)
        special = random.choice("!@#$%^&*")
        letters = random.choice(string.ascii_letters)
        password.append(numbers)
        password.append(letters)
        password.append(special)
    random.shuffle(password)
    totalpassword = "".join(password)
    all_passwords.append(totalpassword)
    print(totalpassword)

    has_upper = any(char.isupper() for char in totalpassword)
    has_lower = any(char.islower() for char in totalpassword)
    has_special = any(char in "!@#$%^&*" for char in totalpassword)
    lenght = len(totalpassword)>12

    if all([has_upper, has_lower, has_special, lenght]) is True:
        goodpassword += 1
    else:
        badpassword += 1

print(f"Сгенерировано {vsego} паролей")
print(f"Хороших {goodpassword} паролей")
print(f"Плохих {badpassword} паролей")

import os
print("Файл будет создан здесь:", os.path.abspath("passwords.txt"))
with open("passwords.txt", "w") as daun:
    for evrypass in all_passwords:
        daun.write(evrypass + "\n")
    daun.write("\n")
    daun.write(f"Сгенерировано {vsego} паролей\n")
    daun.write(f"Хороших паролей: {goodpassword}\n")
    daun.write(f"Плохих паролей: {badpassword}\n")

