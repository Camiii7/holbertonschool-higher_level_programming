#!/usr/bin/python3
"""Define la clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0):
        """
        Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamano del lado del cuadrado es 0
        """
        self.size = size

    @property
    def size(self):
        """
        Obtiene el tamano del cuadrado

        Return:
            int: El tamano actual del cuadrado
            """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Establece el tamano del cuadrado con validaciones

        Args:
            value (int): Nuevo tamano del cuadrado.

        Raises:
            TypeError: Si value no es un numero entero
            ValueError: Si value es menor que 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcula el area del cuadrado

        Returns:
            int: El area del cuadrado
        """
        return self.__size ** 2
