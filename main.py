# Created Homework branch for the main file
# TODO: Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

dict_users = \
    {
        1: {'name': 'Sergay', 'surname': 'Иванов', 'phone': '89154268789', 'email': 'ivan@gmail.com'},
        2: {'name': 'Gregory', 'surname': 'Иванов', 'phone': '88753033519', 'email': 'greg@gmail.com'},
        3: {'name': 'Vasa', 'surname': 'Иванов', 'phone': '89123456789', 'email': ''},
        4: {'name': 'Nikita', 'surname': 'Иванов', 'phone': '8912236436789'},
        5: {'name': 'Иван', 'surname': 'Иванов', 'phone': '123-456-7890', 'email': 'ivan@example.com'},
        6: {'name': 'Петр', 'surname': 'Петров', 'phone': '098-765-4321'},
        7: {'name': 'Сидор', 'surname': 'Сидоров', 'phone': '555-555-5555', 'email': ''}
    }

for i in dict_users:
    if dict_users[i]['email'] == '' or dict_users[i]['email'] is None or dict_users[i]['email'] not in dict_users[i]:
        print(dict_users[i]['name'])
        print(dict_users[i]['phone'])
    else:
        print(dict_users[i]['name'])
        print(dict_users[i]['email'])
