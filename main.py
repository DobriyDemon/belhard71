# Created Homework branch for the main file
# Вывести четные числа от 2 до N по 5 в строку

list_of_fife = []

for i in range(2, int(input("Enter end of range: ")) + 1, 2):
    list_of_fife.append(i) #Append i on index, which equals i
    if len(list_of_fife) == 5: #Check if list has more or equals 5 elements
        joined = ", ".join(str(x) for x in list_of_fife)
        print(joined)
        list_of_fife.clear()
