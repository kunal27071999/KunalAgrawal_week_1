"""15. WAPTP to print "Number" if the type of entered value is int or float, print "Binary"
 if type of entered value is binary and print "Strning" if type of entered value is str """

num = 10.01
if type(num) in (int, float):
    print("Number")
elif type(num) == bin:
    print("Binary")
elif type(num) == str:
    print("string")
