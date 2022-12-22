#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, new_size=None):
        if new_size is not None:
            self.__size = new_size
