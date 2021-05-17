"""32. WAPTP average of first 10 numbers"""
n = 10
temp = n
sum = 0
while(n!=0):
    sum = sum + n
    n = n - 1
print(sum/temp)
