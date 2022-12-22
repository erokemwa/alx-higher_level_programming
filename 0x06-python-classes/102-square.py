#!/usr/bin/python3
class Square:
    __size = 0
    area = 0
    def __init__(self, new_size=0):
        if not isinstance(new_size, int):
            self.size = 0
            raise TypeError("size myst be an integer")
        elif new_size < 0:
            self.size = 0
            raise ValueError("size must be >= 0")
        else:
            self.size = new_size
    def size(self, value):
        if not isinstance(value, int):
            self.size = 0
            raise TypeError("size myst be an integer")
            exit
        elif value < 0:
            self.size = 0
            raise ValueError("size must be >= 0")
        else:
            self.size = value
    def size(self):
        return self.size
    def area(self):
        if not isinstance(self.size, int):
            raise TypeError("size myst be an integer")
        return (self.size * self.size)
    def __lt__(self):
        return self.size
