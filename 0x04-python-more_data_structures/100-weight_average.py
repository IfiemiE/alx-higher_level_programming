#!/usr/bin/python3

def weight_average(my_list=[]):
    wSum = 0
    Sum = 0
    ave = 0
    if len(my_list) != 0:
        for i in range(len(my_list)):
            pair = my_list[i]
            wSum += (pair[0] * pair[1])
            Sum += pair[1]

        ave = wSum / Sum

    return ave
