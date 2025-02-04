#!/usr/bin/python3

class Square:
    """Clase que define un cuadrado"""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con un tamaño y una posicon

        Args:
            size (int): Tamaño del lado del cuadrado (debe ser >= 0
            position (tuple): Posición en la pantalla (tupla de 2 enteros positivos)

        Raises:
            TypeError: Si size no es un entero o position no es una tupla va�lia
            ValueError: Si size es menor que 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtiene el tamaño del cuadrad"""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado con validaciones.

        Args:
            value (int): Nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si value no es un número entero.
            ValueError: Si value es menor que 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Obtiene la posición del cuadrad"""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posicio�n del cuadrado con validaciones.

        Args:
            value (tuple): Nueva posición del cuadrado (debe ser una tupla de 2 enteros positivos).

        Raises:
            TypeError: Si value no es una tupla de dos enteros positivos.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
