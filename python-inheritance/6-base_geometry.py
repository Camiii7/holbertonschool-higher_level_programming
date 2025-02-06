#!/usr/bin/python3
"""Define la clase BaseGeometric"""


class BaseGeometric:
    """Clase base para geometria"""


    def area(self):
        """Lanza una excepcion indicando que no esta implementado"""
        raise Exception("area() is not implemented")
