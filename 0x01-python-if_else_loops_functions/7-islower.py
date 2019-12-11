#!/usr/bin/python3
""" specifies if a char is uppercase or lowercase """


def islower(c):
    if (ord(c) >= 97 and c <= 122):
        return(True)
    else:
        return(False)
