"""48. WAP to find the common elements between two arrays """

a = [1,2,3,4,5]
b= [1,2,3,4,5,6,7,8,9]

a_set = set(a)
b_set = set(b)

if (a_set & b_set):
    print(a_set & b_set)
else:
    print("No common elements")