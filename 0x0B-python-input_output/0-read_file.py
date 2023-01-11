#!/usr/bin/python3

"""prints contents of a file"""


def read_file(filename=""):
    """function to read a file"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
