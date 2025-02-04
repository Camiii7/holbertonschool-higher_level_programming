#!/usr/bin/python3
"""Define una funcion para imprimir una matriz de enteros"""


def print_matrix_integer(matrix=[[]]):
    """
    Imprime una matriz de enteros

    Args:
        matrix (list): Una lista de listas que contiene enteros

    Return:
        None
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
