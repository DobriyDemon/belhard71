# Created Homework branch for the main file

cout_of_output_nums = int(input("Enter the count of output numbers: "))
more_than_K = int(input("Enter the number K: "))
num_M = int(input("Enter the number M: "))
list_of_output_nums = []
list_on_fife = []

for i in range(round(cout_of_output_nums/5)):
    for j in range(cout_of_output_nums):
        if j > more_than_K and j % num_M == 0:
            if len(list_on_fife) == 5:
                copy = list_on_fife.copy()
                print("Copy", copy)
                list_of_output_nums.append(copy)
                list_on_fife.clear()
            list_on_fife.append(j)
    list_of_output_nums.append(list_on_fife)
print("List on fife: ", list_on_fife)
print("List of output values", list_of_output_nums)