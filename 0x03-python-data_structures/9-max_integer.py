#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = None
    if my_list:
        N = len(my_list)
        if N == 0:
            return None
        max_num = my_list[0]
        for i in range(1, N):
            if (max_num < my_list[i]):
                swap = max_num
                max_num = my_list[i]
                my_list[i] = swap

    return max_num
