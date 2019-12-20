#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    product = 0
    for key in a_dictionary:
        product = product * a_dictionary[key]

    return product
