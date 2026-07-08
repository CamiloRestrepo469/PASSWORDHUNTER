from src.eventos import Eventos


def main():

    Eventos.titulo()

    Eventos.bienvenida("Camilo")

    Eventos.separador()

    Eventos.mensaje("Has encontrado un antiguo templo.")

    Eventos.mensaje("La puerta del primer cofre está cerrada.")

    Eventos.error("La contraseña ingresada no es válida.")

    Eventos.despedida()


if __name__ == "__main__":
    main()