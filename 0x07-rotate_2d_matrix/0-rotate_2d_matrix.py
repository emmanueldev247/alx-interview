#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Function to rotate a n x n 2D matrix 90 degrees clockwise in-place
    Args:
        matrix (list): list of list representing matrix
    """
    # First transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then reverse
    for row in matrix:
        row.reverse()
