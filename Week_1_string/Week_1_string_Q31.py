"""31. WAP to print number of occurances of characted in the gven string"""

string = "asdsdscsdad"
for i in range(len(string)):
    print(string[i], " ", string.count(string[i]))
