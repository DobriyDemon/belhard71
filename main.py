# Created Homework branch for the main file

count_of_output_numbers = int(input("Enter the count of output numbers: "))
more_than_K = int(input("Enter the number K: "))
num_M = int(input("Enter the number M: "))
list_of_output_nums = []
list_on_fife = []

for i in range(round(count_of_output_numbers/5)):
    for j in range(count_of_output_numbers * count_of_output_numbers):
        if j > more_than_K and j % num_M == 0:
            print("Each if worked, j: ", j)
            list_on_fife.append(j)
        if len(list_on_fife) > 4:
            list_of_output_nums.append(list_on_fife.copy())
            list_on_fife.clear()
        print(list_on_fife)
        if len(list_of_output_nums) >= round(count_of_output_numbers/5):
            break

print("List of output: ", list_of_output_nums)
print("Length 'List of output list': ", len(list_of_output_nums))
print("Total output length: ", len(list_of_output_nums*5))