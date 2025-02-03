#!/usr/bin/python3
"""Define la clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0):
        """
        Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamaño del lado del cuadrad es 0
        """
        self.size = size

    @property
    def size(self):
        """
        Obtiene el tamaño del cuadrad

        Return:
            int: El tamaño actual del cuadrad
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Establece el tamaño del cuadrado con validacione

        Args:
            value (int): Nuevo tamaño del cuadrad

        Raises:
            TypeError: Si value no es un número enter
            ValueError: Si value es menor que 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcula el area del cuadrad

        Return:
            int: El area del cuadrad
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el caracter #.

        Si size es 0, imprime una linea vacia.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
