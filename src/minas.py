"""

En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, 
lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código 
y evitar el uso de "números mágicos" o cadenas de texto repetidas.

- Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, 
enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random

FILAS = 8
COLUMNAS = 8
NUM_MINAS  = 10

MENU = """
Selecciona una Accion

1 - Revelar Casilla
2 - Marcar Bomba
3 - Rendirte
"""

# Funcion para crear el tablero vacio
def crear_tablero():
    tablero = []

    for _ in range(FILAS):
        nueva_fila = []
        for _ in range(COLUMNAS):
            nueva_fila.append(' ')
        tablero.append(nueva_fila)

    return tablero

# Funcion para iniciar el tablero con las minas aleatorias
def rellenar_tablero(tablero):
    minas = set()

    # Colocar minas aleatoriamente
    while len(minas) < NUM_MINAS:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        minas.add((fila, columna))
        tablero[fila][columna] = 'X'

    # Calcular números para celdas adyacentes a las minas
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] != 'X':
                count_minas = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (fila + i, columna + j) in minas:
                            count_minas += 1
                if count_minas > 0:
                    tablero[fila][columna] = str(count_minas)

    return tablero, minas

# Funcion que muestra el tablero con celdas ocultas y reveladas
def mostrar_tablero(tablero, cas_reveladas):
    filas = len(tablero)
    columnas = len(tablero[0])

    print(" ", end=" ")
    for col in range(1, columnas + 1):
        print(col, end=" ")
    print()

    for i in range(filas):
        print(i + 1, end=" ")
        for j in range(columnas):
            if (i, j) in cas_reveladas:
                print(tablero[i][j], end=" ")
            else:
                print('.', end=" ")
        print()

# Funcion para revelar celdas vacias y de alrededor
def revelar_celdas_vacias(tablero, fila, columna, cas_reveladas):
    if (fila, columna) in cas_reveladas:
        return
    filas = len(tablero)
    columnas = len(tablero[0])
    if fila < 0 or columna < 0 or fila >= filas or columna >= columnas:
        return
    if tablero[fila][columna] != ' ':
        cas_reveladas.add((fila, columna))
        return
    tablero[fila][columna] = '-'
    cas_reveladas.add((fila, columna))
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                revelar_celdas_vacias(tablero, fila + i, columna + j, cas_reveladas)

def verificar_progreso(tablero, minas, cas_reveladas, fila, columna):
    if (fila - 1, columna - 1) in minas:
        print("Perdiste, pisaste una BOMBA !")
        cas_reveladas.update(minas)
        return False
    else:
        revelar_celdas_vacias(tablero, fila - 1, columna - 1, cas_reveladas)
        if len(cas_reveladas) == FILAS * COLUMNAS - NUM_MINAS:
            print("Felicidades descrubriste todo el camino !")
            return False
    return True
    
def introducir_coordenadas(texto):
    verificar_respuesta = False
    while not verificar_respuesta:
        try:
            fila, columna = map(int, input(texto).split(','))
            verificar_respuesta = True
        except IndexError:
            verificar_respuesta = False
    return fila, columna

def jugar_buscaminas():

    tablero_vacio = crear_tablero()
    tablero, minas = rellenar_tablero(tablero_vacio)
    cas_reveladas = set()
    progreso = True 
    
    while progreso:

        mostrar_tablero(tablero, cas_reveladas)

        print(MENU)

        eleccion = input("> ")

        if eleccion == '1':
            fila, columna = introducir_coordenadas("Introduce las coordenadas para revelar (X,Y)\n> ")
            progreso = verificar_progreso(tablero, minas, cas_reveladas, fila, columna)

        elif eleccion == '2':
            fila, columna = introducir_coordenadas("Introduce las coordenadas de la Bomba (X,Y)\n> ")
            tablero[fila - 1][columna - 1] = 'M'

        elif eleccion == '3':
            print("Abandonaste !")
            progreso = False

        else:
            print("Commando no Valido, prueba otra VEZ !")
    else:
        mostrar_tablero(tablero, cas_reveladas)

if __name__ == "__main__":
    jugar_buscaminas()
