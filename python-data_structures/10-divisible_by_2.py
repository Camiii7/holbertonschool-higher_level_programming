#!/usr/bin/python3
"""Define una funcion que encuentra multiplos de 2 en una lista"""


def divisible_by_2(my_list=[]):
    """
    Determina si los elementos de la lista son multiplos de 2

    Args:
        my_list (list): Lista de enteros

    Return:
        list: Nueva lista con valores booleanos (True o False)
    """
    return [num % 2 == 0 for num in my_list]
