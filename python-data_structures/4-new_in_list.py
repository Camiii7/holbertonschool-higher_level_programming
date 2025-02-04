#!/usr/bin/python3
"""Define una funcion para reemplazar un elemento en una copia de una lisa"""


def new_in_list(my_list, idx, element):
    """ Reemplaza un elemento en una lista en una posicion
    espeifica sin modificar la original

    Args:
        my_list (list): Lista original
        idx (int): Indice donde se quiere reemplazar un elemento
        element (any): Nuevo elemento a insertar

    Return:
        lista: Una nueva lista con el elemento reemplazado,
        o una copia de la original si idx es invalida
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
