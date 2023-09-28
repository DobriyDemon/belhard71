# Created Homework branch for the main file
# Task 8

dict_users = \
    {
        1: {'name': 'Sergey', 'surname': 'Иванов', 'phone': '89154268789'},
        2: {'name': 'Gregory', 'surname': 'Nordef', 'phone': '88753033519', 'email': 'greg@gmail.com'},
        3: {'name': 'Vasa', 'surname': 'Gor', 'phone': '89123456789', 'email': ''},
        4: {'name': 'Nikita', 'surname': 'Hire', 'phone': '8912236436789'},
        5: {'name': 'Иван', 'surname': 'Irden', 'phone': '123-456-7890'},
        6: {'name': 'Петр', 'surname': 'Петров', 'phone': '098-765-4321', 'email': 'ivan@example.com'},
        7: {'name': 'Сидор', 'surname': 'Сидоров', 'phone': '555-555-5555', 'email': ''},
        8: {'name': 'Grey', 'surname': 'Forcing', 'phone': '45983-555-555', 'email': ''},
        9: {'name': 'Fred', 'surname': 'Harley', 'phone': '555-092548', 'email': 'Frad@gamil.com'},

    }

for id, user_data in dict_users.items():
    if 'email' not in user_data or user_data['email'] == '':
        print("Name: ", user_data['name'])
