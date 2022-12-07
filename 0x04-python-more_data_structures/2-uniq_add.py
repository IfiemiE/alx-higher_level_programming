#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_sum = 0
    if my_list:
        for i in range(len(my_list)):
            seen = False
            for j in range(0, i):
                if my_list[j] == my_list[i]:
                    seen = True
                    break
            if seen == False:
                uniq_sum += my_list[i]

    return uniq_sum
