#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_set = []
    for turns in range(2):
        if turns == 0:
            base_set = set_1
            check_set = set_2
        else:
            base_set = set_2
            check_set = set_1

        for entry_b in base_set:
            seen = False
            for entry_c in check_set:
                if entry_b == entry_c:
                    seen = True
                    break
            if (not seen):
                diff_set.append(entry_b)

    return set(diff_set)
