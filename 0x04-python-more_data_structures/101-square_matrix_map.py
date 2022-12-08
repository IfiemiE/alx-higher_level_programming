#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda R: list(map(lambda c: c * c, R)), matrix))
