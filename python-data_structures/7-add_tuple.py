#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    a = (a0, a1)

    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    b = (b0, b1)

    somme_1 = a[0] + b[0]
    somme_2 = a[1] + b[1]
    new_tuple = (somme_1, somme_2)
    return (new_tuple)
