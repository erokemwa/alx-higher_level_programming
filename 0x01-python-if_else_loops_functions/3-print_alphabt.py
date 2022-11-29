#!/usr/bin/python3
# prints alphabet

for i in range(0, 26):
    if i != 4 and i != 16:
        print("{:s}" .format(chr(i + 97)), end='')
