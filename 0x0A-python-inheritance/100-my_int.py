#!/usr/bin/pyhton3
""" Write a class MyInt that inherits from int. """


class MyInt(int):
    def __init__(self, num):
        super().__init__()
        self.__num = num

    def __eq__(self, amt):
        if self.__num != amt:
            return True
        else:
            return False

    def __ne__(self, amt):
        if self.__num == amt:
            return True
        else:
            return False
