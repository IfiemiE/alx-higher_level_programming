#!/usr/bin/python3

def common_elements(set_1, set_2):
    inter_set = []
    if (len(set_1) != 0) and (len(set_2) != 0):
        for entry1 in set_1:
            for entry2 in set_2:
                if entry1 == entry2:
                    inter_set.append(entry1)

    return set(inter_set)
