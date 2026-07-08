# PASSWORDHUNTER
# 🔐 Password Hunter - The Ancient Vaults

## Descripción

**Password Hunter - The Ancient Vaults** es un juego interactivo desarrollado en **Python** utilizando **Programación Orientada a Objetos (POO)**.

El jugador asume el papel de un **Cazador de Contraseñas**, cuya misión consiste en generar contraseñas completamente aleatorias para abrir antiguos cofres ocultos dentro de un templo.

Cada contraseña generada debe cumplir estrictamente una serie de reglas de seguridad. Cuando la contraseña es válida, el jugador obtiene un cofre aleatorio con diferentes recompensas. Si la contraseña no cumple las condiciones establecidas, se abre un **Cofre Maldito**, el cual resta puntos al jugador.

El juego permite jugar múltiples rondas, acumulando puntos hasta que el usuario decida finalizar la partida.

---

# Objetivos del proyecto

- Aplicar Programación Orientada a Objetos.
- Implementar generación aleatoria de contraseñas.
- Validar reglas de seguridad.
- Manejar excepciones personalizadas.
- Administrar puntajes.
- Simular un juego interactivo por consola.

---

# Características

✔ Generación completamente aleatoria de contraseñas.

✔ Longitud definida por el usuario.

✔ Longitud mínima de 8 caracteres.

✔ Longitud máxima según los caracteres disponibles.

✔ Al menos una letra mayúscula.

✔ Al menos una letra minúscula.

✔ Al menos un número.

✔ Al menos un carácter especial.

✔ Sin caracteres repetidos.

✔ Apertura aleatoria de cofres.

✔ Sistema de puntaje.

✔ Penalización mediante Cofre Maldito.

✔ Juego por rondas.

✔ Manejo de excepciones personalizadas.

---

# Tipos de Cofres

| Cofre | Puntaje |
|--------|---------|
| 🟤 Común | +10 |
| 🔵 Raro | +25 |
| 🟣 Legendario | +50 |
| ☠ Maldito | -20 |

---

# Estructura del proyecto

```
PASSWORDHUNTER/

│

├── main.py

├── README.md

├── .gitignore

│

└── src/

    ├── __init__.py

    ├── excepciones.py

    ├── password.py

    ├── cofres.py

    ├── puntaje.py

    ├── jugador.py

    ├── eventos.py

    └── juego.py
```

---

# Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Visual Studio Code
- Git
- GitHub

---

# Requisitos

- Python 3.10 o superior

---

# Ejecución

Clonar el repositorio:

```bash
git clone https://github.com/CamiloRestrepo469/PASSWORDHUNTER.git
```

Ingresar a la carpeta:

```bash
cd PASSWORDHUNTER
```

Ejecutar el programa:

```bash
python main.py
```

---

# Programación Orientada a Objetos

El proyecto está estructurado mediante las siguientes clases:

- **Password** → Generación y validación de contraseñas.

- **Cofre** → Representación de los cofres del juego.

- **Jugador** → Administración del jugador.

- **Puntaje** → Gestión del sistema de puntuación.

- **Eventos** → Interfaz de mensajes del juego.

- **JuegoCazador** → Control completo del flujo del juego.

- **Excepciones** → Manejo de errores personalizados.

---

# Reglas de validación de contraseña

Una contraseña será válida únicamente cuando cumpla todas las siguientes condiciones:

- Mínimo 8 caracteres.
- Contener al menos una letra mayúscula.
- Contener al menos una letra minúscula.
- Contener al menos un número.
- Contener al menos un carácter especial.
- No contener caracteres repetidos.

---

# Autor

**Camilo Restrepo**

Universidad Nacional Abierta y a Distancia - UNAD

Curso: Programación Python

2026