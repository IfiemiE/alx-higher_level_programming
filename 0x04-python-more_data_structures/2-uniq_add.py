#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_sum = 0
    for i in range(len(my_list)):
        seen = False
        for j in range(0, i):
            if my_list[j] == my_list[i]:
                seen = True
                break
        if (not seen):
            uniq_sum += my_list[i]

    return uniq_sum
