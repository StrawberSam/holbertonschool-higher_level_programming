#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()

    for element in set_1:
        if element in set_2:
            continue
        else:
            new_set.add(element)
    for element in set_2:
        if element in set_1:
            continue
        else:
            new_set.add(element)
    return (new_set)
