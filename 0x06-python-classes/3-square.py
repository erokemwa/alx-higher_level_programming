#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, new_size=0):
        if not isinstance(new_size, int):
            self.__size = 0
            raise TypeError("size myst be an integer")
        elif new_size < 0:
            self.size = 0
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        return (self.__size * self.__size)
