#!/usr/bin/python3
"""Finding the peak value in a list"""

def find_peak (values):
    """ Finds the peak of a list
        Arg:
            value (list): list of numbers
        Return: peak/max
    """
    if len(values) == 0:
        peak = None
    else:
        peak = values[0]
        for i in range(1, len(values)):
            if peak < values[i]:
                swap = peak
                peak = values[i]
                values[i] = swap

        return peak
