#!/usr/bin/python3
"""
Ce module définit une classe Student simple avec une méthode permettant
de récupérer une représentation en dictionnaire pour une sérialisation JSON.
"""


class Student:
    """
    Représente un étudiant avec un prénom, un nom et un âge.
    Fournit une méthode pour convertir l'instance en dictionnaire.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """
        Retourne une représentation de l'instance sous forme de dictionnaire.

        Si un paramètre `attrs` est fourni et qu'il s'agit d'une liste de
        chaînes, seule une sélection des attributs spécifiés sera incluse dans
        le dictionnaire. Sinon, tous les attributs de l'instance seront
        retournés.

        Args:
            attrs (list, optionnel): Liste de chaînes représentant les noms
            d'attributs à inclure. Si None ou invalide, tous les attributs
            sont retournés.

        Retourne :
            dict : Un dictionnaire contenant les attributs demandés de
            l'étudiant.
        """

        if not isinstance(attrs, list) or attrs is None:
            return self.__dict__
        else:
            new_dic = {}
            for element in attrs:
                if element in self.__dict__:
                    new_dic[element] = self.__dict__[element]
            return new_dic
