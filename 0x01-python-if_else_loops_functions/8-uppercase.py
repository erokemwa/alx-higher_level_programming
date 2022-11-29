#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            d = chr(ord(c) - 32)
        else:
            d = c
        print("{:s}".format(d), end='')
    print('')
