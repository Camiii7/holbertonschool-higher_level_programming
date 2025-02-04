#!/usr/bin/python3
"""Define una funcion que elimina un elemento en una posicion dada de una lista"""


def delete_at(my_list=[], idx=0):
    """
    Elimina el elemento en la posicion especificada de la lista

    Args:
        my_list (list): La lista original
        idx (int): Indice del elemento a eliminar

    Returns:
        list: lista modificada sin el elemento en la posicion idx
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
