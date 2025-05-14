#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for ligne in matrix:
        nouvelle_ligne = []
        for nombre in ligne:
            result = nombre * nombre
            nouvelle_ligne.append(result)
        new_matrix.append(nouvelle_ligne)

    return (new_matrix)
