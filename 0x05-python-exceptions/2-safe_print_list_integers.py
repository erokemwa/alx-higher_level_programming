#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
                print("{:d}".format(my_list[i]), end='')
        except (TypeError, ValueError):
                i = i - 2
    i = i + 1
    print('')
    return i
