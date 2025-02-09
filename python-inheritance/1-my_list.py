#!/usr/bin/python3
"""Define una clase Mylist que hereda de list"""


class MyList(list):
    """Clase que extiende la funcionalidad de list"""

    def print_sorted(self):
        """Imprime la lista ordenada en forma ascendente sin modificarla"""

        print(sorted(self))
