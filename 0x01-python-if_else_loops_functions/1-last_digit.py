#!/usr/bin/python3
""" Gets last digit of a number """


import random
number = random.randint(-10000, 10000)

sentence = "Last digit of {0} is {1} {2}"
ld = number % 10
five = "and is greater than 5"
lessthan = "and is less than 6 and not 0"
zero = "and is 0"
if ld > 5:
    print(sentence.format(number, ld, five))
elif ld == 0:
    print(sentence.format(number, ld, zero))
else:
    if number < 0:
        new = (number * -1) % 10
        print(sentence.format(number, new, lessthan * -1))
    else:
        print(sentence.format(number, new, lessthan))

