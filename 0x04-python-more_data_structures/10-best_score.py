#!/usr/bin/python3


def best_score(a_dictionary):
    for val, key in sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True):
        return val
    if a_dictionary is not True:
        return None
