# #Functions
#
# def function():
#     print("Hello")
#
#
# #Return in function, "function" work's only befor finding "return"
#
# def function():
#     print("Hello")
#     return "Hello", "World"
#
# res = function()
# print(res)
#
#
# #Argument's for function
# def multyply(x, y):#If argument has two underline before name, arguments gives to function only like "__a = 2"
#     return x * y
#
# print(multyply(2, 3))
# print(multyply(x = 2, y = 3))

# Необязательные аргументы(arguments that has "None" value)
# def function(x, y, *args, **kwargs):#kwargs - необязательные именованные аргументы(словарь)
#     print(x, y, args, kwargs)
#
# function(1, 2)
# function(1, 2, 3)
# function(1,2,3, b=4)

# check stirng is polindrone
text = input("Enter text: ")
def is_polindrone(text: str) -> bool:#Tell that we need to input string and return bool
    return text.lower() == text.lower()[::-1]


print(is_polindrone(text))

def a():
    pass

def b(func: callable):
    func(a)
