"""7. Print 123 in decimal, binary, octal and hexadecimal format using base conversion functions """


def int_to_decimal(number):
    decimal = float(number)
    print(number, " in decimal :", decimal)


def int_to_binary(number):
    binary = bin(number)
    print(number, " in binary :", binary)


def int_to_octal(number):
    octal = oct(number)
    print(number, " in octal :", octal)


def int_to_hexadecimal(number):
    hexnum = hex(number)
    print(number, " in hexadecimal :", hexnum)


num = 123
int_to_decimal(num)
int_to_binary(num)
int_to_octal(num)
int_to_hexadecimal(num)
