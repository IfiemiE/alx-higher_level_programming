#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())
    for key in key_list:
        if a_dictionary[key] == value:
            a_dictionary.pop(key, None)

    return a_dictionary
