"""56. WAP to accept a matrix of order n*m and interchange the diagonals"""

N = 3

def interchangeDiagonals(array):

    for i in range(N):
        if (i != N / 2):
            temp = array[i][i]
            array[i][i] = array[i][N - i - 1]
            array[i][N - i - 1] = temp

    for i in range(N):
        for j in range(N):
            print(array[i][j], end=" ")
        print()


array = [4, 5, 6], [1, 2, 3], [7, 8, 9]
interchangeDiagonals(array)