#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if i >= len(my_string):
            break
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string = my_string[:i] + my_string[i + 1:]
    return my_string
