#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for n in my_list:
        try:
            print("{:d}".format(n), end="")
            count += 1
        except (IndexError, ValueError, TypeError):
            continue

    print("")
    return (count)
