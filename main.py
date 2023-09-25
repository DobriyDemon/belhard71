# Created Homework branch for the main file
# Вывести четные числа от 2 до N по 5 в строку

list_of_fife = []

for i in range(2, int(input("Enter end of range: ")) + 1, 2):
    list_of_fife.append(i)
    if len(list_of_fife) >= 5:
        print(list_of_fife)
        list_of_fife.clear()

