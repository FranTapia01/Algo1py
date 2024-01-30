import gamelib
import bazas
import random

#///////////////////////////////////////////////Funciones Graficas//////////////////////////////////////////////////////
def dibujar_gandor(ganadores):
    '''
    Recibe una lista con el o los  ganadores y los imprime en pantalla. Pregunta si se quiere inicializar un nuevo juego.
    '''
    x, y = 500, 200
    gamelib.draw_text('Presione Enter para volver a jugar, de lo contrario presione cualquier tecla para salir del juego', 500, 400)
    if len(ganadores) == 1:
        gamelib.draw_text('GANADOR', x, y)
        gamelib.draw_text(f'{ganadores[0][1]} - puntaje: {ganadores[0][0]}', x, y + 50)
    else:   
        gamelib.draw_text('EMPATE', x, y)
        for i in range(len(ganadores)):
            gamelib.draw_text(f'{ganadores[i][1]} - puntaje: {ganadores[i][0]}', x, y + 50)
            y += 50
    


def dibujar_cartas(estado_juego, turno, rectangulos, cartas_jugadas):
    '''
    Recibe el estado de juego, el turno y los rectángulos y dibuja las cartas del jugador al que le toca tirar(o definir su apuesta)
    en el rectángulo inferior.
    También dibuja el revés de las cartas en las otras posiciones de los jugadores.
    ''' 
    diccionario_jugadores, _, palo_triunfo = estado_juego
    gamelib.draw_image(f'img/{palo_triunfo}.gif', 165, 25) 
    cantidad_cartas = len(diccionario_jugadores[turno][0])
    if cantidad_cartas != 0:   
        cartas_centradas = centrar_cartas(cantidad_cartas)
    
    for i in range(len(diccionario_jugadores)):  
        x, y = rectangulos[i][0], rectangulos[i][1]
        if i == 0:
            x-=28
            for carta in diccionario_jugadores[turno][0]:
                x += cartas_centradas
                if len(cartas_jugadas) == len(diccionario_jugadores):
                    gamelib.draw_image('img/blue_back.gif', x, y+2)            
                else:
                    gamelib.draw_image(f'img/{carta}.gif', x, y+2)
        elif i == 1:
            x-=28      
            for _ in range(cantidad_cartas):
                x += cartas_centradas
                gamelib.draw_image('img/blue_back.gif', x, y+2)                
        else:  
            y-=28
            for _ in range(cantidad_cartas):
                y += cartas_centradas
                gamelib.draw_image('img/blue_back_h.gif', x+2, y)  


                
def dibujar_jugadores(jugadores, turno, estado_juego):
    '''
    Dibuja los nombres de los jugadores y los va rotando segun el turno actual
    '''
    diccionario_jugadores, _, _ = estado_juego
    indice = jugadores.index(turno)    
    contador = 0
    coordenadas = [(480, 450), (220, 300), (480, 140), (780, 300)]
    if len(jugadores) == 2:
        coordenadas.pop(3)
        coordenadas.pop(1)
    elif len(jugadores) == 3:
        coordenadas.pop(3)

    puntaje, apuesta, bazas = diccionario_jugadores[jugadores[indice]][1:]
    gamelib.draw_text(f'{jugadores[indice]} P: {puntaje} A: {apuesta} B: {bazas}', coordenadas[0][0], coordenadas[0][1], fill = 'black')

    while contador != len(jugadores) -1:
        if indice >= len(jugadores) -1:
            indice = -1
        indice += 1
        contador += 1
        x, y = coordenadas[contador]
        puntaje, apuesta, bazas = diccionario_jugadores[jugadores[indice]][1:]
        gamelib.draw_text(f'{jugadores[indice]} P: {puntaje} A: {apuesta} B: {bazas}', x, y, fill = 'black')



def dibujar_tablero(cant_jugadores, rectangulos, estado_juego):
    '''
    Recibe la cantidad de jugadores y una lista con coordenadas en forma de rectangulo donde dibujar el tablero.
    Utiliza la cantidad de jugadores para definir la cantidad de rectangulos a dibujar.
    '''
    _, ronda, _ = estado_juego
    gamelib.draw_image('img/fondo_mesa.gif', 0, 0)    
    gamelib.draw_text(f'RONDA: {ronda}', 850, 20, fill='black')  
    gamelib.draw_text('palo del triunfo', 200, 15, fill='black')  
    contador = -1
    for _ in range(cant_jugadores):
        contador += 1
        coordenadas = rectangulos[contador]
        x1, y1, x2, y2 = coordenadas    
        gamelib.draw_rectangle(x1, y1, x2, y2, outline='white', fill='black', width=2)
              

        
def dibujar_jugadas(cartas_jugadas, estado_juego, ganador):
    '''
    Dibuja las cartas que juega cada jugador en la posicion correspondiente (rotan con el jugador segun el turno)
    Ademas cuando todos los jugadores hayan jugado, marca en verda la carta ganadora.
    ''' 
    diccionario_jugadores, _, _ = estado_juego
    coordenadas = [(580, 250), (468, 185), (355, 250), (468, 320)]#derecha arriba izquierda abajo
    cartas_jugadas = cartas_jugadas[::-1]

    if len(diccionario_jugadores) == 2:
        coordenadas.pop(0)
        coordenadas.pop(1)
    elif len(diccionario_jugadores) == 3:
        coordenadas.pop(0)

    if len(cartas_jugadas) == len(diccionario_jugadores):
        jugadores = []
        for carta in cartas_jugadas:
            jugadores.append(carta[0])
        indice = jugadores.index(ganador)
        x1, y1 = coordenadas[indice]
        gamelib.draw_rectangle(x1-1, y1-1, x1+65, y1+96, outline='green', fill='white', width=3)

    if cartas_jugadas != []:
        for i in range(len(cartas_jugadas)):    
            x, y = coordenadas[i]
            gamelib.draw_image(f'img/{cartas_jugadas[i][1]}.gif', x, y)



def dibujar(estado_juego, turno, rectangulos,cant_jugadores, jugadores, cartas_jugadas, ganador=None):
    '''
    Simplificacion para realizar todos los dibujos en una funcion
    '''
    gamelib.draw_begin()
    dibujar_tablero(cant_jugadores, rectangulos, estado_juego)
    dibujar_cartas(estado_juego, turno, rectangulos, cartas_jugadas)
    dibujar_jugadores(jugadores, turno, estado_juego)
    dibujar_jugadas(cartas_jugadas, estado_juego, ganador)
    gamelib.draw_end()
            

#///////////////////////////////////////////Funciones Auxiliares////////////////////////////////////////////////////////////

def centrar_cartas(ronda):
    '''
    Recibe el numero de cartas de una baraja y devuelve las coordenadas en pixeles para que quede centrada.
    '''
    limite = 460
    contador = 70
    lista = []
    dimension_carta = 70
    for _ in range(ronda):   
        lista.append(dimension_carta)
        contador += dimension_carta
    while contador > limite:
        for i in range(len(lista)):
            lista[i] -= 1
        contador -= ronda
    return(lista[0])

    
    
def crear_rectangulos(cant_jugadores):
    '''
    Crea los espacios donde iran las cartas de cada jugador segun la cantidad de jugadores y los devuelve.
    '''
    rectangulos = []
    rectangulos.append((280, 480, 720, 580))
    rectangulos.append((280, 20, 720, 120))  
    rectangulos.append((20, 80, 120, 520))
    rectangulos.append((880, 80, 980, 520))   
    return rectangulos



def cartas_a_pixeles(cant_jugadores, x_variable, ronda):
    '''
    Recibe la cantidad de cartas de los jugadores y devuelve el tamaño en pixeles de cada carta.
    '''
    rectangulos = crear_rectangulos(cant_jugadores)
    lista_de_cartas = []
    x1 = rectangulos[0][0] - 28
    y1 = rectangulos[0][1] + 2
    y2 = y1 + 65
    for i in range(ronda):
        x1 += x_variable
        x2 = x1 + x_variable
        Y = range(y1, y2)
        if i != ronda-1:
            X = range(x1, x2)
        else:
            X = range(x1, x1 + 63)             
        lista_de_cartas.append([X, Y])
    return lista_de_cartas



def inicializar_variables():
    '''
    Simplificacion en una sola funcion para iniciar todas las variables necesarias al comienzo de la partida.
    '''
    jugadores, cant_jugadores = pedir_jugadores()
    estado_juego = bazas.juego_inicial(jugadores)
    rectangulos = crear_rectangulos(cant_jugadores)
    turno = random.choice(jugadores)
    mano_ronda = turno
    lista_de_apuestas = []
    cartas_jugadas = []
    return jugadores, cant_jugadores, estado_juego, rectangulos, turno, mano_ronda, lista_de_apuestas, cartas_jugadas



def juego_actualizar(estado_juego, turno, cartas_jugadas, x, y):
    '''
    Verifica que la carta jugada corresponda con sus coordenadas en la interfaz de gamelib. 
    Si corresponde, Llama a bazas.pedir_jugada. Devuelve el estado de juego, la validez de las coordenadas clickeadas y las cartas jugadas
    '''
    diccionario_jugadores, _, _ = estado_juego
    x_variable = centrar_cartas(len(diccionario_jugadores[turno][0]))
    lista_de_cartas = cartas_a_pixeles(len(diccionario_jugadores), x_variable, len(diccionario_jugadores[turno][0]))
    cantidad = len(cartas_jugadas)

    for i in range(len(lista_de_cartas)):
        if x in lista_de_cartas[i][0] and y in lista_de_cartas[i][1]:
            carta_seleccionada =  diccionario_jugadores[turno][0][i]
            estado_juego, cartas_jugadas = bazas.pedir_jugada(turno, carta_seleccionada, estado_juego, cartas_jugadas)
            if cantidad == len(cartas_jugadas):
                eleccion_valida = False
            else:
                eleccion_valida = True
            return estado_juego, eleccion_valida, cartas_jugadas
    eleccion_valida = False
    return estado_juego, eleccion_valida, cartas_jugadas
    

    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
def pedir_jugadores():
    '''
    Pide al usuario que se ingrese una cantidad de jugadores. Si la cantidad es valida le pide sus nombres y devuelve una
    lista con los nombres de los jugadores y la cantidad.
    '''
    jugadores = []
    valores_validos = ('2', '3', '4')
    cant_jugadores = gamelib.input('Ingrese la cantidad de jugadores (2, 3 o 4)')
    while cant_jugadores not in valores_validos:
        cant_jugadores = gamelib.input('cantidad invalida, elija: (2, 3 o 4)')
    cant_jugadores = int(cant_jugadores)
    for i in range (cant_jugadores):
        nombre = gamelib.input('Ingrese su nombre')[:10]
        if nombre == '':
            jugadores.append(f'jugador {i+1}')
        else:
            jugadores.append(nombre)
    return jugadores, cant_jugadores



def cambiar_turno(turno, jugadores):
    '''
    Recibe una lista de jugadores, el nombre del que acaba de jugar, y devuelve el siguiente.
    '''
    indice = jugadores.index(turno)
    if indice >= len(jugadores) -1:
        indice = -1
    indice += 1
    turno = jugadores[indice]
    return turno



def pedir_apuesta(turno, lista_de_apuestas, contador, estado_juego):
    '''
    Recibe una lista de apuestas, el turno actual, un contador con el total de apuestas de la mano y el estado del juego.
    Pide una apuesta al jugador correspondiente y si la apuesta es valida la añade a la lista. 
    Suma el valor de la apuesta al contador y lo devuelve.
    '''
    diccionario_jugadores, ronda, _  = estado_juego
    apuesta = ''
    while not apuesta.isdigit():
        apuesta = (gamelib.input(f'{turno}, Ingrese una apuesta'))
    apuesta = int(apuesta)
    contador += apuesta

    while contador == ronda and len(lista_de_apuestas) + 1 == len(diccionario_jugadores) or apuesta > ronda:
        contador -= apuesta
        apuesta = (gamelib.input('Apuesta Invalida, Ingrese Nuevamente'))
        if apuesta == '':
            apuesta = ronda + 1
        else:
            apuesta = int(apuesta)
        contador += apuesta
    datos = (turno, apuesta)
    lista_de_apuestas.append(datos)
    return contador
    


def jugar_carta(estado_juego, turno, cartas_jugadas):
    '''
    Recibe un estado de juego, el nombre del jugador actual y las cartas jugadas por los demas en caso que haya.
    Pide al jugador que haga click en la carta que quiere jugar.
    De ser valida, devuelve la lista de cartas jugadas de los anteriores jugadores mas la del actual y el estado de juego.
    '''
    eleccion_valida= None
    while eleccion_valida == None:
        ev = gamelib.wait()
        
        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y
            estado_juego, eleccion_valida, cartas_jugadas = juego_actualizar(estado_juego, turno, cartas_jugadas, x, y)

    if eleccion_valida:
        return estado_juego, cartas_jugadas
    return jugar_carta(estado_juego, turno, cartas_jugadas)



def cambiar_ronda(estado_juego):
    '''
    Se encarga de cambiar la ronda del juego y reiniciar los valores de manos ganadas y apuestas.
    Devuelve un nuevo estado de juego con la nueva ronda y un nuevo palo del triunfo
    '''
    diccionario_jugadores, ronda, palo_triunfo = estado_juego
    ronda += 1     
    mazo = bazas.generar_cartas()
    for clave in diccionario_jugadores:
        baraja, mazo = bazas.repartir_cartas(mazo, ronda)
        diccionario_jugadores[clave][0] = baraja
        diccionario_jugadores[clave][2] = 0
        diccionario_jugadores[clave][3] = 0
    if ronda != 13:
        palo_triunfo = random.choice(mazo)
    else:
        palo_triunfo = '1C'
    return (diccionario_jugadores, ronda, palo_triunfo)

#////////////////////////////////////////////////////Main///////////////////////////////////////////////////////////

def main():
    gamelib.resize(1000, 600)
    jugadores, cant_jugadores, estado_juego, rectangulos, turno, mano_ronda, lista_de_apuestas, cartas_jugadas = inicializar_variables()
    while gamelib.is_alive():
        turno = mano_ronda
        dibujar(estado_juego, turno, rectangulos, cant_jugadores, jugadores, cartas_jugadas)
        if len(lista_de_apuestas) != cant_jugadores:
            contador = 0
            for _ in range(cant_jugadores):
                contador = pedir_apuesta(turno, lista_de_apuestas, contador, estado_juego)
                turno = cambiar_turno(turno, jugadores)
                dibujar(estado_juego, turno, rectangulos,cant_jugadores, jugadores, cartas_jugadas)
            estado_juego = bazas.pedir_apuestas(lista_de_apuestas, estado_juego)    
        while not bazas.ronda_terminada(estado_juego): 
            for _ in range (cant_jugadores):
                dibujar(estado_juego, turno, rectangulos,cant_jugadores, jugadores, cartas_jugadas)
                estado_juego, cartas_jugadas = jugar_carta(estado_juego, turno, cartas_jugadas)
                turno = cambiar_turno(turno, jugadores)
            estado_juego, ganador = bazas.determinar_ganador_mano(cartas_jugadas, estado_juego)
            dibujar(estado_juego, turno, rectangulos,cant_jugadores, jugadores, cartas_jugadas, ganador)
            gamelib.wait(gamelib.EventType.ButtonPress) 
            cartas_jugadas = []
            turno = ganador
            
        if not bazas.fin_del_juego(estado_juego):
            estado_juego = bazas.contabilizar_puntos_ronda(estado_juego)
            lista_de_apuestas = []
            mano_ronda = cambiar_turno(mano_ronda, jugadores)
            estado_juego = cambiar_ronda(estado_juego)
        else:
            gamelib.draw_begin()
            dibujar(estado_juego, turno, rectangulos,cant_jugadores, jugadores, cartas_jugadas)
            dibujar_gandor(bazas.determinar_ganador_juego(estado_juego))
            gamelib.draw_end()
            tecla = gamelib.wait(gamelib.EventType.KeyPress)
            tecla = tecla.key
            if tecla == 'Return':
                jugadores, cant_jugadores, estado_juego, rectangulos, turno, mano_ronda, lista_de_apuestas, cartas_jugadas = inicializar_variables() 
            else:
                break

gamelib.init(main)




