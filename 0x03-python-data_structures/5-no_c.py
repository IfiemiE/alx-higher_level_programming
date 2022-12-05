#!/usr/bin/python3
def no_c(my_string):
    C_less_string = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            C_less_string += i
    return C_less_string
