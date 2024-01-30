import random

POSIBLES_VECINOS = [(0,1), (0,-1), (1,0), (-1,0)]

class Flood:
    """
    Clase para administrar un tablero de N colores.
    """
    def __init__(self, alto, ancho):
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        self.alto = alto
        self.ancho = ancho
        self.grilla = [[0 for _ in range(ancho)] for _ in range(alto)]
        

    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        for i in range(self.alto):
            for j in range(self.ancho):
                self.grilla[i][j] = random.choice(range(n_colores))
        

    def obtener_color(self, fil, col):
        """
        Devuelve el color que se encuentra en las self.coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        return self.grilla[fil][col]


    def obtener_posibles_colores(self):
        """
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        """
        colores_usados = []
        for i in range(self.alto):
            for j in range(self.ancho):
                if self.grilla[i][j] not in colores_usados:
                    colores_usados.append(self.grilla[i][j])
        return colores_usados 


    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        return (self.alto, self.ancho)


    def _crear_bloque(self, vecinos, color, bloque):
        """
        Recibe una lista de vecinos, un color y una nueva lista en la que añadira a los que conformen la primera 
        mas todos los casilleros adyacentes que sean de color pasado por parametros, 
        ya sean casilleros solitarios o varios que esten conectados entre si
        """
        if vecinos == []:
            return
        
        for x, y in vecinos:
            if (x, y) not in bloque:
                bloque.append((x, y))
                vecinos = self._listar_vecinos(x, y, color)
                self._crear_bloque(vecinos, color, bloque)


    def cambiar_color(self, color_nuevo):
        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        color_viejo = self.grilla[0][0]
        vecinos = self._listar_vecinos(0, 0, color_viejo)
        bloque_flood = [(0, 0)]
        self._crear_bloque(vecinos, color_viejo, bloque_flood)
        
        for x, y in bloque_flood:
            self.grilla[x][y] = color_nuevo
       

    def clonar(self):
        """
        Devuelve:
            Flood: Copia del Flood actual
        """
        nuevo_flood = Flood(self.alto, self.ancho)
        nuevo_flood.grilla = self.copiar_grilla(self.grilla)
        return nuevo_flood


    def esta_completado(self):
        """
        Indica si todas las self.coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        """
        return all(all(x==self.grilla[i][0] for x in self.grilla[i]) for i in range(self.alto))


    def _posicion_valida(self, x, y):
        """
        verifica que la posicion ingresada como parametro corresponde a una valida dentro de la grilla
        """
        return y >= 0 and y < self.ancho and x >= 0 and x < self.alto


    def _listar_vecinos(self, x, y, color):
        """
        Recibe la posicion de un casillero y un color.
        Devuelve una lista con los vecinos que tengan el color pasado como parametro.
        """
        vecinos = []
        for i, j in POSIBLES_VECINOS:
            if self._posicion_valida(x+i, y+j) and self.grilla[x+i][y+j] == color:
                vecinos.append((x+i, y+j))
        return vecinos


    def color_mayoritario(self):
        """
        Devuelve en base al flood actual cual es el color que mas casilleros le agregaria 
        contando los casilleros solitarios mas los que formen islas.
        """
        color_viejo = self.grilla[0][0]
        vecinos = self._listar_vecinos(0, 0, color_viejo)
        bloque_flood = [(0, 0)]
        self._crear_bloque(vecinos, color_viejo, bloque_flood)   
        colores = self.obtener_posibles_colores()
        colores.remove(color_viejo)
        colores_contados = {}
        for color in colores:
            vecinos = bloque_flood
            bloque_vecino = []
            self._crear_bloque(vecinos, color, bloque_vecino)
            for casillero in bloque_flood:
                bloque_vecino.remove(casillero)
            colores_contados[len(bloque_vecino)] = color
        return colores_contados[max(colores_contados)]


    def copiar_grilla(self, grilla): #resuelve problemas de mutabilidad
        """
        Recibe una grilla y devuelve una copia. 
        """
        nueva = []
        for i in range(len(grilla)):
            nueva.append([])
            for j in range(len(grilla[0])):
                nueva[i].append(grilla[i][j])
        return nueva