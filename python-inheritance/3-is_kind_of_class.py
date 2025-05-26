#!/usr/bin/python3
"""
returns True if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class ; otherwise False.
    """


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class ;
    otherwise False.

    Args:
        obj (_type_): objet
        a_class (_type_): classe

    Returns:
        true or false : vrai ou faux
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
