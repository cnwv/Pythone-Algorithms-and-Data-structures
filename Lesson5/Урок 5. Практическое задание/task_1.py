"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple


def midlle_profit(n):
    COMPANIES = namedtuple("Company", "name period_1 period_2 period_3 period_4")
    companies_profit = {}
    more_middle = {}
    less_middle = {}
    for company in range(n):
        company = COMPANIES(
            name=input("Enter name company - "),
            period_1=int(input("Period 1 - ")),
        period_2 = int(input("Period 2 - ")),
        period_3 = int(input("Period 3 - ")),
        period_4 = int(input("Period 4 - ")))
        companies_profit[company.name] = \
            (company.period_1 + company.period_2 + company.period_3 + company.period_4)
    aver_profit = sum(companies_profit.values()) / n
    for key, value in companies_profit.items():
        if companies_profit[key] > aver_profit:
            more_middle[key] = value
        else:
            less_middle[key] = value
    print(f"Average profit - {aver_profit}")
    print(f"Companies more middle profit")
    for i in more_middle.items():
        print(*i)
    print(f"Companies less middle profit")
    for i in less_middle.items():
        print(*i)

midlle_profit(int(input('Enter amount of the companies')))

