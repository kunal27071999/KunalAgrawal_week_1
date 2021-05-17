"""9. Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.
Examples
Input: [5,10,15]
Output: Arithmetic
"""

def ArithGeo(arr):
    flag = -1
    for i in range(len(arr)-2):
        if arr[i+1] - arr[i] == arr[i+2] - arr[i+1]:
            flag = 1
        elif arr[i+1]/arr[i] == arr[i+2]/arr[i+1]:
            flag = 0
        else:
            flag = -1
    return flag


a = [2, 6, 18, 54]
val = ArithGeo(a)
if val == 1:
    print("Arithmetic")
elif val == 0:
    print("geometic")
else:
    print(-1)
