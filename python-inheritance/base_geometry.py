#!/usr/bin/python3
"""Define la clase BaseGeometry"""


class BaseGeometry:
    """Clase base para operaciones geometricas"""

    def area(self):
        """Manda una excepcion para indicar que el metodo no esta implementado"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un numero entero positivo

        Args:
            name (str): nombre del valor
            value (int): valor a validar 

        Raises:
            TypeError: Si value no es un num etero
            ValueError: Si value es menor o = a 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
