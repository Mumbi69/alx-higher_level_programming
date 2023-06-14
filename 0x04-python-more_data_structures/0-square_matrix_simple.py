#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[0 for _ in range(len(row))] for row in matrix]

    for s in range(len(matrix)):
        for m in range(len(matrix[s])):
            square_matrix[s][m] = matrix[s][m] ** 2

    return square_matrix
