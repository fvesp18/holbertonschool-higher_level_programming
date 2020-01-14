#!/usr/bin/python3
""" DIVIDES EACH ELEMENT OF MATRIX BY DIV """


def matrix_divided(matrix, div):
    """ 
    RETURNS NEW MATRIX WITH DIVIDED ELEMENTS.

    BOTH MATRIX AND DIV MUST BE OF TYPE INTEGER, FLOAT

    PARAMETERS:
        MATRIX: MATRIX
        DIV: DIVISOR
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    
    length = len(matrix)
    size = 0
    
    if length is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    result = [[] for row in range(length)]
    
    for row in matrix:
        for elem in row:
            size = size + 1
    
    for lists in result:
        if size != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if isinstance(elem, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            lists.append(round(float(elem / div), 2))

    return result
