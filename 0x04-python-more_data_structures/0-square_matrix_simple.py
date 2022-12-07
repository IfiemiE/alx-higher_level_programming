#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nRow = len(matrix)
    if nRow != 0:
        sq_matrix = []
        for r in range(nRow):
            sq_matrix.append([])
            nCol = len(matrix[r])
            for c in range(nCol):
                ele_sq = matrix[r][c] * matrix[r][c]
                sq_matrix[r].append(ele_sq)

        return sq_matrix
