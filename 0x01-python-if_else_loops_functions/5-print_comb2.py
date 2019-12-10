#!/usr/bin/python3
""" prints all numbers from 00 to 99 """


for i in range(00, 100):
    if i <= 98:
        print("{:02d}".format(i), end=", ")

if i == 99:
    print("{:d}".format(i), end="\n")
