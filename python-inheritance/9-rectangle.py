#!/usr/bin/python3
"""Modulo que define la clase Rectangle heredada de BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Clase rectangle que hereda de BaseGeometry"""

    def __init__(self, width, height):
        """Inicializa el rectangulo con ancho y altura"""
        

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Devuelve una cadena reprensentando el objeto"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calcula el area del rectangulo"""
        return self.__width * self.__height
