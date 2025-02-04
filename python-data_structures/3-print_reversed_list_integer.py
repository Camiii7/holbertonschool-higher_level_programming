#!/usr/bin/python3
"""
Define una función para imprimir una lista de enteros en orden inverso.
"""


def print_reversed_list_integer(my_list=[]):
    """
    Imprime todos los enteros de una lista en orden inverso.

    Args:
        my_list (list): Lista de enteros.
    """
    if my_list:
        for num in reversed(my_list):
            print("{:d}".format(num))
