"""
=========================================================
Módulo: eventos.py
Proyecto: Password Hunter - The Ancient Vaults

Este módulo contiene la clase Eventos, encargada de
mostrar todos los mensajes e interfaces del juego.

Autor: Camilo Restrepo
=========================================================
"""


# ==========================================================
# CLASE EVENTOS
# ==========================================================

class Eventos:
    """
    =====================================================
    CLASE EVENTOS
    =====================================================

    Esta clase centraliza todos los mensajes del juego.

    Responsabilidades
    -----------------
    • Mostrar el título principal.
    • Mostrar separadores.
    • Mostrar mensajes informativos.
    • Mostrar mensajes de error.
    • Mostrar despedidas.
    """

    @staticmethod
    def titulo():
        """
        Muestra el título principal del juego.
        """

        print("\n" + "=" * 60)
        print("        PASSWORD HUNTER - THE ANCIENT VAULTS")
        print("=" * 60)

    @staticmethod
    def separador():
        """
        Imprime un separador.
        """

        print("-" * 60)

    @staticmethod
    def bienvenida(nombre):
        """
        Da la bienvenida al jugador.

        Parámetros
        ----------
        nombre : str
            Nombre del jugador.
        """

        print(f"\n¡Bienvenido, {nombre}!")
        print("Tu misión será abrir los antiguos cofres.")
        print("Cada contraseña válida puede darte grandes recompensas.")

    @staticmethod
    def mensaje(texto):
        """
        Muestra un mensaje general.

        Parámetros
        ----------
        texto : str
            Mensaje a mostrar.
        """

        print(f"\n>> {texto}")

    @staticmethod
    def error(texto):
        """
        Muestra un mensaje de error.

        Parámetros
        ----------
        texto : str
            Error ocurrido.
        """

        print("\n[ERROR]")
        print(texto)

    @staticmethod
    def despedida():
        """
        Mensaje final del juego.
        """

        print("\n" + "=" * 60)
        print("Gracias por jugar Password Hunter.")
        print("¡Hasta la próxima aventura!")
        print("=" * 60)