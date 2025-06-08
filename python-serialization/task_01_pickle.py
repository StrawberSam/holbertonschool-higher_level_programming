#!/usr/bin/python3
import pickle

"""Module pour la sérialisation et désérialisation d'objets
personnalisés avec pickle."""


class CustomObject:
    """Classe représentant un objet personnalisable avec des
    méthodes de sérialisation."""

    def __init__(self, name="", age=None, is_student=None):
        """
        Initialise un objet CustomObject.

        Args:
            name (str): Le nom de la personne.
            age (int or None): L'âge de la personne.
            is_student (bool or None): Indique si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet dans la console.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'objet et l'enregistre dans un fichier binaire.

        Args:
            filename (str): Le nom du fichier de sortie.
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet depuis un fichier binaire.

        Args:
            filename (str): Le nom du fichier à lire.

        Returns:
            CustomObject or None: L'objet désérialisé, ou None si erreur.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return None
