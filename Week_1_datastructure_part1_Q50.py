"""50. WAP to check whether a given matrix is Lower Triangular Matrix or not."""


def islowertriangular(M):
    for i in range(0, len(M)):
        for j in range(i + 1, len(M)):
            if (M[i][j] != 0):
                return False
    return True


# Driver function.
M = [[1, 0, 0, 0],
     [1, 4, 0, 0],
     [4, 6, 2, 0],
     [0, 4, 7, 6]]

if islowertriangular(M):
    print("Yes")
else:
    print("No")

