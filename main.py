# Created Homework branch for the main file
# Task 4
list_of_data = ['English', 12, 'Russian', (56, 54, 52, 50), {'name': 'John'}, 'Italian']


def filter_strings(lst):
    return ' '.join(str(x) for x in lst if isinstance(x, str))


print(filter_strings(lst = list_of_data))
