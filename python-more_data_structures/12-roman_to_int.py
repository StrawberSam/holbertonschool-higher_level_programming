#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)

    dictionary = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }

    total = 0
    i = 0

    while i < len(roman_string):
        if (
            i + 1 < len(roman_string)
            and dictionary[roman_string[i]] < dictionary[roman_string[i + 1]]
           ):
            total += (
                dictionary[roman_string[i + 1]] -
                dictionary[roman_string[i]]
            )

            i += 2  # Skip the next symbol

        else:
            total += dictionary[roman_string[i]]
            i += 1
    return (total)
