#!/usr/bin/python3

def multiple_returns(sentence):
    first = len(sentence)
    if first != 0:
        second = sentence[0]
    else:
        second = None

    return (first, second)
