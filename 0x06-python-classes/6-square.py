#!/usr/bin/python3
class Square:

    def __init__(self, new_size=0, new_position=(0, 0)):   # initialization
        if not isinstance(new_position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(new_position[0], int) or new_position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(new_position[1], int) or new_position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(new_size, int):
            self.__size = 0
            raise TypeError("size myst be an integer")
        elif new_size < 0:
            self.__size = 0
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size
            self.__position = new_position

    @property
    def position(self):                    # position retriever
        return self.__position

    @position.setter
    def position(self, value):            # position setter
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):                       # size getter
        return self.__size

    @size.setter
    def size(self, value):                 # size setter
        if not isinstance(value, int):
            self.__size = 0
            raise TypeError("size myst be an integer")
            exit
        elif value < 0:
            self.__size = 0
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):              # print square
        if self.__size == 0:
            print('')
        for i in range(0, self.__position[1]):
            print('')
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(' ', end='')
            for j in range(0, self.__size):
                print('#', end='')
            print('')
