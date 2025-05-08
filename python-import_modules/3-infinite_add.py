#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv)  # Récupère les args en prenant le nom du script
    add = 0  # Stock la somme des arguments

    for i in range(1, count):  # Boucle qui commence par le 1er arg
        add += int(sys.argv[i])  # Convertit l'arg en entier et le met dans add

    print("{}".format(add))  # Print le résultat
