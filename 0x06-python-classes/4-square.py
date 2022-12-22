#!/usr/bin/python3
class Square:

    def __init__(self, new_size=0):
        if not isinstance(new_size, int):
            self.__size = 0
            raise TypeError("size must be an integer")
            exit
        elif new_size < 0:
            self.__size = 0
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            self.__size = 0
            raise TypeError("size must be an integer")
            exit
        elif value < 0:
            self.__size = 0
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
