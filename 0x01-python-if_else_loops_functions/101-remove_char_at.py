#!/usr/bin/python3

def remove_char_at(str, n):
    result = ""
    position = -1
    for i in str:
        position = position + 1
        if (position != n):
            result = result + i

    return (result)
