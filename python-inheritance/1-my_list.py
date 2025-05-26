#/!usr/bin/python3
""" function that prints the list, but sorted (ascending sort)
    """
class MyList(list):
    """prints the list, but sorted (ascending sort)

    Args:
        list (class): Class list
    """
    def print_sorted(self):
        print(sorted(self))
