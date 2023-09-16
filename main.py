
user_input = input("Enter something: ")
result_1_1 = user_input.replace(" ", "-")
print(result_1_1)


splitted = user_input.split()
print(splitted)
result_2_1 = "-".join(splitted)
print(result_2_1)
