import random

def juego_inicial(jugadores):
    '''
    crea un estado inicial del juego de acuerdo a la cantidad de jugadores ingresados (2 o 4), y lo devuelve
    en forma de tupla con un diccionario con cada jugador y sus cartas, la ronda, y el palo del triunfo.
    '''
    ronda = 1
    diccionario_jugadores = {}
    mazo = generar_cartas()
    for jugador in jugadores:
        baraja, mazo = repartir_cartas(mazo, ronda)
        diccionario_jugadores[jugador] = [baraja, 0, 0, 0] #cartas, puntaje, apuesta, mano ganada
    palo_triunfo = random.choice(mazo)
    return diccionario_jugadores, ronda, palo_triunfo



def generar_cartas():
    '''
    devuelve un mazo con cartas tipo naipes franceses
    '''
    mazo = []
    palos = ['T', 'P', 'D', 'C']
    for x in palos:
        for valor in range(1, 14):
            carta = (f'{valor}{x}')
            mazo.append((carta))
    return mazo



def repartir_cartas(mazo, ronda):
    '''
    De acuerdo al numero de rondas que va reparte la misma cantidad de cartas del mazo de forma aleatoria.
    '''
    baraja = random.sample(mazo, k = ronda)
    for carta in baraja:
        mazo.remove(carta)
    return (baraja, mazo)



def pedir_apuestas(lista_de_apuestas, estado_juego):
    '''
    Pide a cada jugador su apuesta y la agrega al diccionario de jugadores.
    Devuelve un nuevo estado del juego
    '''
    diccionario_jugadores, ronda, palo_triunfo = estado_juego
    for jugador, apuesta in lista_de_apuestas:
        diccionario_jugadores[jugador][2] = apuesta
    estado_juego = diccionario_jugadores, ronda, palo_triunfo
    return estado_juego



def pedir_jugada(jugador, carta, estado_juego, cartas_jugadas=[]):
    '''
    Recibe la carta que el jugador quiere jugar, 
    verifica si es valida de acuerdo a las reglas, la agrega a la lista con las otras cartas jugadas 
    de la mano y la elimina de la baraja del jugador.
    Devuelve un nuevo estado del juego y una lista con las jugadas de esa mano.
    '''
    diccionario_jugadores, ronda, palo_triunfo = estado_juego
    validas = cartas_validas(diccionario_jugadores[jugador][0], cartas_jugadas, palo_triunfo)
    if carta in validas:
        cartas_jugadas.append((jugador, carta))
        diccionario_jugadores[jugador][0].remove(carta)
        estado_juego = diccionario_jugadores, ronda, palo_triunfo
    return estado_juego, cartas_jugadas



def cartas_validas(baraja, cartas_jugadas, palo_triunfo):
    '''
    Crea y devuelve una lista de cartas permitidas para jugar segun el palo del triunfo y las cartas ya jugadas anteriormente
    '''
    cartas_permitidas = []
    if cartas_jugadas == []:
        for carta in baraja:
            cartas_permitidas.append(carta)
        return cartas_permitidas
    inicial = cartas_jugadas[0][1]
    letra_triunfo = palo_triunfo[-1]
    letra_inicial = inicial[-1]
    mayor_i = int(inicial[:-1])
    mayor_t = 0
    menores = []
    mayores = []
    for tupla in cartas_jugadas:
        _, carta = tupla
        if carta[-1] == inicial[-1] and int(carta[:-1]) > mayor_i:
            mayor_i = int(carta[:-1]) 
        elif carta[-1] == palo_triunfo[-1] and int(carta[:-1]) > mayor_t:
            mayor_t = int(carta[:-1])

    conjuntos_palos = {'t': [], 'i': [], 'o': []}
    for carta in baraja:
        if carta[-1] == letra_triunfo:
            conjuntos_palos['t'].append(carta)
        elif carta[-1] == letra_inicial:
            conjuntos_palos['i'].append(carta)
        else:
            conjuntos_palos['o'].append(carta)

    if conjuntos_palos['t'] == [] and conjuntos_palos['i'] == []:
        cartas_permitidas = conjuntos_palos['o']
    elif conjuntos_palos['i'] == []:
        for carta in conjuntos_palos['t']:
            if int(carta[:-1]) > mayor_t or int(carta[:-1]) == 1:
                mayores.append(carta)
            else:
                menores.append(carta)
        if mayores == []:
            cartas_permitidas = menores
        else:
            cartas_permitidas = mayores
    else:
        for carta in conjuntos_palos['i']:
            if int(carta[:-1]) > mayor_i or int(carta[:-1]) == 1:
                mayores.append(carta)
            else:
                menores.append(carta)
        if mayores == []:
            cartas_permitidas = menores
        else:
            cartas_permitidas = mayores
    return cartas_permitidas



def determinar_ganador_mano(cartas_jugadas, estado_juego):
    '''
    Recibe todas las cartas jugadas en una mano, el palo del triunfo y determina quien es el ganador.
    '''
    diccionario_jugadores, ronda, palo_triunfo = estado_juego
    ranking_palo_triunfo = []
    ranking_normal = []
    for jugada in cartas_jugadas:     
        if jugada[1][-1] == palo_triunfo[-1]:
            ranking_palo_triunfo.append((int(jugada[1][:-1]), jugada[0]))  
        elif jugada[1][-1] == cartas_jugadas[0][1][-1]:
            ranking_normal.append((int(jugada[1][:-1]), jugada[0]))
 
    ranking_normal = sorted(ranking_normal)[::-1]
    ranking_palo_triunfo = sorted(ranking_palo_triunfo)[::-1]
    
    if ranking_palo_triunfo != []:
        for jugador in ranking_palo_triunfo:       
            if jugador[0] == 1:
                diccionario_jugadores[jugador[1]][3] += 1               
                return (diccionario_jugadores, ronda, palo_triunfo), jugador[1]  
        diccionario_jugadores[ranking_palo_triunfo[0][1]][3] += 1
        return (diccionario_jugadores, ronda, palo_triunfo), ranking_palo_triunfo[0][1]       
    else:
        for jugador in ranking_normal:       
            if jugador[0] == 1:
                diccionario_jugadores[jugador[1]][3] += 1               
                return (diccionario_jugadores, ronda, palo_triunfo), jugador[1]    
        diccionario_jugadores[ranking_normal[0][1]][3] += 1
        return (diccionario_jugadores, ronda, palo_triunfo), ranking_normal[0][1]  



def contabilizar_puntos_ronda(estado_juego):
    '''
    Recibe un estado de juego y suma los puntos que haya conseguido.
    10 puntos si bazas ganadas = apuesta
    5 por baza ganada
    si gana y apuesta = 0 5 * numero de ronda
    suma los puntos y devuelve el estado con los nuevos puntos 
    '''
    diccionario_jugadores, ronda, palo_triunfo = estado_juego
    for jugador in diccionario_jugadores:
        puntaje = 0
        _, _, bazas_ganadas, apuesta = diccionario_jugadores[jugador]
        if bazas_ganadas == apuesta:
            puntaje += 10
            if bazas_ganadas == 0:
                puntaje += 5 * ronda
            else:
                puntaje += 5 * bazas_ganadas
        diccionario_jugadores[jugador][1] += puntaje
        estado_juego = diccionario_jugadores, ronda, palo_triunfo
    return estado_juego



def determinar_ganador_juego(estado_juego):
    '''
    Recibe el estado del juego con los puntajes finales de todos los jugadores y devuelve el gandor 
    del juego o si hubo un empate devuelve una lista con los mismos.
    '''
    diccionario_jugadores, _, _ = estado_juego
    tabla_puntaje = []
    tabla_empate = []
    for jugador in diccionario_jugadores:
        _, puntaje_total, _, _ = diccionario_jugadores[jugador]
        tabla_puntaje.append((int(puntaje_total), jugador))

    tabla_puntaje = sorted(tabla_puntaje)[::-1]
    tabla_empate.append(tabla_puntaje[0])

    for puntaje in tabla_puntaje:
        if puntaje[1] != tabla_empate[0][1]:
            if puntaje[0] == tabla_empate[0][0]:
                tabla_empate.append(puntaje)
    if len(tabla_empate) == 1:
        return [tabla_puntaje[0]]
    else:
        return tabla_empate



def ronda_terminada(estado_juego):
    '''
    Recive el estado de juego y devuelve True o False si la ronda termino o no.
    '''
    diccionario_jugadores, _, _  = estado_juego
    for jugador in diccionario_jugadores:
        if diccionario_jugadores[jugador][0] != []:
            break
        return True
    return False



def fin_del_juego(estado_juego):
    '''
    Recive el estado de juego y devuelve True o False si el juego termino o no.
    '''
    _, ronda, _ = estado_juego
    if ronda == 13 and ronda_terminada(estado_juego):
        return True
    return False


