#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    N = len(my_list)
    if ((idx < 0) or (idx > (N - 1))):
        return my_list
    for i in range(N):
        if i == idx:
            del my_list[i]

    return my_list
