import ttt_core

def pedir_posicion():
    valido = False
    while not valido:
        print("Escribe la posicion de la fila que quieres seleccionar ( es entre 0 y 2): ")
        fila = input()
        print("Escribe la posicion de la columna que quieres seleccionar ( es entre 0 y 2): ")
        col = input()
        if fila in ["0", "1", "2"] and col in ["0", "1", "2"]:
            return int(fila), int(col)
        else:
            print("No existe esa posicion en el tablero , vuelvelo a intentar")

def jugar():
    print("--- Tres en raya ---")
    print("1. 2 jugadores")
    print("2. Contra CPU")
    modo = input("Escribe que modo es el que quieres jugar: ")

    tablero = ttt_core.crear_tablero()
    turno = 1
    ganador = 0
    juego_activo = True

    while juego_activo:
        ttt_core.mostrar_tablero(tablero)
        print("Le toca al jugador", turno)
        if modo == "2" and turno == 2:
            fila, col = ttt_core.movimiento_cpu(tablero)
            print("La CPU a seleccionado la casilla:", fila, col)
        else:
            fila, col = pedir_posicion()
        if ttt_core.posicion_valida(tablero, fila, col):
            ttt_core.colocar_ficha(tablero, fila, col, turno)
            if ttt_core.hay_ganador(tablero, turno):
                ttt_core.mostrar_tablero(tablero)
                print("El jugador", turno, "ha ganada , pringao")
                juego_activo = False
            elif ttt_core.tablero_lleno(tablero):
                ttt_core.mostrar_tablero(tablero)
                print("Empate , que mala suerte eh ")
                juego_activo = False
            else:
                if turno == 1:
                    turno = 2
                else:
                    turno = 1
        else:
            print("No puedes repetir las mismas coordenadas")
if __name__ == "__main__":
    jugar()
