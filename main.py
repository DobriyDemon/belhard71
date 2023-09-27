# Created Homework branch for the main file
# Task 6
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_of_nums)


def sort_list(list_of_nums):
    for i in range(len(list_of_nums)):
        if i % 2 != 0:
            list_of_nums.remove(i)
            list_of_nums.append(i)
        print(list_of_nums)
    print(list_of_nums)
    return list_of_nums


sort_list(list_of_nums)
