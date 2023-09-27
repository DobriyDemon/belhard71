# Task 1
string = input('Enter a decimal number:  ')


def str_to_int(string):
    result = 0
    for char in string:
        result = result * 10 + (ord(char) - ord('0'))
    print("Decmal num in 'str_to_int: '", result)
    print("Type of decmal num in 'str_to_int: '", type(result))
    return result


def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    print("Binary num in 'decimal_to_binary: '", binary)
    print("Type of binaty num in 'decimal_to_binary: '", type(binary))
    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
    print("Decmal num in 'binary_to_decimal: '", decimal)
    print("Type of decmal num in 'binary_to_decimal: '", type(decimal))
    return decimal


binary_to_decimal(decimal_to_binary(str_to_int(string)))
