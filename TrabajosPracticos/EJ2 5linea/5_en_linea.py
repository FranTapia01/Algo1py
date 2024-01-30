import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 350
DIMENSION = 10


def juego_crear():
    """Inicializar el estado del juego"""
    tablero = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
    turno = 1
    return tablero, turno   



def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego
    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    tablero, turno = juego
    if x < ANCHO_VENTANA and y < ALTO_VENTANA-50:
        i, j = pixeles_a_coordenadas(x, y)      
        if tablero[i][j] == 0:
            tablero[i][j] = turno   
            turno = (turno + 1) // turno
    return tablero, turno



def pixeles_a_coordenadas(x, y):
    '''Recibe coordenadas en pixeles donde se hizo click y devuelve los indices de la casilla a la que corresponde en el tablero'''
    casillas = []
    for n in range(0, 300, 30):
        casillas.append(range(n, n+30))

    for i in range(len(casillas)):
        if x in casillas[i]:
            indice_x = i
        if y in casillas[i]:
            indice_y = i
    return indice_y, indice_x



def juego_mostrar(juego):
    """Actualizar la ventana"""
    tablero, turno = juego

    gamelib.draw_text('Turno : ', 230, 320)
    gamelib.draw_text('5 en línea', 50, 320) 
    if turno == 1:
        gamelib.draw_oval(260, 310, 280, 330, outline='green', fill='black', width=2)
    else:
        gamelib.draw_line(260, 310, 280, 330, fill='red', width=2)
        gamelib.draw_line(260, 330, 280, 310, fill='red', width=2)

    for i in range(0, ALTO_VENTANA-20, 30):
        gamelib.draw_line(0, i, ALTO_VENTANA-20, i, fill='grey', width=2)
    for j in range(0, ANCHO_VENTANA, 30):
        gamelib.draw_line(j, 0, j, ANCHO_VENTANA, fill='grey', width=2)

    for x in range(len(tablero[0])):
        for y in range(len(tablero)):
            if tablero[x][y] == 1:
                gamelib.draw_oval((y*30)+5, (x*30)+5, (y*30)+25, (x*30)+25, outline='green', fill='black', width=2)

            if tablero[x][y] == 2:
                gamelib.draw_line((y*30)+5, (x*30)+5, (y*30)+25, (x*30)+25, fill='red', width=2)
                gamelib.draw_line((y*30)+25, (x*30)+5, (y*30)+5, (x*30)+25, fill='red', width=2)


def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)