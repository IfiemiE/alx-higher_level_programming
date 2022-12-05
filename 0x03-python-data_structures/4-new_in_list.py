#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list:
        new_copy = []
        if (idx < 0) or (idx > (len(my_list) - 1)):
            for i in my_list:
                new_copy.append(i)
        else:
            for i in range(len(my_list)):
                if (i == idx):
                    new_copy.append(element)
                else:
                    new_copy.append(my_list[i])
    return new_copy
