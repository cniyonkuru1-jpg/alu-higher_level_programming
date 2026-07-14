#!/usr/bin/python3
"""Defines a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers, row by row."""
    for row in matrix:
        line = ""
        for i in range(len(row)):
            if i == len(row) - 1:
                line += "{:d}".format(row[i])
            else:
                line += "{:d} ".format(row[i])
        print(line)
