#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    liste_vide = []

    for x in my_list:
        if x % 2 == 0:
            liste_vide.append(True)
        else:
            liste_vide.append(False)
    return (liste_vide)
