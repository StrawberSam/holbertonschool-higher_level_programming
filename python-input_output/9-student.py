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

    def to_json(self):
        """
        Retourne une représentation de l'instance sous forme de dictionnaire.

        Retourne :
        dict : Un dictionnaire contenant les attributs de l'étudiant.
        """
        return self.__dict__
