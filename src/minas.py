
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

def crear_tablero():
    """

    Crea un tablero de juego vacío para el juego Buscaminas.

    Devuelve:
        lista: Una lista bidimensional que representa un tablero de juego vacío para Buscaminas. 
        Cada elemento en la lista representa una celda en el tablero y está inicialmente configurado como un carácter de espacio.

    """

    tablero = []

    for _ in range(FILAS):
        nueva_fila = []
        for _ in range(COLUMNAS):
            nueva_fila.append(' ')
        tablero.append(nueva_fila)

    return tablero

def rellenar_tablero(tablero):
    """

    Rellena el tablero de juego con minas y calcula los números para las celdas adyacentes a las minas.

    Argumentos:
        tablero (lista): El tablero de juego representado como una lista 2D.

    Devuelve:
        tablero (lista): El tablero de juego actualizado con números asignados a las celdas adyacentes a las minas.
        minas (conjunto): Un conjunto de coordenadas que representan las posiciones de las minas.

    """

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

def mostrar_tablero(tablero, conj_reveladas, conj_marcadas):
    """

    Mostrar el tablero de juego con las celdas reveladas y marcadas.

    Argumentos:
        tablero (listas): El tablero de juego representado como una lista 2D.
        conj_reveladas (conjunto): Un conjunto de tuplas que representan las coordenadas de las celdas reveladas.
        conj_marcadas (conjunto): Un conjunto de tuplas que representan las coordenadas de las celdas marcadas.

    Devuelve:
        Nada: La función solo muestra el tablero de juego, no devuelve ningún valor.

    """

    filas = len(tablero)
    columnas = len(tablero[0])

    print(" ", end=" ")
    for col in range(1, columnas + 1):
        print(col, end=" ")
    print()

    for i in range(filas):
        print(i + 1, end=" ")
        for j in range(columnas):
            if (i, j) in conj_reveladas:
                print(tablero[i][j], end=" ")
            elif (i, j) in conj_marcadas:
                print('M', end=" ")  # Mostrar celdas marcadas con 'M'
            else:
                print('.', end=" ")
        print()

def revelar_celdas_vacias(tablero, fila, columna, cas_reveladas):
    """

    Revela las celdas vacías en un tablero de juego verificando de forma recursiva las celdas vecinas.

    Argumentos:
        tablero (listas): El tablero de juego representado como una lista 2D.
        fila (entero): El índice de fila de la celda que se va a revelar.
        columna (entero): El índice de columna de la celda que se va a revelar.
        cas_reveladas (conjunto): Un conjunto de celdas que ya han sido reveladas.

    Devuelve:
        Ninguno: La función actualiza el tablero de juego y el conjunto de celdas reveladas en su lugar.

    """

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
    """

    Revisa el progreso del juego en el programa Buscaminas.

    Argumentos:
        tablero (listas): Una lista 2D que representa el tablero de juego.
        minas (conjunto): Un conjunto de tuplas que representan las coordenadas de las minas.
        cas_reveladas (conjunto): Un conjunto de tuplas que representan las coordenadas de las celdas reveladas.
        fila (entero): La coordenada de fila de la celda actual.
        columna (entero): La coordenada de columna de la celda actual.

    Devuelve:
        True si el juego aún está en progreso.
        False si el juego ha terminado.

    """

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
    """

    Solicita al usuario ingresar las coordenadas de una celda en el tablero de juego.

    Argumentos:
        prompt (cadena): El mensaje a mostrar al usuario como solicitud de entrada.

    Devuelve:
        fila (entero): El índice de fila actualizado de la celda.
        columna (entero): El índice de columna actualizado de la celda.

    """

    verificar_respuesta = False
    while not verificar_respuesta:
        try:
            fila, columna = map(int, input(texto).split(','))
            if 1 <= fila <= FILAS and 1 <= columna <= COLUMNAS:
                verificar_respuesta = True
        except ValueError:
            verificar_respuesta = False
    return fila, columna

def jugar_buscaminas():

    tablero_vacio = crear_tablero()
    tablero, minas = rellenar_tablero(tablero_vacio)
    cas_reveladas = set()
    conj_marcadas = set()
    progreso = True 
    
    while progreso:

        mostrar_tablero(tablero, cas_reveladas, conj_marcadas)

        print(MENU)

        eleccion = input("> ")

        if eleccion == '1':
            fila, columna = introducir_coordenadas("Introduce las coordenadas para revelar (X,Y)\n> ")
            progreso = verificar_progreso(tablero, minas, cas_reveladas, fila, columna)

        elif eleccion == '2':
            fila, columna = introducir_coordenadas("Introduce las coordenadas de la Bomba (X,Y)\n> ")
            conj_marcadas.add((fila - 1, columna - 1))

        elif eleccion == '3':
            print("Abandonaste !")
            progreso = False

        else:
            print("Commando no Valido, prueba otra VEZ !")

    else:
        mostrar_tablero(tablero, cas_reveladas, conj_marcadas)

if __name__ == "__main__":
    jugar_buscaminas()
