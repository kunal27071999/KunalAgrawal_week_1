"""40. WAP find a pair with a given sum in the array."""

def getPair(a,sum):
    pair = []
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i] + a[j] == sum:
                pair.append(a[i])
                pair.append(a[j])

    return pair


arr = [ 1,2,3,4,5,6,7,8,9]
sum = 10
print(getPair(arr,sum))




