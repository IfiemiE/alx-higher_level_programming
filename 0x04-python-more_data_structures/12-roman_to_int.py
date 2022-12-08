#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    if (roman_string and isinstance(roman_string, str)):
        basic_numeral = {
                            'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000
        }
        num_char = len(roman_string)
        position = 0
        while (position <= (num_char - 1)):
            char = roman_string[position]
            val = basic_numeral[char]
            if (position != (num_char - 1)):
                next_val = basic_numeral[roman_string[position + 1]]
                if val < next_val:
                    val = next_val - val
                    position += 1

            num += val
            position += 1

    return num
