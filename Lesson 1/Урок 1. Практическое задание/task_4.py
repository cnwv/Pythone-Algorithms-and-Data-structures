"""
Задание 4.
Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
login_list = ["login1", "login2", "login3", "login4", "login5", "login6", "login7", "login8", "login9", "login10"]
pass_list = ["pass1", "pass2", "pass3", "pass4", "pass5", "pass6", "pass7", "pass8", "pass9", "pass10"]
users_dict = {
    'user1': 'pass1',
    'user2': 'pass2',
    'user3': 'pass3',
    'user4': 'pass4',
    'user5': 'pass5',
    'user6': 'pass6',
    'user7': 'pass7',
    'user8': 'pass8',
    'user9': 'pass9',
    'user10': 'pass10'
}


def first_methode(login, password):
    auth = False
    for key, value in users_dict.items():
        if key == login and password == value:
            auth = True
            break
    if auth is False:
        return f"login or password is invalid"
    else:
        return f"authorization successful"


def second_method(login, password):
    first = 0
    last = len(login_list) - 1

    while (first <= last):
        middle = (first + last) // 2

        if login == login_list[middle]:
            break

        if login < login_list[middle]:
            last = middle - 1
        else:
            first = middle + 1

    if password == pass_list[middle]:
        return f"authorization successful"
    else:
        return f"login or password is invalid"


print('First method')
print(first_methode("user10", "pass10"))
print('Second method')
print(second_method("login7", "pass7"))
