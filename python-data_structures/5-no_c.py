#!/usr/bin/python3
def no_c(my_string):
    my_string_2 = ""

    for c in my_string:
        if c != "c" and c != "C":
            my_string_2 += c
    return (my_string_2)
