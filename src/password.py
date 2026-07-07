"""
=========================================================
Módulo: password.py
Proyecto: Password Hunter - The Ancient Vaults

Este módulo contiene la clase Password, encargada de
generar y validar contraseñas seguras para abrir los
cofres del juego.

Autor: Camilo Restrepo
=========================================================
"""

# =========================================================
# IMPORTACIONES
# =========================================================

import random
import string

from src.excepciones import (
    LongitudInvalida,
    PasswordInvalida,
)

# =========================================================
# CLASE PASSWORD
# =========================================================


class Password:
    """
    Clase encargada de generar y validar contraseñas.

    Responsabilidades
    -----------------
    - Generar contraseñas completamente aleatorias.
    - Validar que cumplan todas las reglas del juego.
    - Garantizar que no existan caracteres repetidos.

    Reglas de validación
    --------------------
    ✔ Longitud mínima de 8 caracteres.
    ✔ Al menos una letra mayúscula.
    ✔ Al menos una letra minúscula.
    ✔ Al menos un número.
    ✔ Al menos un carácter especial.
    ✔ Sin caracteres repetidos.
    """

    # Caracteres especiales permitidos por el juego
    CARACTERES_ESPECIALES = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self):
        """
        Constructor de la clase.

        Actualmente no requiere inicializar atributos,
        pero se incluye para mantener una estructura
        consistente y permitir futuras ampliaciones.
        """
        pass

    def generar(self, longitud: int) -> str:
        """
        Genera una contraseña completamente aleatoria.

        Parámetros
        ----------
        longitud : int
            Longitud deseada para la contraseña.

        Retorna
        -------
        str
            Contraseña válida generada aleatoriamente.

        Excepciones
        -----------
        LongitudInvalida
            Si la longitud solicitada es menor que 8.
        """

        if longitud < 8:
            raise LongitudInvalida(longitud)

        mayuscula = random.choice(string.ascii_uppercase)
        minuscula = random.choice(string.ascii_lowercase)
        numero = random.choice(string.digits)
        especial = random.choice(self.CARACTERES_ESPECIALES)

        caracteres = (
            list(string.ascii_letters)
            + list(string.digits)
            + list(self.CARACTERES_ESPECIALES)
        )

        password = [
            mayuscula,
            minuscula,
            numero,
            especial,
        ]

        while len(password) < longitud:

            caracter = random.choice(caracteres)

            if caracter not in password:
                password.append(caracter)

        random.shuffle(password)

        return "".join(password)

    def validar(self, password: str) -> bool:
        """
        Verifica que una contraseña cumpla todas las reglas.

        Parámetros
        ----------
        password : str
            Contraseña que será validada.

        Retorna
        -------
        bool
            True si la contraseña es válida.

        Excepciones
        -----------
        PasswordInvalida
            Cuando alguna regla no se cumple.
        """

        if len(password) < 8:
            raise PasswordInvalida(
                "La contraseña tiene menos de ocho caracteres."
            )

        self.tiene_mayusculas(password)
        self.tiene_minusculas(password)
        self.tiene_numeros(password)
        self.tiene_especiales(password)
        self.sin_repetidos(password)

        return True

    def tiene_mayusculas(self, password: str) -> bool:
        """
        Verifica la existencia de letras mayúsculas.
        """

        if not any(c.isupper() for c in password):
            raise PasswordInvalida(
                "Debe contener al menos una letra mayúscula."
            )

        return True

    def tiene_minusculas(self, password: str) -> bool:
        """
        Verifica la existencia de letras minúsculas.
        """

        if not any(c.islower() for c in password):
            raise PasswordInvalida(
                "Debe contener al menos una letra minúscula."
            )

        return True

    def tiene_numeros(self, password: str) -> bool:
        """
        Verifica la existencia de números.
        """

        if not any(c.isdigit() for c in password):
            raise PasswordInvalida(
                "Debe contener al menos un número."
            )

        return True

    def tiene_especiales(self, password: str) -> bool:
        """
        Verifica la existencia de caracteres especiales.
        """

        if not any(
            c in self.CARACTERES_ESPECIALES
            for c in password
        ):
            raise PasswordInvalida(
                "Debe contener un carácter especial."
            )

        return True

    def sin_repetidos(self, password: str) -> bool:
        """
        Comprueba que no existan caracteres repetidos.
        """

        if len(password) != len(set(password)):
            raise PasswordInvalida(
                "La contraseña contiene caracteres repetidos."
            )

        return True