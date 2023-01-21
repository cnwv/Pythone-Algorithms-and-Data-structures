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
"""
from hashlib import sha256
from uuid import uuid4
import json
import os
from time import sleep


class CheckPassword:
    def __init__(self, storage=dict(), storage_json='Passwords.json'):
        self.storage = storage  # База паролей на json
        self.storage_json = storage_json  # Имя базы
        self.pwd = ''  # Пароль
        self.hash_pwd = ''  # Хеш пароля
        self.salt = ''  # Соль
        self.salted_hash = ''  # Соленый хеш

    def get_hash(self):
        """Вычисляем хеш пароля, без соли"""
        self.hash_pwd = sha256(self.pwd.encode()).hexdigest()

    def check_hash(self):
        """Проверяем хеш веденного пароля с базой"""
        if self.hash_pwd not in self.storage:  # Если хеша пароля не существует в базе, то генерим новую соль
            self.salt = uuid4().hex
            return False
        else:
            self.salt = self.storage[self.hash_pwd]  # Если хеш нашелся, то берем его соль из базы
            return True

    def get_salted_hash(self):
        """Вычисляем соленый хеш"""
        self.salted_hash = sha256(self.pwd.encode() + self.salt.encode()).hexdigest()

    def read_base(self):
        """Читаем базу"""
        if not os.path.exists(self.storage_json):  # Если в папке не существует базы, возвращаем пустой словарь
            return self.storage
        with open(self.storage_json, 'r', encoding='utf-8') as storage:
            self.storage = json.load(storage)

    def write_base(self):
        """Записываем базу в json"""
        self.storage[self.hash_pwd] = self.salt  # записываем новый хеш и соль
        with open(self.storage_json, 'w', encoding='utf-8') as storage:  # перезаписываем
            json.dump(self.storage, storage)


if __name__ == '__main__':
    hashes = CheckPassword()
    # Меню
    while True:
        hashes.pwd = input('Введи пароль: \n')
        if hashes.pwd == "0":
            exit(0)
        hashes.get_hash()  # Cчитаем хеш
        hashes.read_base()  # Читаем базу
        # hashes.check_hash()
        # Проверяем хеш
        if hashes.check_hash():
            hashes.get_salted_hash()
            print("Успешно! Ваш соленый хеш - ", hashes.salted_hash)
        else:
            hashes.get_salted_hash()
            print("Пароля не существует в базе! Его соленый хеш - ", hashes.salted_hash)
            print("Записываем в базу")
            sleep(1)  # выебоны
            print('...')
            sleep(2)
            print('Готово!')
            hashes.write_base()
