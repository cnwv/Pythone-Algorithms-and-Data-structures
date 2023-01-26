"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    n = 1234567890
    revers_1(n)
    revers_2(n)
    revers_3(n)


cProfile.run('main()')
"""
  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     11/1    0.000    0.000    0.000    0.000 task_3.py:16(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:40(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
number = 10000
timeit_dict = {
    "revers_1(123456789)": "from __main__ import revers_1",
    "revers_2(123456789)": "from __main__ import revers_2",
    "revers_3(123456789)": "from __main__ import revers_3",
}
for stmt, set in timeit_dict.items():
    print(f"Замер функции {stmt}={round(timeit.timeit(stmt, setup=set), 3)}c")
"""
Замер функции revers_1(123456789)=3.576с
Замер функции revers_2(123456789)=1.663с
Замер функции revers_3(123456789)=0.335с
"""
