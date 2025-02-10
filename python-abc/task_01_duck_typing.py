#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Clase abstracta Shape con metodos abstractos area y perimetro"""


    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Clase Circle que hereda de Shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius

class Rectangle(Shape):
    """Clase Rectangle que hereda de Shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Funcion que imprime el area y perimetro de un objeto que sigue la interfaz Shape"""
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
