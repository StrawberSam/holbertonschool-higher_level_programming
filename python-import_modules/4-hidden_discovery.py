#!/usr/bin/python3

import importlib.util
# On importe le module 'importlib.util' qui permet de charger un module à
# partir de son fichier .pyc
# Cela nous aide à importer dynamiquement le fichier compilé 'hidden_4.pyc'
# au lieu d'un fichier source .py normal


def main():
    """Print all names defined by hidden_4 module."""
    # Ceci est la fonction principale qui va afficher tous les noms définis
    # dans le module 'hidden_4'

    path = "/tmp/hidden_4.pyc"  # Spécifie le chemin du fichier compilé .pyc
    # Ici, nous indiquons le chemin où se trouve le fichier 'hidden_4.pyc'
    # sur la sandbox

    # Charge le module depuis le fichier .pyc
    spec = importlib.util.spec_from_file_location("hidden_4", path)
    # On crée un "spécificateur" (spec) pour le module 'hidden_4' en utilisant
    # le chemin du fichier .pyc
    # Ce spécificateur contient toutes les informations nécessaires pour
    # charger le module

    hidden_4 = importlib.util.module_from_spec(spec)
    # Avec 'spec', on crée un objet module vide. Cet objet module représentera
    # notre module 'hidden_4'

    spec.loader.exec_module(hidden_4)
    # 'exec_module' exécute le code du module (dans ce cas, 'hidden_4.pyc') et
    # charge toutes les fonctions, classes, etc. définies dedans
    # Ainsi, le module 'hidden_4' devient disponible pour être utilisé dans
    # notre script

    # Fonction qui retourne la liste de tous les noms définis dans un module
    names = dir(hidden_4)
    # 'dir(hidden_4)' retourne une liste de tous les attributs
    # (fonctions, variables, etc.) définis dans le module 'hidden_4'
    # Cela inclut à la fois les noms visibles et les noms spéciaux

    for name in sorted(names):
        # On parcourt cette liste de noms, triée par ordre alphabétique
        # (grâce à sorted)
        # On souhaite afficher ces noms dans un ordre alphabétique pour rendre
        # les résultats plus lisibles

        if not name.startswith("__"):  # Filtre les noms en __
            # Si un nom ne commence pas par '__' (qui désigne généralement les
            # noms spéciaux comme __init__, __str__...)
            # On l'affiche. Cela permet de ne pas afficher les noms internes
            # utilisés par Python, qui sont souvent privés.
            print(name)


if __name__ == "__main__":
    main()
