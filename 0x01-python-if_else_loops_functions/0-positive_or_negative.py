#!/usr/bin/python3
""" Assigns random signed number to var number """


import random
number = random.randint(-10, 10)

number_if_pos = "{} is positive"
number_if_zero = "{} is zero"
number_if_neg = "{} is negative"

if number == 0:
    print(number_if_zero.format(number))
if number > 0:
    print(number_if_pos.format(number))
if number < 0:
    print(number_if_neg.format(number))
