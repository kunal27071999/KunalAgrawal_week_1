"""17.What is none data type, declare and print it"""

"""The None keyword is used to define a null variable or an object. In Python, None keyword is an object,
 and it is a data type of the class NoneType.

We can assign None to any variable, but you can not create other NoneType objects."""

x = None

if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")
