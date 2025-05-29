#!/usr/bin/python3
"""
Ce module démontre l'utilisation des mixins en Python pour composer
des comportements dans une classe de manière modulaire et réutilisable.

Classes fournies :
- SwimMixin : ajoute un comportement de nage.
- FlyMixin : ajoute un comportement de vol.
- Dragon : créature mythique capable de nager, voler et rugir.
"""


class SwimMixin:
    """Mixin qui ajoute la capacité de nager à une classe."""

    def swim(self):
        """Affiche que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin qui ajoute la capacité de voler à une classe."""

    def fly(self):
        """Affiche que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe représentant un dragon mythique.

    Hérite de SwimMixin et FlyMixin pour obtenir les comportements
    de nage et de vol.
    Possède également un comportement propre : rugir.
    """

    def roar(self):
        """Affiche que le dragon rugit."""
        print("The dragon roars!")
