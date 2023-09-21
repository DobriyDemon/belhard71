# Operatory vetvlenia
a = int(input("Enter number: "))

# if a > 0:# if a return True
#     print("Variable 'a' is positive")
# elif a < 0: # if a return False
#     print("Variable 'a' is negative")
# else: # if a return False in each case
#     print("Variable 'a' is zero")
#
# # Operatory "and" and "or"
# #And - ymnozhenie
# if a > 0 and a == 10:
#     print("Variable 'a' is positive and equal to 10")
#
# #Or - clozhenie
#
# if (a < 0 or a == -10) and a == 11:
#     print("Variable 'a' is positive and equal to 11")

a = 4
b = 0
print(a or False) #Return left operand if it's True, else return right operand
print(b and False)#Return right operand if it's True, else return left operand

#Cicle 'for'
#enumerate - return index and value (return cortage)

#Continie - work only in loop "for"
for i in range(10):
    if i == 5:
        continue
    print(i)
#Break - work only in loop "for"
for i in range(10):
    if i == 5:
        continue
    print(i)
