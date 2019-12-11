#!/usr/bin/python3
""" Gets last digit of a number """


import random
number = random.randint(-10000, 10000)

sentence = "Last digit of {0} is {1} {2}"

if number < 0:
    ld = number % -10
else:
    ld = number % 10

if ld is 0:
    end = "and is 0"
elif ld < 6 and not 0:
    end = "and is less than 6 and not 0"
else:
    end = "and is greater than 5"

print(sentence.format(number, ld, end))
