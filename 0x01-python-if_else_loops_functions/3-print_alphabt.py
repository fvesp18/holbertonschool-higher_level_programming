#!/usr/bin/python3
""" prints alphabet """

for c in range(97,123):
    if c == 101 or c == 113:
        pass
    else:
        print("{:c}".format(c), end="")
