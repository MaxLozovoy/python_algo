"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
import hashlib
from uuid import uuid4

password = input('Введите пароль:\n>>')

hash_obj = hashlib.sha256((password).encode())

salt = uuid4().hex  # -> e52347823e2247e3b7a483f5f082e330
hex_dig_res = hash_obj.hexdigest()  # -> a6f5197ce1133b8c76d60f26f7d352300c0a410292d7b5457854c97135f77952

hash_of_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

print(f'Соль: {salt}')
print(f'Хэш-объект пароля: {hex_dig_res}')
print(f'Хэш "соленого пароля": {hash_of_pass}')

proof_password = input('Введите пароль повторно:\n>>')
hash_obj_proof = hashlib.sha256((password).encode())
hex_dig_res_proof = hash_obj_proof.hexdigest()
hash_of_proof_pass = hashlib.sha256(salt.encode() + proof_password.encode()).hexdigest()

if hash_of_proof_pass == hash_of_pass:
    print('Вы прошли аутентификацию')
else:
    print('Пароль не верный!!!')


