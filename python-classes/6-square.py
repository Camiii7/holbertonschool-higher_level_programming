#!/usr/bin/python3
"""Define la clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamaño del lado del cuadrad es 0
            position (tuple): Posicion del cuadrad
        

        Raises:
        TypeError: Si size no es un numero entero o position no es una tupla de 2 enteros positivos
        ValueError: Si size es menor que 0

        
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Obtiene el tamaño del cuadrao

        Return:
            int: El tamaño actual del cuadrad
        """
        return self.__size

    def position(self):
        """Obtiene la posicion del cuadrad"""
        return self.__position

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

    def position(self, value):
        """Establece la posición del cuadrado con validacione

        Args:
            value (tuple): Nueva posición del cuadrado.

        Raises:
            TypeError: Si value no es una tupla de 2 enteros positivos.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcula el area del cuadrad

        Return:
            int: El area del cuadrad
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el caracter # con la posicion especificada

        Si size es 0, imprime una linea vacia.
        """
        if self.__size == 0:
            print("")
        
        return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
      
