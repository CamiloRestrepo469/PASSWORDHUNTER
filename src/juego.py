"""
=========================================================
Módulo: juego.py
Proyecto: Password Hunter - The Ancient Vaults

Este módulo contiene la clase JuegoCazador, encargada
de controlar toda la lógica principal del juego.

Autor: Camilo Restrepo
=========================================================
"""

# ==========================================================
# IMPORTACIONES
# ==========================================================

from src.password import Password
from src.cofres import Cofre
from src.jugador import Jugador
from src.eventos import Eventos
from src.excepciones import (
    LongitudInvalida,
    PasswordInvalida
)


# ==========================================================
# CLASE JUEGOCAZADOR
# ==========================================================

class JuegoCazador:
    """
    =====================================================
    CLASE JUEGOCAZADOR
    =====================================================

    Esta clase administra todo el flujo del juego.

    Responsabilidades
    -----------------
    • Crear el jugador.
    • Generar contraseñas.
    • Validarlas.
    • Abrir cofres.
    • Actualizar el puntaje.
    • Permitir jugar varias rondas.
    """

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(self):
        """
        Inicializa todos los objetos necesarios
        para ejecutar el juego.
        """

        self.password = Password()

        self.jugador = None

    # =====================================================
    # INICIAR JUEGO
    # =====================================================

    def iniciar(self):
        """
        Solicita el nombre del jugador
        e inicia la partida.
        """

        Eventos.titulo()

        nombre = input("\nIngrese su nombre: ").strip()

        if nombre == "":
            nombre = "Cazador"

        self.jugador = Jugador(nombre)

        Eventos.bienvenida(nombre)

    # =====================================================
    # MOSTRAR PUNTAJE
    # =====================================================

    def mostrar_puntaje(self):
        """
        Muestra el puntaje actual.
        """

        self.jugador.mostrar_estado()

    # =====================================================
    # JUGAR UNA RONDA
    # =====================================================

    def jugar_ronda(self):
        """
        Ejecuta una ronda completa del juego.

        Durante una ronda el jugador:

        • Ingresa la longitud de la contraseña.
        • Se genera una contraseña aleatoria.
        • Se valida la contraseña.
        • Se abre un cofre.
        • Se actualiza el puntaje.
        """

        try:

            print()

            longitud = int(
                input("Ingrese la longitud de la contraseña (mínimo 8): ")
            )

            password = self.password.generar(longitud)

            self.password.validar(password)

            Eventos.separador()

            print("\nContraseña generada:\n")

            print(password)

            print()

            cofre = Cofre.obtener_aleatorio()

            cofre.abrir()

            self.jugador.agregar_puntos(cofre.puntos)

            self.mostrar_puntaje()

        except (LongitudInvalida, PasswordInvalida) as error:

            Eventos.error(str(error))

            cofre = Cofre.obtener_maldito()

            cofre.abrir()

            self.jugador.agregar_puntos(cofre.puntos)

            self.mostrar_puntaje()

        except ValueError:

            Eventos.error(
                "Debe ingresar únicamente números enteros."
            )

    # =====================================================
    # PREGUNTAR SI EL JUGADOR DESEA CONTINUAR
    # =====================================================

    def desea_continuar(self) -> bool:
        """
        Pregunta al jugador si desea jugar otra ronda.

        Retorna
        -------
        bool
            True si desea continuar.
            False si desea finalizar el juego.
        """

        while True:

            respuesta = input(
                "\n¿Desea jugar otra ronda? (S/N): "
            ).strip().upper()

            if respuesta == "S":
                return True

            if respuesta == "N":
                return False

            Eventos.error(
                "Respuesta inválida. Escriba únicamente S o N."
            )
    # =====================================================
    # EJECUTAR JUEGO COMPLETO
    # =====================================================

    def ejecutar(self):
        """
        Ejecuta el ciclo principal del juego.

        El jugador podrá jugar tantas rondas
        como desee hasta decidir salir.
        """

        self.iniciar()

        continuar = True

        while continuar:

            self.jugar_ronda()

            continuar = self.desea_continuar()

        Eventos.despedida()

        print()

        print("PUNTAJE FINAL")

        self.jugador.mostrar_estado()