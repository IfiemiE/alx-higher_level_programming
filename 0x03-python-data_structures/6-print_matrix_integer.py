#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    nRow = len(matrix)
    for i in range(nRow):
        nCol = len(matrix[i])
        for j in range(nCol):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (nCol - 1):
                print(' ', end='')
        print('')
