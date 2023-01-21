"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""
from hashlib import sha256
import json
import os


class CashWebpage:
    def __init__(self):
        self.web_page = ''
        self.cash = {}
        self.file = 'cash.json'
        self.salt = "231accf263e34a05a1388a759266c812"
        self.hash = ''

    def check_webpage(self):
        self.hash = sha256(self.web_page.encode() + self.salt.encode()).hexdigest()
        if not os.path.exists(self.file):
            print(f'Web page not in cash. Its hash {self.hash}')
            self.cash[self.hash] = 1
            with open(self.file, 'w', encoding='utf-8') as storage:
                json.dump(self.cash, storage)
        if os.path.exists(self.file):
            with open(self.file, 'r', encoding='utf-8') as storage:
                self.cash = json.load(storage)
            if self.hash in self.cash:
                print(f'This web page already in cash. Its hash {self.hash}')
            else:
                print(f'Web page not in cash. Its hash {self.hash}')
                self.cash[self.hash] = len(self.cash) + 1
                with open(self.file, 'w', encoding='utf-8') as storage:
                    json.dump(self.cash, storage)


cash = CashWebpage()
while cash.web_page != '0':
    cash.web_page = input("Enter web page. Enter 0 for exit")
    cash.check_webpage()




