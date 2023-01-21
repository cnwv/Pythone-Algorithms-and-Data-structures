"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from random import random
from time import time


def time_calc(func):
    """Декоратор для замеров времени выполнения функций"""

    def wrapper(obj, items):
        start_time = time()
        res = func(obj, items)
        res_time = time() - start_time
        print(f'Замер времени для ф-ции: {func.__name__}(), эл-тов:'
              f' {len(items):,d}, время: {res_time:.6f} сек.')
        return res, res_time

    return wrapper


@time_calc
def elem_add_in_dict(curr_dict: dict, elements):
    curr_dict = {idx: elem for idx, elem in enumerate(elements)}
    return curr_dict


@time_calc
def elem_add_in_list(curr_list: list, elements):
    curr_list = [elem for elem in elements]
    return curr_list


test_dict = {}
test_list = []
test_counts = 100000, 1000000, 10000000
for test_cnt in test_counts:
    # генерим заданное кол-во случайных элементов
    random_elements = tuple(random() for _ in range(test_cnt))


elem_add_in_list(test_list, random_elements)
elem_add_in_dict(test_dict, random_elements)
