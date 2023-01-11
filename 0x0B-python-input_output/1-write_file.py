#!/usr/bin/python3

"""writes to a file"""


def write_file(filename="", text=""):
    """a function to write to a file and
    return number of charcaters written"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
