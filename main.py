# Task 1
string = input('Enter a decimal number: ')


def str_to_int(string):
    result = 0
    for char in string:
        result = result * 10 + (ord(char) - ord('0'))
    print(result)
    print(type(result))
    return result


def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    print(binary)
    print(type(binary))
    return binary


decimal_to_binary(str_to_int(string))
