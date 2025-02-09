#!/usr/bin/python3
"""Modulo que define la clase Square heredada de rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Clase Squiare que hereda de rectangle"""

    def __init__(self, size):
        """Inicializa el cuadrado con el tamao size"""
        self.integer_validator("size", size)
        self.__size = size


        super().__init__(self.__size, self.__size)

    def area(self):
        """Calcula el area del cuadrado"""
        return self.__size * self.__size

    def __str__(self):
        """Devuelve una cadena representando el cuadrado"""
        return f"[Square] {self.__size}/{self.__size}"
