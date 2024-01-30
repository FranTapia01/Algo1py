
from time import time


def sumar_columnas(matriz):
    res = [0 for _ in range(len(matriz[0]))]

    for col in range(len(matriz[0])):
        for fil in range(len(matriz)):
            res[col] += matriz[fil][col]
    return res

def lista_super():
    lista = []
    total = 0
    while True:
        mensaje = input("ingrese mensaje: ")
        if validar(mensaje):
            break
    mensaje = mensaje.split()
    for i in range(len(mensaje)):
        if mensaje[i].isdigit():
            lista.append((mensaje[i+1], mensaje[i]))
            total += 1
    
    for producto in lista:
        print(f"{producto[0]} - {producto[1]}")
    print(total)

    

def validar(mensaje):
    for p in mensaje.split():
        if p.isdigit():
            return True
    return False


tiempo = [2, 45, 3]
segundos = 4850


def segundos_a_grados(tiempo, segundos):

    eq = [3600, 60, 1]
    for i in range(len(eq)):
        agregado  = segundos//eq[i]
        print(agregado)
        sobra = segundos%eq[i]
        print(sobra)
        tiempo[i] += agregado
        segundos = sobra
    cont = 2
    for _ in range(cont):
        if tiempo[cont] > 59:
           
            tiempo[cont-1] += 1
            tiempo[cont] -= 60
        cont -= 1
        

class Angulo:
    def __init__(self, grado, minuto, segundo):
        if grado < 0 or minuto < 0 or segundo < 0:
            raise ValueError("angulo invalido")
        self.angulo = [grado, minuto, segundo]
        self.relacion = [3600, 60, 1]

    def __str__(self):
        g, m, s = self.angulo
        return f"{g}* {m}' {s}''"


    def sumar_segundos(self, agregado):
        if agregado < 0:
            raise ValueError("no se puede restar segundos")
        angulo = self._pasar_a_angulo(agregado)
        i = 2
        for _ in range(i):
            self.angulo[i] += angulo[i]
            if self.angulo[i] > 59:
                self.angulo[i-1] += 1 
                self.angulo[i] -= 60
            i-=1
        self.angulo[0] += angulo[0]
            

    def diferencia_en_segundos(self, otro):
        res = (self._pasar_a_segundo(), otro._pasar_a_segundo())
        return max(res) - min(res)

    def _pasar_a_angulo(self, segundos):
        angulo = [0, 0, 0]
        
        for i in range(3):
            angulo[i] += segundos // self.relacion[i]
            segundos = segundos % self.relacion[i]
        return angulo


    def _pasar_a_segundo(self):
        total = 0
        for i in range(3):
            total += self.angulo[i]*self.relacion[i]
        return total


