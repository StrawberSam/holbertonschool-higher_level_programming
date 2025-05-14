#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    somme = 0

    for number in my_list:
        if number in unique:
            continue
        else:
            unique.append(number)
            somme += number

    return (somme)
