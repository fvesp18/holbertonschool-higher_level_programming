#!/usr/bin/python3
statment = "{} arguments"
from sys import argv
i = 0
length = len(argv)
if length == 1:
    length = length - 1
    statement = "{} arguments."
    print(statement.format(length))
elif length > 1:
    length = length - 1
    statement = "{} arguments:"
    print(statement.format(length))
    while i < length:
        i += 1
        print("{}: {}".format(i, argv[i]))
