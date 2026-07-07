"""
=========================================================
Módulo: excepciones.py
Proyecto: Password Hunter - The Ancient Vaults

Contiene las excepciones personalizadas utilizadas
durante todo el juego.

Autor: Camilo Restrepo
=========================================================
"""


class ErrorJuego(Exception):
    """
    Clase base para todas las excepciones del juego.

    Todas las excepciones personalizadas heredarán de esta
    clase para facilitar el manejo centralizado de errores.
    """

    def __init__(self, mensaje: str):
        super().__init__(mensaje)


class LongitudInvalida(ErrorJuego):
    """
    Se lanza cuando la longitud ingresada por el usuario
    es menor al mínimo permitido.
    """

    def __init__(self, longitud: int):
        mensaje = (
            f"La longitud '{longitud}' no es válida. "
            "Debe ser un número mayor o igual a 8."
        )
        super().__init__(mensaje)


class EntradaNoNumerica(ErrorJuego):
    """
    Se lanza cuando el usuario escribe un dato
    que no corresponde a un número entero.
    """

    def __init__(self):
        mensaje = "Debe ingresar únicamente valores numéricos."
        super().__init__(mensaje)


class PasswordInvalida(ErrorJuego):
    """
    Se lanza cuando una contraseña no cumple
    las reglas de validación del juego.
    """

    def __init__(self, motivo: str):
        mensaje = f"Contraseña inválida: {motivo}"
        super().__init__(mensaje)