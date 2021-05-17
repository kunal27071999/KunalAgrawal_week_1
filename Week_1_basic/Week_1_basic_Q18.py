"""18.del statement: explain with use"""

"""delete keyword is used to delete both the value as well as the variable"""


my_var = 5
my_tuple = ('Sam', 25)
my_dict = {'name': 'Sam', 'age': 25}

del my_var
del my_tuple
del my_dict

# Error: my_var is not defined
print(my_var)

# Error: my_tuple is not defined you can delete the whole tuple but cannot delete the value inside the tuple
print(my_tuple)

# Error: my_dict is not defined
print(my_dict)