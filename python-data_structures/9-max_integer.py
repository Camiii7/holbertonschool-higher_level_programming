#!/usr/bin/python3
"""Define una funcion que encuentra el entero mas grande en una lista"""


def max_integer(my_list=[]):
    """
    Encuentra el numero mas grande en una lista de enteros

    Args:
        my_list (list): lista de enteros

    Returns:
        int: El numero mas grande en la lista, o None si la lista esta vacia
    """
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
