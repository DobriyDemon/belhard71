# Created Homework branch for the main file
from collections import defaultdict

data_username = defaultdict(list)
data_email = defaultdict(list)
data_2 = defaultdict(list)
count_of_users = input('Enter count of users: ')
#data_1[input('Enter username: ')].append(input('Enter email: '))
data_2 = {i: data_username[i].append(input("Enter username: ")), i: data_email[i].append(input("Enter email: ")) for i in range(int(count_of_users))}
print(data_username)
print(data_2)
