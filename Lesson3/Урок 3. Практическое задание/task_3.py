"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
from hashlib import sha256

word = input('Введите строку:')
substr = set()
while word != '':
    for i in range(len(word)):
        if word[i:] != word and word[i:] != '':
            substr.add(sha256(word[i:].encode()).hexdigest())
        if word[:-i] != word and word[:-i] != '':
            substr.add(sha256(word[:-i].encode()).hexdigest())
    word = word[1::]

print(f"Количество уникальных подстрок {len(substr)}. \nЕго хеши:")
print(*substr, sep="\n")
