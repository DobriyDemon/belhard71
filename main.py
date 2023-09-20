#Created Homework branch for the main file

list_of_numbers = []
number = int(input("Enter the number: "))
degree = int(input("Enter the max degree of the number: "))
for i in range(degree):
    list_of_numbers.append(int(number ** (i+1)))
print(f"List of numbers: {list_of_numbers}")
print(f"Max degree is: {degree}")