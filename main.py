# Lesson_5_2 (Calculator)
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
