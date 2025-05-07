#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10 # Transforme le nbr en val absolue
    print("{}".format(last_digit), end="")
    return last_digit
# Abs sert à transformer le nbr en valeur absolue(pour nombre négatif)
