#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Define una clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): El tama√±o del lado del cuadrad por defecto, es 0.

        Raises:
            TypeError: Si size no es un nu∫mero entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            uaise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
