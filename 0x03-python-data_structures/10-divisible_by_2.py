#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        N = len(my_list)
        if N != 0:
            new_list = []
            for i in range(N):
                rem = (my_list[i] % 2)
                if rem == 0:
                    new_list.append(True)
                else:
                    new_list.append(False)

        return new_list
