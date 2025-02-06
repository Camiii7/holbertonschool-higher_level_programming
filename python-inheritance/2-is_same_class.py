#!/usr/bin/python3
"""Define la funcion is_same_class"""


def is_same_class(obj, a_class):
    """
    Verifica si el objeto es exactamente una instancia de la clase especificada

    Args:
        obj: El objeto a verificar
        a_class: La clase a comparar

    Return:
        bool: True si obj es exactamente una instancia de a_class,
        false en caso que no 
    """
    return type(obj) == a_class
