# Created Homework branch for the main file
# Task 5
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_of_nums)


def reverse(list_of_nums):
    list_of_nums.sort(reverse = True)
    print(list_of_nums)
    return list_of_nums


reverse(list_of_nums = list_of_nums)
