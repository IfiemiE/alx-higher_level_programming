#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        nRow = len(matrix)
        for i in range(nRow):
            nCol = len(matrix[i])
            for j in range(nCol):
                if j != (nCol - 1):
                    print("{:d} ".format(matrix[i][j]), end="")
                else:
                    print("{:d}".format(matrix[i][j]))
