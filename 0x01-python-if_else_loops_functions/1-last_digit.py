#!/usr/bin/python3
""" Gets last digit of a number """


import random
number = random.randint(-10000, 10000)

sentence = "Last digit of {0} is {1} {2}"
if number < 0:
        ld = number * -1
ld = number % 10
five = "and is greater than 5"
lessthan = "and is less than 6 and not 0"
zero = "and is 0"
print(sentence.format(number, ld, zero if ld == 0 else lessthan))
