# Created Homework branch for the main file
# Task 5
count_of_nums_in_list = input("Enter a count of numbers in list: ")
list_of_nums = []
for i in range(int(count_of_nums_in_list) + 1):
    list_of_nums.append(i)
list_of_nums.remove(0)
print(list_of_nums)


def reverse(list_of_nums):
    len_list_of_nums = len(list_of_nums)
    for i in range(len_list_of_nums - 1, -1, -1):
        list_of_nums.append(list_of_nums[i])
    count = list_of_nums[0]
    while len(list_of_nums) != len_list_of_nums:
        list_of_nums.remove(count)
        count += 1
    print(list_of_nums)
    return list_of_nums


reverse(list_of_nums = list_of_nums)
