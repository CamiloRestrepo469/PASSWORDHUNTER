"""
=========================================================
Módulo: puntaje.py
Proyecto: Password Hunter - The Ancient Vaults

Este módulo contiene la clase Puntaje, encargada de
administrar el puntaje acumulado del jugador durante
toda la partida.

Autor: Camilo Restrepo
=========================================================
"""


# ==========================================================
# CLASE PUNTAJE
# ==========================================================

class Puntaje:
    """
    =====================================================
    CLASE PUNTAJE
    =====================================================

    Esta clase administra el puntaje del jugador.

    Responsabilidades
    -----------------
    • Almacenar el puntaje.
    • Sumar puntos.
    • Restar puntos.
    • Reiniciar el puntaje.
    • Mostrar el puntaje actual.
    """

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(self):
        """
        Constructor de la clase.

        Todo jugador inicia la partida con
        cero (0) puntos.
        """

        self.__puntaje = 0

    # =====================================================
    # AGREGAR PUNTOS
    # =====================================================

    def agregar(self, puntos: int):
        """
        Agrega puntos al marcador.

        Parámetros
        ----------
        puntos : int
            Cantidad de puntos que se sumarán.
        """

        self.__puntaje += puntos

    # =====================================================
    # DESCONTAR PUNTOS
    # =====================================================

    def descontar(self, puntos: int):
        """
        Descuenta puntos del marcador.

        Parámetros
        ----------
        puntos : int
            Cantidad de puntos que serán
            descontados.
        """

        self.__puntaje -= puntos

    # =====================================================
    # ACTUALIZAR PUNTAJE
    # =====================================================

    def actualizar(self, puntos: int):
        """
        Actualiza automáticamente el puntaje.

        Si el valor recibido es positivo,
        suma puntos.

        Si el valor recibido es negativo,
        resta puntos.

        Parámetros
        ----------
        puntos : int
            Valor recibido desde un cofre.
        """

        self.__puntaje += puntos

    # =====================================================
    # OBTENER PUNTAJE
    # =====================================================

    def obtener(self) -> int:
        """
        Devuelve el puntaje actual.

        Retorna
        -------
        int
            Puntaje acumulado.
        """

        return self.__puntaje

    # =====================================================
    # REINICIAR PUNTAJE
    # =====================================================

    def reiniciar(self):
        """
        Reinicia el puntaje del jugador.

        Se utiliza cuando inicia una nueva
        partida.
        """

        self.__puntaje = 0

    # =====================================================
    # MOSTRAR PUNTAJE
    # =====================================================

    def mostrar(self):
        """
        Muestra en pantalla el puntaje
        acumulado.
        """

        print("\n" + "=" * 55)
        print("PUNTAJE ACTUAL")
        print("=" * 55)
        print(f"Puntos acumulados: {self.__puntaje}")
        print("=" * 55)

    # =====================================================
    # REPRESENTACIÓN EN TEXTO
    # =====================================================

    def __str__(self):
        """
        Devuelve una representación en texto
        del puntaje.
        """

        return f"Puntaje actual: {self.__puntaje} puntos"