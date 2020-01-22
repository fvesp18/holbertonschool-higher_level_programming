#!/usr/bin/python3
""" reads a txt file, prints to stdout """


def read_file(filename=""):
    """ some stuff """
    with open(filename, 'r') as aFile:
        for aLine in aFile:
            print(aLine, end="")
