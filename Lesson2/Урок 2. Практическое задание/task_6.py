"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randint


def guess_game(attempts):
    guess = int(input('Guess - '))
    if attempts == 0:
        return f'You lose! Number was - {number}'
    if guess == number:
        return f'You win!'
    else:
        if guess > number:
            print("Smaller")
            return guess_game(attempts - 1)
        else:
            print("More")
            return guess_game(attempts - 1)


number = randint(1, 100)
print("Guess a number from 1 to 100")
print(guess_game(10))
