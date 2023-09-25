# Created Homework branch for the main file
print("Calculator!")
num1 = int(input("Enter first number: "))
action = input("Enter action: ")
num2 = int(input("Enter second number: "))

if action == "+":
    result = num1 + num2
elif action == "-":
    result = num1 - num2
elif action == "*":
    result = num1 * num2
elif action == "/":
    result = num1 / num2
elif action == "**":
    result = num1 ** num2
elif action == "%":
    result = num1 % num2
elif action == "//":
    result = num1 // num2

print("Result: ",num1, action, num2, "=", result)
