#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    key_list = list(a_dictionary.keys())
    new_dict = {}
    for key in key_list:
        val = a_dictionary[key]
        new_dict[key] = val * 2

    return (new_dict)
