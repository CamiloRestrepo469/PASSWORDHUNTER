"""
=========================================================
Archivo: main.py

Proyecto:
Password Hunter - The Ancient Vaults

Este archivo se utiliza temporalmente para realizar
pruebas de los módulos desarrollados.

Posteriormente será reemplazado por el menú principal
del juego.

Autor:
Camilo Restrepo
=========================================================
"""

# =====================================================
# IMPORTACIONES
# =====================================================

from src.password import Password
from src.excepciones import ErrorJuego


def main():
    """
    Función principal de pruebas.

    Permite comprobar que la clase Password genera
    correctamente contraseñas válidas y que el sistema
    de excepciones funciona adecuadamente.
    """

    print("=" * 60)
    print("      PASSWORD HUNTER - LABORATORIO DE PRUEBAS")
    print("=" * 60)

    motor = Password()

    try:

        longitud = int(
            input("\nIngrese la longitud de la contraseña: ")
        )

        password = motor.generar(longitud)

        print("\nContraseña generada:")
        print(password)

        motor.validar(password)

        print("\nLa contraseña es COMPLETAMENTE válida.")

    except ErrorJuego as error:

        print("\nSe produjo un error:")

        print(error)


if __name__ == "__main__":
    main()