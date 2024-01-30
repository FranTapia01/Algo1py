import logica

def mostrar(tablero, cant_movimientos):
    """dibuja en la consola el tablero y los datos del juego"""
    
    print("\n=======FIFTEEN=======")
    print(f"controles: {logica.ARRIBA} {logica.IZQUIERDA} {logica.ABAJO} {logica.DERECHA}")
    cadena = ""
    for i in range(logica.ALTO_TABLERO):
        for j in range(logica.ANCHO_TABLERO):
            cadena += f"|{str(tablero[i][j]).center(4)}"
        print(f"{cadena}|")
        cadena = ""
    print(f"movimientos realizados: {cant_movimientos}")

    if logica.juego_terminado(tablero, cant_movimientos) and cant_movimientos >= logica.MOVIMIENTOS_INICIALES*5:
        print("----- Perdiste :( -----")
        print(f"ingresa {logica.JUEGO_NUEVO} para jugar de nuevo")
    elif logica.juego_terminado(tablero, cant_movimientos):
        print("----- Felicidades, Ganaste! -----")
        print(f"ingresa {logica.JUEGO_NUEVO} para jugar de nuevo")
    print(f"ingresa {logica.SALIR} para salir")



def main():
    tablero = logica.mezclar_piezas(logica.crear_tablero())
    contador_movimientos = 0
    entrada = ''

    while entrada != logica.SALIR:
        if not logica.juego_terminado(tablero, contador_movimientos):
            mostrar(tablero, contador_movimientos)
            entrada = input("Entrada: ")
            tablero, movimientos_validados = logica.mover(tablero, logica.traducir_movimientos(entrada))
            contador_movimientos += movimientos_validados
        else:
            mostrar(tablero, contador_movimientos)
            entrada = input("Entrada: ")
            if entrada == logica.JUEGO_NUEVO:
                tablero = logica.mezclar_piezas(logica.crear_tablero())
                contador_movimientos = 0

main()

