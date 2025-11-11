import numpy as np
import random

# Crear tabla
def crear_tablero():
    return np.zeros((3, 3), dtype=int)

# Mostrar tabla
def mostrar_tablero(tablero):
    print()
    for fila in range(3):
        linea = ""
        for col in range(3):
            if tablero[fila, col] == 0:
                linea = linea + " . "
            elif tablero[fila, col] == 1:
                linea = linea + " X "
            else:
                linea = linea + " O "
        print(linea)
    print()

# Mirar si la posicion es valida
def posicion_valida(tablero, fila, col):
    if fila < 0 or fila > 2:
        return False
    if col < 0 or col > 2:
        return False
    if tablero[fila, col] != 0:
        return False
    return True

# Colocar ficha en el tablero
def colocar_ficha(tablero, fila, col, jugador):
    tablero[fila, col] = jugador

# Mirar si alguien a ganado
def hay_ganador(tablero, jugador):
    for i in range(3):
        if tablero[i, 0] == jugador and tablero[i, 1] == jugador and tablero[i, 2] == jugador:
            return True
        if tablero[0, i] == jugador and tablero[1, i] == jugador and tablero[2, i] == jugador:
            return True
    if tablero[0, 0] == jugador and tablero[1, 1] == jugador and tablero[2, 2] == jugador:
        return True
    if tablero[0, 2] == jugador and tablero[1, 1] == jugador and tablero[2, 0] == jugador:
        return True
    return False

# Ver si hay empate
def tablero_lleno(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i, j] == 0:
                return False
    return True

# Que juegue la CPU
def movimiento_cpu(tablero):
    libres = []
    for i in range(3):
        for j in range(3):
            if tablero[i, j] == 0:
                libres.append((i, j))
    if len(libres) > 0:
        eleccion = random.choice(libres)
        return eleccion
    return (-1, -1)
