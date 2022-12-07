#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_list = a_dictionary.keys()
    key_list = list(key_list)
    key_list.sort()
    for i in range(len(key_list)):
        key = key_list[i]
        value = a_dictionary[key]
        print("{:s}: {}".format(key, value))
