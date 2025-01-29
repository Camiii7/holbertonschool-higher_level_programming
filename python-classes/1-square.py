#!/usr/bin/python3
"""Define una clase Square"""


class Square:
    """Representa un cuadrado"""
    
    def __init__(self, size):
        """Inicializa un nuevo cuadrado.
        
        Args:
            size (int): El tamaño del nuevo cuadrado.
        """
        self.__size = size
