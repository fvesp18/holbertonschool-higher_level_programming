#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        first = sentence[0]
    else:
        first = None
    some_tup = (length, first)

    if sentence and length > 0:
        return some_tup
    else:
        return some_tup
