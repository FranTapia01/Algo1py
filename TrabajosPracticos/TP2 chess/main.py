import gamelib
import logica

ANCHO_VENTANA = 400
ALTO_VENTANA = 470
DIM_TABLERO = 400
CASILLA = 50


def juego_mostrar(juego):
    '''dibuja la interfaz de la aplicación en la ventana'''

    gamelib.draw_text('Shape Shifter Chess', 100, 420, fill = 'white')
    gamelib.draw_text(f'nivel: {juego.nivel}', 300, 420, fill = 'white')
    gamelib.draw_text(f'Salir: Esc', 300, 450, fill = 'white')
    gamelib.draw_text(f'Reintentar: r', 100, 450, fill = 'white')
    

    for j in range(0, DIM_TABLERO, CASILLA): # tablero
        for i in range(0, DIM_TABLERO, CASILLA):
            if ((i+j)//10)%2 == 0: color = '#534a3a'
            else: color = '#d6d6d6'    
            gamelib.draw_rectangle(i, j, i+CASILLA, j+CASILLA, fill=color)

    for i in range(logica.DIMENSION):
        for j in range(logica.DIMENSION):     
            if juego.tablero[i][j] == logica.VACIO:
                continue
            if (i, j) == juego.pieza_activa:
                gamelib.draw_image(f'img/{juego.tablero[i][j]}_rojo.gif', (j*CASILLA)+4, (i*CASILLA)+4)
            else:
                gamelib.draw_image(f'img/{juego.tablero[i][j]}_blanco.gif', (j*CASILLA)+4, (i*CASILLA)+4)

            for posible in juego._movimientos_posibles(juego.pieza_activa):
                x, y = posible[0], posible[1]
                if juego.tablero[x][y] != logica.VACIO:
                    gamelib.draw_rectangle((y*CASILLA)+2, (x*CASILLA)+2, (y*CASILLA)+CASILLA-2, (x*CASILLA)+CASILLA,outline='red', fill='', width=3)


def pixeles_a_coordenadas(x, y):
    '''Recibe coordenadas en pixeles donde se hizo click y devuelve los indices de la casilla a la que corresponde en el tablero'''
    casillas = []
    for n in range(0, DIM_TABLERO, CASILLA):
        casillas.append(range(n, n+CASILLA))

    for i in range(len(casillas)):
        if x in casillas[i]:
            indice_x = i
        if y in casillas[i]:
            indice_y = i
    return indice_y, indice_x


def main():
    gamelib.title("Shape Shifter Chess")
    gamelib.resize(ANCHO_VENTANA-3, ALTO_VENTANA)
    juego = logica.Shape_Shifter_Chess()
    respuesta = gamelib.input("Desea cargar el ultimo nivel jugado? s/n")
    if respuesta == 's':
        try: juego.cargar_archivos('autoguardado.txt')     
        except:
            gamelib.say('No se encontro una partida guardada')
            juego.iniciar_nivel()    
    else:
        juego.iniciar_nivel()
    
    while gamelib.is_alive():   

        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:  
            if ev.y < DIM_TABLERO:
                i, j = pixeles_a_coordenadas(ev.x, ev.y)
                juego.comer(i, j)
            
        elif ev.type == gamelib.EventType.KeyPress:
            if ev.key == 'Escape':
                break
            if ev.key == 'r':
                juego.cargar_archivos('autoguardado.txt')            

        if juego.termino_nivel():
            juego.tablero[juego.pieza_activa[0]][juego.pieza_activa[1]] = logica.VACIO
            juego.piezas_comidas = 0
            juego.nivel += 1
            juego.iniciar_nivel()
            
gamelib.init(main)