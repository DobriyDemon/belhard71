# Created Homework branch for the main file
# Task 7
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_of_nums)
print("The length of the list is: ", len(list_of_nums))

for i in range(len(list_of_nums)):
    if i != len(list_of_nums) - 1:
        sum_neighbors = list_of_nums[i - 1] + list_of_nums[i + 1]
    else:
        sum_neighbors = list_of_nums[i - 1] + list_of_nums[0]
    print("The sum of the neibors of ", list_of_nums[i], " is: ", sum_neighbors)
