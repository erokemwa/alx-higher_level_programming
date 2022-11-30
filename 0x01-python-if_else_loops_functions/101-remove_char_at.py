#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    nstr = ''
    for c in str:
        if i != n:
            nstr = nstr + c
        i = i + 1
    return nstr
