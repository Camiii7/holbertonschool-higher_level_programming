#!/usr/bin/python3
"""Define una funcion que devuelve la longitud de una cadena
y su primer caracter"""


def multiple_returns(sentence):
    """
    Retorna una tupla con la longitud de la cadena y su primer caracter

    Args:
        sentence (str): La cadena de texto

    Returns:
        tuple: Una tupla (longitud, primer_caracter)
               Si la cadena esta vacia, devuelve (0, None)
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
