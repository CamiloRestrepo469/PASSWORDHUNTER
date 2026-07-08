"""
=========================================================
Módulo: jugador.py
Proyecto: Password Hunter - The Ancient Vaults

Este módulo contiene la clase Jugador, encargada de
representar al jugador dentro del juego.

El jugador posee un nombre y un sistema de puntaje
que se actualiza a medida que abre cofres.

Autor: Camilo Restrepo
=========================================================
"""

# ==========================================================
# IMPORTACIONES
# ==========================================================

from src.puntaje import Puntaje


# ==========================================================
# CLASE JUGADOR
# ==========================================================

class Jugador:
    """
    =====================================================
    CLASE JUGADOR
    =====================================================

    Representa al jugador dentro del juego.

    Responsabilidades
    -----------------
    • Almacenar el nombre del jugador.
    • Administrar el puntaje.
    • Mostrar la información del jugador.
    • Reiniciar la partida cuando sea necesario.
    """

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(self, nombre: str):
        """
        Constructor de la clase.

        Parámetros
        ----------
        nombre : str
            Nombre del jugador.
        """

        self.nombre = nombre
        self.puntaje = Puntaje()

    # =====================================================
    # AGREGAR PUNTOS
    # =====================================================

    def agregar_puntos(self, puntos: int):
        """
        Agrega puntos al jugador.

        Parámetros
        ----------
        puntos : int
            Cantidad de puntos recibidos.
        """

        self.puntaje.actualizar(puntos)

    # =====================================================
    # OBTENER PUNTAJE
    # =====================================================

    def obtener_puntaje(self) -> int:
        """
        Devuelve el puntaje actual del jugador.

        Retorna
        -------
        int
            Puntaje acumulado.
        """

        return self.puntaje.obtener()

    # =====================================================
    # REINICIAR JUGADOR
    # =====================================================

    def reiniciar(self):
        """
        Reinicia el puntaje del jugador.

        Se utiliza cuando comienza una nueva partida.
        """

        self.puntaje.reiniciar()

    # =====================================================
    # MOSTRAR INFORMACIÓN
    # =====================================================

    def mostrar_estado(self):
        """
        Muestra la información actual del jugador.
        """

        print("\n" + "=" * 55)
        print("INFORMACIÓN DEL JUGADOR")
        print("=" * 55)
        print(f"Jugador : {self.nombre}")
        print(f"Puntaje : {self.obtener_puntaje()} puntos")
        print("=" * 55)

    # =====================================================
    # REPRESENTACIÓN EN TEXTO
    # =====================================================

    def __str__(self):
        """
        Devuelve una representación en texto del jugador.
        """

        return (
            f"Jugador: {self.nombre} | "
            f"Puntaje: {self.obtener_puntaje()} puntos"
        )