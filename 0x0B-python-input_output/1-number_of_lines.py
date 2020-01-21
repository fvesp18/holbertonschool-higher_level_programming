#!/usr/bin/python3
""" returns the number of lines in a file as an integer """


def number_of_lines(filename=""):
    lineNum = 0
    with open('my_file_0.txt', encoding='UTF8') as aFile:
        for aLine in aFile:
            lineNum += 1
        return lineNum
