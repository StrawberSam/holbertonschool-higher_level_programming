#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
    """


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an instance
    of the specified class ; otherwise False.

    Args:
        obj (int): nombre
        a_class (class int): type

    Returns:
        true or false : vrai ou faux
    """
    if type(obj) is a_class:
        return True
    else:
        return False
