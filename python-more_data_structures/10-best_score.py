#!/usr/bin/python3
def best_score(a_dictionary):
    score = None
    best_key = None

    if not a_dictionary:
        return (None)

    for key in a_dictionary:
        if score is None or a_dictionary[key] > score:
            score = a_dictionary[key]
            best_key = key
    return (best_key)
