"""44. WAP to Segregate 0s and 1s in an array."""

a = [0,1,0,1,0,1,0]
print([i for i in a if i == 0]+ [i for i in a if i ==1])
