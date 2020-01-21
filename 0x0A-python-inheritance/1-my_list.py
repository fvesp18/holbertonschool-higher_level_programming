#!/usr/bin/python3
""" create inheretence for List from MyList """


class MyList(list):
    def print_sorted(self):
        print("{}".format(sorted(self)))
