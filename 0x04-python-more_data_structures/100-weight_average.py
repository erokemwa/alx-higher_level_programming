#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list[0] == None:
        return 0
    ans = 0.0
    for i in range(0, len(my_list)):
        ans += my_list[i][0] * my_list[i][1]
    for i in range(0, len(my_list)):
        ans = ans / my_list[i][1]
    return ans
