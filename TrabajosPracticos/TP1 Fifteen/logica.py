import random

#/////////CONFIGURACION DEL JUEGO////////////
ALTO_TABLERO = 4
ANCHO_TABLERO = 4
CANTIDAD_PIEZAS = ALTO_TABLERO * ANCHO_TABLERO -1    
MOVIMIENTOS_INICIALES = CANTIDAD_PIEZAS * 5
CASILLA_VACIA = ' '
#/////////////////////////////////////////////

#/////CONTROLES///////
ARRIBA = 'w'
ABAJO = 's'
IZQUIERDA = 'a'
DERECHA = 'd'
SALIR = 'o'
JUEGO_NUEVO = 'n'
#/////////////////////


def crear_tablero():
    tablero = [[1+i+j*ANCHO_TABLERO for i in range(ANCHO_TABLERO)] for j in range(ALTO_TABLERO)]
    tablero[ALTO_TABLERO-1][ANCHO_TABLERO-1] = CASILLA_VACIA
    return tablero



def mover(tablero, movimientos):
    """Recibe un tablero y una lista de movimientos, devuelve el tablero con los movimiendos efectuados y 
    un int con la cantidad de movimientos validados"""
    movimientos_validados = 0
    for sentido, direccion in movimientos:
        for i in range(ALTO_TABLERO): #busco la casilla vacia
            for j in range(ANCHO_TABLERO):
                if tablero[i][j] == CASILLA_VACIA:
                    break
            if tablero[i][j] == CASILLA_VACIA:
                break
    
        if movimiento_valido([sentido, direccion], [i, j]):
            if sentido == DERECHA or sentido == IZQUIERDA:
                tablero[i][j+direccion], tablero[i][j] = tablero[i][j], tablero[i][j+direccion]  
            else:
                tablero[i+direccion][j], tablero[i][j] = tablero[i][j], tablero[i+direccion][j]
            movimientos_validados += 1
    return tablero, movimientos_validados



def mezclar_piezas(tablero):
    """Devuelve un str con movimientos randoms para mezclar el tablero"""
    lista_de_movimientos = [ARRIBA, ABAJO, IZQUIERDA, DERECHA]
    piezas_movidas = 0

    while piezas_movidas < MOVIMIENTOS_INICIALES: #me aseguro que efectivamente se realicen la cantidad de movimientos iniciales de mezcla
        movimiento = random.choice(lista_de_movimientos)
        tablero, movimiento_validado = mover(tablero, traducir_movimientos(movimiento)) 
        piezas_movidas += movimiento_validado
    return tablero    
    


def juego_terminado(tablero, cantidad_movimientos):
    """Recibe el tablero y verifica si el usuario a completado el juego, devuelve true or false respectivamente"""
    if tablero == crear_tablero() or cantidad_movimientos >= MOVIMIENTOS_INICIALES*5:
        return True
    return False


#//////////////////////////////////////////////////////Funciones Auxiliares ////////////////////////////////////////////////////////


def movimiento_valido(movimiento, puntero):
    """Recibe un movimiento y la posicion de la casilla vacia y verifica que el moviemiendo ingresado es valido, 
    devuelve true or false respectivamente"""
    x, y = puntero
    sentido, direccion = movimiento
    if sentido == DERECHA or sentido == IZQUIERDA:
        if y+direccion >= ANCHO_TABLERO or y+direccion < 0:
            return False
        return True
    else:
        if x+direccion >= ALTO_TABLERO or x+direccion < 0:
            return False
        return True



def traducir_movimientos(entrada):
    """recibe un str con las teclas presionadas y devuelve una lista con la interpretacion para la funcion 'mover'"""
    movimientos = []
    for tecla in entrada:
        if tecla == ARRIBA:
            movimientos.append([ARRIBA, 1])
        elif tecla == ABAJO:
            movimientos.append([ABAJO, -1])
        elif tecla == IZQUIERDA:
            movimientos.append([IZQUIERDA, 1])
        elif tecla == DERECHA:
            movimientos.append([DERECHA, -1])
    return movimientos

