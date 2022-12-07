#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [None] * len(my_list)
    for i in range(0, len(my_list)):
        if my_list[i] is search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]
    return new_list
