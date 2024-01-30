from flood import Flood
from pila import Pila
from cola import Cola


class JuegoFlood:
    """
    Clase para administrar un Flood, junto con sus estados y acciones
    """

    def __init__(self, alto, ancho, n_colores):
        """
        Genera un nuevo JuegoFlood, el cual tiene un Flood y otros
        atributos para realizar las distintas acciones del juego.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla del Flood.
            n_colores: Cantidad maxima de colores a incluir en la grilla.
        """
        self.flood = Flood(alto, ancho)
        self.flood.mezclar_tablero(n_colores)
        self.mejor_n_movimientos, _ = self._calcular_movimientos()
        self.n_movimientos = 0
        self.pasos_solucion = Cola()
        self.hecho = Pila()
        self.deshecho = Pila()
        self.hecho.apilar(self.flood.clonar())
        
    
    def cambiar_color(self, color):

        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """
        if color != self.flood.grilla[0][0]:
            self.n_movimientos += 1
            self.flood.cambiar_color(color)
            self.hecho.apilar(self.flood.clonar())
            self.deshecho = Pila()
            
        if not self.pasos_solucion.esta_vacia() and self.pasos_solucion.ver_frente() == color:
            self.pasos_solucion.desencolar()
        else:
            self.pasos_solucion = Cola()


    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """
        if self.n_movimientos > 0:
            self.deshecho.apilar(self.hecho.desapilar())
            grilla = self.hecho.ver_tope().grilla
            self.flood.grilla = self.flood.copiar_grilla(grilla)         
            self.n_movimientos -= 1
            self.pasos_solucion = Cola()


    def rehacer(self):
        """
        Rehace el movimiento que fue deshecho si existe, manejando las
        estructuras para deshacer y rehacer.
        """
        if not self.deshecho.esta_vacia():
            grilla = self.deshecho.ver_tope().grilla
            self.hecho.apilar(self.deshecho.desapilar())
            self.flood.grilla = self.flood.copiar_grilla(grilla)   
            self.n_movimientos += 1
            self.pasos_solucion = Cola()


    def _calcular_movimientos(self):
        """
        Realiza una solución de pasos contra el Flood actual (en una Cola)
        y devuelve la cantidad de movimientos que llevó a esa solución.

        La heuristica aplicada en cada instancia de la grilla/tablero, es que: 
        el color que se elije como el mas efectivo es el que mas casilleros agregaria al flood actual 
        contando tanto casilleros individuales como las islas adyacentes al flood.

        Devuelve:
            int: Cantidad de movimientos que llevó a la solución encontrada.
            Cola: Pasos utilizados para llegar a dicha solución
        """
        flood_solucion = self.flood.clonar()
        pasos = Cola()
        pasos_cantidad = 0
        while not flood_solucion.esta_completado():
            color = flood_solucion.color_mayoritario()
            flood_solucion.cambiar_color(color)
            pasos_cantidad += 1
            pasos.encolar(color)
        return pasos_cantidad, pasos
   
      
    def hay_proximo_paso(self):
        """
        Devuelve un booleano indicando si hay una solución calculada
        """
        return not self.pasos_solucion.esta_vacia()


    def proximo_paso(self):
        """
        Si hay una solución calculada, devuelve el próximo paso.
        Caso contrario devuelve ValueError

        Devuelve:
            Color del próximo paso de la solución
        """
        return self.pasos_solucion.ver_frente()


    def calcular_nueva_solucion(self):
        """
        Calcula una secuencia de pasos que solucionan el estado actual
        del flood, de tal forma que se pueda llamar al método `proximo_paso()`
        """
        _, self.pasos_solucion = self._calcular_movimientos()


    def dimensiones(self):
        return self.flood.dimensiones()


    def obtener_color(self, fil, col):
        return self.flood.obtener_color(fil, col)


    def obtener_posibles_colores(self):
        return self.flood.obtener_posibles_colores()


    def esta_completado(self):
        return self.flood.esta_completado()
