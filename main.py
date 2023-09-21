# Created Homework branch for the main file

cout_of_output_nums = int(input("Enter the count of output numbers: "))
more_than_K = int(input("Enter the number K: "))
num_M = int(input("Enter the number M: "))
list_of_output_nums = []
list_on_fife = []

for i in range(cout_of_output_nums):
    if i > more_than_K:
        print("i is more than K: ")
        if i % num_M == 0:
            print("i is a multiple of M: ")
            if len(list_on_fife) <= 5:
                list_on_fife.append(i)
                print("list_on_fife <=5: ", list_on_fife)
            else:
                list_on_fife.clear()
                list_on_fife.append(i)

                print("list_on_fife if list <=5(else): ", list_on_fife)
            list_of_output_nums.append(list_on_fife)
            print("list_of_output_nums: ", list_of_output_nums)
print(list_of_output_nums)