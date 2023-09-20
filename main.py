# Created Homework branch for the main file
from collections import defaultdict

count_of_users = int(input("Enter count of users: "))
data_username_and_email = {}
data_output = defaultdict(list)
data_username_and_email['username_and_email'] = [input("Enter username: ") + ", " + input("Enter email: ") for i in range(count_of_users)]
data_output = {i: data_username_and_email['username_and_email'][i] for i in range(count_of_users)}
print(f"Data username and email: {data_username_and_email}")
print(f"Data output: {data_output}")
