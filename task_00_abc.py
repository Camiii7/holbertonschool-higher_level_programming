#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """clase abstracta Animal"""


    @abstractmethod
    def sound(self):
        """Metodo abstracto que debe ser implementado en las clases hijas"""
        pass

class Dog(Animal):
    """Clase que representa a un perro, heredando de animal"""

    def sound(self):
        """Implementacion del metodo sound para Dog"""
        return "Bark"

class Cat(Animal):
    "Clase que representa a un gato, hereda de Animal"""

    def sound(self):
            """Implementacion del metodo sound para Cat"""
            return "Meow"
