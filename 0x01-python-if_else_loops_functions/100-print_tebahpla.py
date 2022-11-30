#!/usr/bin/python3

for i in range(26, 0, -1):
    if i % 2 == 1:
        x = i - 32
    else:
        x = i
    print("{}" .format(chr(x + 96)), end='')
