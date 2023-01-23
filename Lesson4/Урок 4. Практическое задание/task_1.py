"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [x for x in nums if x % 2 == 0]


list = [i for i in range(1000)]

print(timeit.timeit("func_1(list)", setup="from __main__ import func_1, list", number=1000))
# 0.10690950200023508
print(timeit.timeit("func_2(list)", setup="from __main__ import func_2, list", number=1000))
# 0.04861902800030293
