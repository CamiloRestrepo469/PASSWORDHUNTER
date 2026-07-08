from src.jugador import Jugador


def main():

    jugador = Jugador("Camilo")

    jugador.mostrar_estado()

    jugador.agregar_puntos(10)

    jugador.agregar_puntos(25)

    jugador.agregar_puntos(50)

    jugador.agregar_puntos(-20)

    jugador.mostrar_estado()

    print()

    print(jugador)

    jugador.reiniciar()

    jugador.mostrar_estado()


if __name__ == "__main__":
    main()