#!/usr/bin/python3
if __name__ == "__main__":  # Protection d'execution
    from add_0 import add  # Importation de la fonction add depuis add_0
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
