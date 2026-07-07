"""
=========================================================
Módulo: cofres.py
Proyecto: Password Hunter - The Ancient Vaults

Este módulo contiene la clase Cofre, encargada de
representar los diferentes cofres del juego.

Cada cofre posee un nombre, una cantidad de puntos y un
mensaje que será mostrado al jugador cuando sea abierto.

Autor: Camilo Restrepo
=========================================================
"""

# ==========================================================
# IMPORTACIONES
# ==========================================================

import random


# ==========================================================
# CLASE COFRE
# ==========================================================

class Cofre:
    """
    =====================================================
    CLASE COFRE
    =====================================================

    Representa un cofre dentro del juego.

    Cada cofre tiene:

    • Nombre.
    • Puntos.
    • Mensaje.
    • Rareza.

    El juego utilizará esta clase para crear cofres
    aleatorios cuando una contraseña sea válida.

    Si la contraseña no es válida se utilizará un
    Cofre Maldito.
    """

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(
        self,
        nombre: str,
        puntos: int,
        rareza: str,
        mensaje: str
    ):
        """
        Constructor de la clase.

        Parámetros
        ----------
        nombre : str
            Nombre del cofre.

        puntos : int
            Cantidad de puntos otorgados.

        rareza : str
            Nivel de rareza del cofre.

        mensaje : str
            Descripción que verá el jugador.
        """

        self.nombre = nombre
        self.puntos = puntos
        self.rareza = rareza
        self.mensaje = mensaje

    # =====================================================
    # MOSTRAR INFORMACIÓN
    # =====================================================

    def abrir(self):
        """
        Muestra en pantalla toda la información del cofre.
        """

        print("\n" + "=" * 55)

        print(f"COFRE: {self.nombre}")

        print(f"Rareza: {self.rareza}")

        print()

        print(self.mensaje)

        print()

        if self.puntos >= 0:

            print(f"Puntos obtenidos: +{self.puntos}")

        else:

            print(f"Puntos perdidos: {self.puntos}")

        print("=" * 55)

    # =====================================================
    # COFRE ALEATORIO
    # =====================================================

    @staticmethod
    def obtener_aleatorio():
        """
        Devuelve uno de los cofres positivos del juego.

        Retorna
        -------
        Cofre
        """

        cofres = [

            Cofre(

                nombre="Cofre Común",

                puntos=10,

                rareza="Común",

                mensaje=(
                    "Has encontrado un pequeño cofre de madera.\n"
                    "Dentro había algunas monedas antiguas."
                )
            ),

            Cofre(

                nombre="Cofre Raro",

                puntos=25,

                rareza="Raro",

                mensaje=(
                    "El cofre emite un extraño brillo azul.\n"
                    "Dentro encuentras una valiosa reliquia."
                )
            ),

            Cofre(

                nombre="Cofre Legendario",

                puntos=50,

                rareza="Legendario",

                mensaje=(
                    "Una poderosa energía ilumina el templo.\n"
                    "Has descubierto un tesoro legendario."
                )
            )

        ]

        return random.choice(cofres)

    # =====================================================
    # COFRE MALDITO
    # =====================================================

    @staticmethod
    def obtener_maldito():
        """
        Devuelve el Cofre Maldito.

        Este cofre aparece cuando la contraseña es
        inválida.

        Retorna
        -------
        Cofre
        """

        return Cofre(

            nombre="Cofre Maldito",

            puntos=-20,

            rareza="Maldito",

            mensaje=(
                "La cerradura rechaza tu contraseña.\n"
                "Una antigua maldición consume parte de tu energía."
            )
        )