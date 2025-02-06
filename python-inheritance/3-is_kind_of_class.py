#!/usr/bin/python3
"""Define la funcion is_kind_of_class"""

def is_kind_of_class(obj, a_class):
    """Verifica si el objeto es una instancia de una clase o una subclase
     

     Args:
        obj: el objeto a verificar
        a_class: la clase a comparar

    Return:
        bool: True si obj es una instancia de a_class o una subclase, 
        false en caso que no
    """
    return isinstance(obj, a_class)
