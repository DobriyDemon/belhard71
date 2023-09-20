# Created Homework branch for the main file
from collections import defaultdict
count_of_users = int(input("Enter count of users: "))
data_username_and_email = []
data_username_and_email = {'username': [input("Enter username: ")], 'email': [input("Enter email: ")]}
data_output = defaultdict(list)
data_output.fromkeys(['name'],[data_username_and_email])

print(f"Data username: {data_username_and_email}")
print(f"Data output: {data_output}")
# print(f"List: {list_username_and_email_values}")
# print(f"Data 1: {data_1}")
# print(f"Data 2: {data_2}")
