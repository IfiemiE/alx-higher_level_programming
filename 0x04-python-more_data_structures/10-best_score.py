#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        key_list = list(a_dictionary.keys())
        best_key = key_list[0]
        best_val = a_dictionary[best_key]
        for key in key_list[1:]:
            val = a_dictionary[key]
            if val > best_val:
                best_key = key
                best_val = val

        return best_key
