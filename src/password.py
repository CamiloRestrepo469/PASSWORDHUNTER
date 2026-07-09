"""
=========================================================
Módulo: password.py
Proyecto: Password Hunter - The Ancient Vaults

Clase encargada de generar y validar contraseñas
seguras para el juego.

- Algoritmo de generación equilibrado.
- Métodos privados.
- Código reutilizable.
- Totalmente documentado.

Autor: Camilo Restrepo
=========================================================
"""

# ==========================================================
# IMPORTACIONES
# ==========================================================

import random
import string

from src.excepciones import (
    LongitudInvalida,
    PasswordInvalida,
)


class Password:
    """
    =========================================================
    CLASE PASSWORD
    =========================================================

    Esta clase representa el motor encargado de generar y
    validar contraseñas para el juego Password Hunter.

    Responsabilidades
    -----------------
    • Generar contraseñas completamente aleatorias.
    • Garantizar que no existan caracteres repetidos.
    • Distribuir equilibradamente los tipos de caracteres.
    • Validar que la contraseña cumpla todas las reglas.
    """

    # =====================================================
    # CONSTANTES
    # =====================================================

    MAYUSCULAS = list(string.ascii_uppercase)

    MINUSCULAS = list(string.ascii_lowercase)

    NUMEROS = list(string.digits)

    ESPECIALES = list("¿¡?=)(/¨*+-%&$#!")

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(self):
        """
        Constructor de la clase.

        Calcula la cantidad máxima de caracteres únicos
        disponibles para evitar que el usuario solicite una
        contraseña imposible de generar.
        """

        self.total_caracteres = (
            len(self.MAYUSCULAS)
            + len(self.MINUSCULAS)
            + len(self.NUMEROS)
            + len(self.ESPECIALES)
        )

    # =====================================================
    # MÉTODO PRINCIPAL
    # =====================================================

    def generar(self, longitud: int) -> str:
        """
        Genera una contraseña completamente aleatoria.

        Parámetros
        ----------
        longitud : int

        Retorna
        -------
        str

        Excepciones
        -----------
        LongitudInvalida
        """

        # ---------------------------------------------
        # Validar longitud mínima
        # ---------------------------------------------

        if longitud < 8:
            raise LongitudInvalida(longitud)

        # ---------------------------------------------
        # Validar longitud máxima
        # ---------------------------------------------

        if longitud > self.total_caracteres:
            raise PasswordInvalida(
                f"La longitud máxima permitida es "
                f"{self.total_caracteres} caracteres."
            )

        # ---------------------------------------------
        # Calcular distribución equilibrada
        # ---------------------------------------------

        distribucion = self._calcular_distribucion(longitud)

        password = []

        utilizados = set()

        # ---------------------------------------------
        # Agregar mayúsculas
        # ---------------------------------------------

        password.extend(
            self._generar_bloque(
                self.MAYUSCULAS,
                distribucion["mayusculas"],
                utilizados
            )
        )

        # ---------------------------------------------
        # Agregar minúsculas
        # ---------------------------------------------

        password.extend(
            self._generar_bloque(
                self.MINUSCULAS,
                distribucion["minusculas"],
                utilizados
            )
        )

        # ---------------------------------------------
        # Agregar números
        # ---------------------------------------------

        password.extend(
            self._generar_bloque(
                self.NUMEROS,
                distribucion["numeros"],
                utilizados
            )
        )

        # ---------------------------------------------
        # Agregar caracteres especiales
        # ---------------------------------------------

        password.extend(
            self._generar_bloque(
                self.ESPECIALES,
                distribucion["especiales"],
                utilizados
            )
        )

        # ---------------------------------------------
        # Mezclar completamente la contraseña
        # ---------------------------------------------

        random.shuffle(password)

        return "".join(password)

    # =====================================================
    # MÉTODOS PRIVADOS
    # =====================================================

    def _calcular_distribucion(self, longitud: int) -> dict:
        """
        Calcula cuántos caracteres de cada categoría tendrá
        la contraseña.

        El objetivo es obtener una contraseña equilibrada.

        Retorna un diccionario con la cantidad de:

        - mayúsculas
        - minúsculas
        - números
        - especiales
        """

        base = longitud // 4

        distribucion = {
            "mayusculas": base,
            "minusculas": base,
            "numeros": base,
            "especiales": base,
        }

        restante = longitud - (base * 4)

        categorias = [
            "mayusculas",
            "minusculas",
            "numeros",
            "especiales",
        ]

        while restante > 0:

            categoria = random.choice(categorias)

            distribucion[categoria] += 1

            restante -= 1

        return distribucion

    def _generar_bloque(
        self,
        caracteres: list,
        cantidad: int,
        utilizados: set
    ) -> list:
        """
        Genera un bloque de caracteres únicos.

        Parámetros
        ----------
        caracteres : list
            Lista de caracteres disponibles.

        cantidad : int
            Cantidad de caracteres que se deben generar.

        utilizados : set
            Conjunto que almacena los caracteres ya
            utilizados para impedir repeticiones.
        """

        bloque = []

        while len(bloque) < cantidad:

            caracter = self._obtener_caracter_unico(
                caracteres,
                utilizados
            )

            bloque.append(caracter)

        return bloque

    def _obtener_caracter_unico(
        self,
        caracteres: list,
        utilizados: set
    ) -> str:
        """
        Obtiene un único carácter aleatorio que todavía
        no haya sido utilizado anteriormente.
        """

        while True:

            caracter = random.choice(caracteres)

            if caracter not in utilizados:

                utilizados.add(caracter)

                return caracter
    # =====================================================
    # MÉTODOS DE VALIDACIÓN
    # =====================================================

    def validar(self, password: str) -> bool:
        """
        Valida que una contraseña cumpla todas las reglas
        establecidas por el juego.

        Parámetros
        ----------
        password : str
            Contraseña que será validada.

        Retorna
        -------
        bool
            True cuando la contraseña es completamente
            válida.

        Excepciones
        -----------
        PasswordInvalida
            Si alguna regla no se cumple.
        """

        # ---------------------------------------------
        # Validar longitud mínima
        # ---------------------------------------------

        if len(password) < 8:
            raise PasswordInvalida(
                "La contraseña tiene menos de 8 caracteres."
            )

        # ---------------------------------------------
        # Ejecutar todas las validaciones
        # ---------------------------------------------

        self.tiene_mayusculas(password)
        self.tiene_minusculas(password)
        self.tiene_numeros(password)
        self.tiene_especiales(password)
        self.sin_repetidos(password)

        return True

    # =====================================================
    # VALIDAR MAYÚSCULAS
    # =====================================================

    def tiene_mayusculas(self, password: str) -> bool:
        """
        Comprueba que exista al menos una letra
        mayúscula.
        """

        if not any(caracter.isupper() for caracter in password):

            raise PasswordInvalida(
                "La contraseña debe contener al menos "
                "una letra mayúscula."
            )

        return True

    # =====================================================
    # VALIDAR MINÚSCULAS
    # =====================================================

    def tiene_minusculas(self, password: str) -> bool:
        """
        Comprueba que exista al menos una letra
        minúscula.
        """

        if not any(caracter.islower() for caracter in password):

            raise PasswordInvalida(
                "La contraseña debe contener al menos "
                "una letra minúscula."
            )

        return True

    # =====================================================
    # VALIDAR NÚMEROS
    # =====================================================

    def tiene_numeros(self, password: str) -> bool:
        """
        Comprueba que exista al menos un número.
        """

        if not any(caracter.isdigit() for caracter in password):

            raise PasswordInvalida(
                "La contraseña debe contener al menos "
                "un número."
            )

        return True

    # =====================================================
    # VALIDAR CARACTERES ESPECIALES
    # =====================================================

    def tiene_especiales(self, password: str) -> bool:
        """
        Comprueba que exista al menos un carácter
        especial permitido.
        """

        if not any(
            caracter in self.ESPECIALES
            for caracter in password
        ):

            raise PasswordInvalida(
                "La contraseña debe contener al menos "
                "un carácter especial."
            )

        return True

    # =====================================================
    # VALIDAR CARACTERES REPETIDOS
    # =====================================================

    def sin_repetidos(self, password: str) -> bool:
        """
        Comprueba que ningún carácter se encuentre
        repetido dentro de la contraseña.

        Si el tamaño del conjunto (set) es diferente
        al tamaño de la cadena, significa que existen
        caracteres duplicados.
        """

        if len(password) != len(set(password)):

            raise PasswordInvalida(
                "La contraseña contiene caracteres "
                "repetidos."
            )

        return True