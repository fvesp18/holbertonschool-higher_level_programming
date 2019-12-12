#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    length = len(argv)
    if length == 1:
        length = length - 1
        statement = "{} arguments."
        print(statement.format(length))
    elif length == 2:
        length = length - 1
        statement = "{} argument:"
        print(statement.format(length))
        print("{}: {}".format(length, argv[1]))
    elif length > 1:
        length = length - 1
        statement = "{} arguments:"
        print(statement.format(length))
        while i < length:
            i += 1
            print("{}: {}".format(i, argv[i]))
