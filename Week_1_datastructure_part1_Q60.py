"""60. WAP to add list of elements to a given set
Input
set_1 = {"a", "b", "c"}
list_1 = ["b", "d", "e"]"""

sample_set = {"a", "b", "c"}

list_of_num = ["b", "d", "e"]

for elem in list_of_num:
    sample_set.add(elem)
print('Modified Set: ')
print(sample_set)
