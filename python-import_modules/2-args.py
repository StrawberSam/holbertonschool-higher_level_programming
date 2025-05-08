#!/usr/bin/python3
import sys  # Importation du module sys pour accéder aux args de la lgn de cmd

if __name__ == "__main__":
    args = sys.argv[1:]  # Récupère les args en ignorant le nom du script
    count = len(args)

    #  Affiche un msg en fonction du nombre d'arguments
    if count == 0:
        print("0 arguments.")

    elif count == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(count))

    # boucle for pour afficher chaque argument avec le numéro
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
        # 'arg' représente un seul argument de la liste 'args'
