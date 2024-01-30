import csv
import random

DIMENSION = 8
VACIO = ''

class Shape_Shifter_Chess():
    def __init__(self):
        self.movimientos = self.cargar_archivos('movimientos.csv')
        self.tablero = [[VACIO for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.nivel = 1
        self.pieza_activa = None
        self.piezas_comidas = 0
        
        

    def iniciar_nivel(self):
        """inicializa el juego con el nivel en atributos"""
        pieza = random.choice(list(self.movimientos.keys()))
        i, j = random.choice(range(DIMENSION)), random.choice(range(DIMENSION))
        self.tablero[i][j] = pieza
        self.pieza_activa = (i, j)
        
        for _ in range(self.nivel+1): 
            lista_coordenadas = self._movimientos_posibles((i, j))
            pieza = random.choice(list(self.movimientos.keys()))  
            while True: 
                posible_coordenada = random.choice(lista_coordenadas)
                x, y = posible_coordenada
                if self.tablero[x][y] == VACIO:  
                    self.tablero[x][y] = pieza
                    i, j = posible_coordenada
                    break
                lista_coordenadas.remove(posible_coordenada)
                if lista_coordenadas == []:
                    raise IndexError("no se pudieron agregar mas piezas :(")
        self._guardar()



    def comer(self, i, j): 
        """come la pieza que este en la posicion recibida""" 
        if (i, j) in self._movimientos_posibles(self.pieza_activa) and self.tablero[i][j] != VACIO:
            self.tablero[self.pieza_activa[0]][self.pieza_activa[1]] = VACIO
            self.pieza_activa = (i, j)
            self.piezas_comidas += 1



    def _movimientos_posibles(self, posicion):   
        """recibe la posicion de una pieza, por ende tambien su nombre y devuelve una lista 
        con todos los movimientos que puede realizar dicha pieza"""
        i, j = posicion
        pieza = self.tablero[i][j]
        lista_movimientos = []
        for x, y in self.movimientos[pieza][0]:
            if self.movimientos[pieza][1]:
                for n in range(1, DIMENSION):         
                    if self._posicion_valida(x*n+i, y*n+j):                  
                        lista_movimientos.append((x*n+i, y*n+j))
            else:
                if self._posicion_valida(x+i, y+j):
                    lista_movimientos.append((x+i, y+j))
        return lista_movimientos
        


    def _posicion_valida(self, x, y):
        """verifica que la posicion pasada corresponde a una valida del tablero"""
        return x in range(DIMENSION) and y in range(DIMENSION)



    def _guardar(self):
        """guarda los atributos actuales del juego"""
        with open("autoguardado.txt", 'w') as f:
            tablero = []
            for fila in self.tablero:
                tablero.append(','.join(fila))

            f.write(f"{'-'.join(tablero)};{self.nivel};{self.pieza_activa[0]}{self.pieza_activa[1]};{self.piezas_comidas}")



    def cargar_archivos(self, ruta):
        """recibe una ruta, procesa y carga el contenido del archivo"""
        if ruta == 'movimientos.csv':
            movimientos = {}
            with open(ruta) as file:
                for pieza, cord, extensible in csv.reader(file):
                    if extensible == "false": extensible = ""
                    cord = cord.split(';')
                    if pieza not in movimientos:
                        movimientos[pieza] = [[], bool(extensible)]    
                    movimientos[pieza][0].append((int(cord[0]), int(cord[1])))
            return movimientos
       
        if ruta == 'autoguardado.txt':
            res = []
            with open(ruta) as file:
                for linea in file:
                    tablero, nivel, pieza_activa, piezas_comidas = linea.split(';')
                    tablero = tablero.split('-')
                    for i in range(DIMENSION):
                        fila = tablero[i].split(',')
                        res.append(fila)
                    self.tablero = res
                    self.nivel = int(nivel)
                    self.pieza_activa = (int(pieza_activa[0]), int(pieza_activa[1]))
                    self.piezas_comidas = int(piezas_comidas)
         

    def termino_nivel(self):
        """verifica que no quedan mas piezas por comer"""
        return self.piezas_comidas == self.nivel+1
