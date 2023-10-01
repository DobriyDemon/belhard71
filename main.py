# Created Homework branch for the main file
# Task 3
list_of_nums = []
count_of_nums = int(input("Enter the count of numbers in list: "))


def slide_of_list(count_of_nums: int) -> list:
    for i in range(1, int(count_of_nums) + 1):
        list_of_nums.append(i)
    print(list_of_nums)
    user_input_slide_of_list = int(input("Enter the count of slide: "))
    for i in range(len(list_of_nums)):
        list_of_nums[i] = list_of_nums[i] + user_input_slide_of_list
    print(list_of_nums)
    return list_of_nums


slide_of_list(count_of_nums = count_of_nums)
