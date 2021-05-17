"""1. Declare below types of variables and print them
Text:str
Numeric:int, float, complex (Positive and Negative)
Boolean:bool
Binary: bytes
String: str"""


text_string1 = 'kunal'
print("Type of the python object {0} is {1}".format(text_string1, type(text_string1)))

num_int = 45
print("Type of the python object {0} is {1}".format(num_int, type(num_int)))

num_float = 67.89
print("Type of the python object {0} is {1}".format(num_float, type(num_float)))

num_complex = 4+5j
print("Type of the python object {0} is {1}".format(num_complex, type(num_complex)))

boolean = False
print("Type of the python object {0} is {1}".format(boolean, type(boolean)))


binary = b'12'
print("Type of the python object {0} is {1}".format(binary, type(binary)))
print("Binary representation of {0} is {0:b}".format(12))