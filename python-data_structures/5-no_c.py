#!/usr/bin/python3
""" Define una funcion que elimina todas las letras 'c' y 'C' de una cadena"""


def no_c(my_string):
    """
    Elimina todas las ocurrencias de 'c' y 'C' en una cadena

    Args:
        my_string (str): la cadena original

    Returns:
        str: una nueva cadena sin los caracteres 'c' y 'C'
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
