from src.minas import verificar_progreso

def test_verificar_progreso():
    
    tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    minas = set([(0, 1), (1, 2)])
    cas_reveladas = set([(0, 0), (1, 0)])
    fila = 2
    columna = 1

    assert verificar_progreso(tablero, minas, cas_reveladas, fila, columna) == True