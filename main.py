"""
=========================================================
Archivo: main.py
Proyecto: Password Hunter - The Ancient Vaults

Punto de entrada principal del programa.

Autor: Camilo Restrepo
=========================================================
"""
from src.juego import JuegoCazador


def main():
    """
    Función principal del programa.
    """

    juego = JuegoCazador()

    juego.ejecutar()


if __name__ == "__main__":
    main()