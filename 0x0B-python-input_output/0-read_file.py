#!/usr/bin/python3
""" reads a txt file, prints to stdout """


def read_file(filename=""):
    """ some stuff """
    with open('my_file_0.txt', 'r') as aFile:
        for aLine in aFile:
            print(aLine, end="")
