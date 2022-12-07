#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new = [row[:] for row in matrix]
    for idx, row in enumerate(new):
        for idx2, col in enumerate(row):
            new[idx][idx2] = row[idx2] ** 2
    return new
