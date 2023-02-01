"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from random import randint
from collections import deque
from timeit import timeit


def list_insert(n):
    list = []
    for i in random_list[:n]:
        list.insert(0, i)
    return list


def deque_appendleft(n):
    deq_obj = deque()
    for i in random_deque[:n]:
        deq_obj.appendleft(i)
    return deq_obj


def list_append(n):
    list = []
    for i in random_list[:n]:
        list.append(i)
    return list


def deque_append(n):
    deq_obj = deque()
    for i in random_deque[:n]:
        deq_obj.append(i)
    return deq_obj


def list_pop():
    random_list_pop = [randint(1, 1000) for _ in range(10000)]
    for i in range(10000):
        random_list_pop.pop()


def deque_pop():
    for i in range(10000):
        random_deque.popleft()


def list_pop0():
    for i in range(1000):
        random_list.pop(0)


def deque_popleft():
    for i in range(1000):
        random_deque.popleft()


random_list = [randint(1, 1000) for _ in range(1000000)]
random_deque = deque()
random_deque.extend(random_list)

n = 1000
# insert(0, i) vs appendleft(i)
# print(timeit("list_insert(n)", setup="from __main__ import list_insert, n", number=10000))
# print(timeit("deque_appendleft(n)", setup="from __main__ import deque_appendleft, n", number=10000))
# # 2.718362999999954
# # 0.6167083999998795
# # list.append vs deque.append
# print(timeit("list_append(n)", setup="from __main__ import list_append, n", number=10000))
# print(timeit("deque_append(n)", setup="from __main__ import deque_append, n", number=10000))
# 0.6689458000000741
# 0.6727911000000404
# print(timeit("list_pop()", setup="from __main__ import list_pop", number=1000))
# print(timeit("deque_pop()", setup="from __main__ import deque_pop", number=1000))
# 9.958442199999809
# 9.848818800000117
print(timeit("list_pop0()", setup="from __main__ import list_pop0", number=10))
print(timeit("deque_popleft()", setup="from __main__ import deque_popleft", number=10))
# 9.958442199999809
# 9.848818800000117
