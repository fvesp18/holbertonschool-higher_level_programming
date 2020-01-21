#!/usr/bin/python3
""" reads a txt file, prints to stdout """


def read_file(filename=""):
    lineNum = 0
    with open('my_file_0.txt', encoding='UTF8') as aFile:
        for aLine in aFile:
            lineNum += 1
            print('{:}'.format(aLine.rstrip()))
