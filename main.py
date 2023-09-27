# Created Homework branch for the main file
# Task 4
list_of_data = ['English', 12, 'Russian', (56, 54, 52, 50), {'name': 'John'}, 'Italian', False]


def sort_strings_only(list_of_data):
    return sorted(filter(lambda x: type(x) == str, list_of_data))


print(sort_strings_only(list_of_data))

sort_strings_only(list_of_data)
