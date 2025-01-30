#!/usr/bin/python3
"""Define una clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamaño del lado del cuadrado. Por defecto, es 0.

        Raises:
            TypeError: Si size no es un número entero.
            ValueError: Si size es menor que 0.
        """
        self.size = size  # Usa el setter para validaciones

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece un nuevo tamaño para el cuadrado con validaciones.

        Args:
            value (int): Nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si value no es un nu�mero entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

