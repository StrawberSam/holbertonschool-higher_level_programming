#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.

    Args:
        obj (_type_): un objet
        a_class (_type_): une classe

    Returns:
        True/false: Vrai ou faux
    """
    if type(obj) == a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False

