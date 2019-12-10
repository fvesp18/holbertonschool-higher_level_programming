#!/usr/bin/python3
""" prints digits and its hex value """


for i in range(0, 99):
    print("{:d} = 0x{:x}".format(i, i), end="\n")
