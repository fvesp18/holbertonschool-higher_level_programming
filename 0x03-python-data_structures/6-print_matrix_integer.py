#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for i in range(len(matrix[row])):
            if i != row + 3:
                print("{:d} ".format(matrix[row][i]), end="")

        print("")
