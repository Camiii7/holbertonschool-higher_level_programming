#!/usr/bin/python3
"""Define una funcion para sumar dos tuplas"""


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Suma los dos primeros elementos de dos tuplas

    Args:
        tuple_a (tuple): Primera tupla
        tuple_b (tuple): Segunda tupla

    Return:
        tuple: Una nueva tupla con la suma de los dos primeros elementos
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
