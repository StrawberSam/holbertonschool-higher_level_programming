#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:  # On parcourt les lignes
        for i in range(len(row)):
            if i != len(row) - 1:  # On cherche le dernier element
                print("{:d}".format(row[i]), end=" ")  # Un espace
            else:
                print("{:d}".format(row[i]), end="")  # Pas d'espace
        print()
