import csv
'''
1. Escribir un programa que abra un archivo separado por comas y le pida al usuario dos
numeros. El programa debe escribir en otro archivo el contenido del primero con las columnas
del archivo CSV intercambiadas segun los numeros del usuario. Por ejemplo, si una linea del
archivo es lunes,martes,miercoles,jueves" y los numeros del usuario son 1 y 3, el archivo de
salida sera miercoles,martes,lunes,jueves" (las columnas 1 y 3 estan intercambiadas)
'''
def intercambiar_columnas(origen, destino, c1, c2):
    
    with open(origen) as f_origen, open(destino, 'w') as f_destino:
        destino = csv.writer(f_destino)
        for fila in csv.reader(f_origen):
            if max(c1,c2) > len(fila):
                
                raise IndexError("columnas ingresadas fuera de rango")
            fila[c1], fila[c2] = fila[c2], fila[c1]
            destino.writerow(fila)
        
def pedir_numero():
    while True:
        entrada = input("ingrese numero: ")
        if entrada.isdigit() and int(entrada) != 0:
            return int(entrada)-1
        print("ingrese un numero valido para columnas")

def main():
    n1, n2 = pedir_numero(), pedir_numero()
    intercambiar_columnas("origen.txt", "destino.txt", n1, n2)
main()

'''
2. Escribir una funcion que reciba un nombre de un archivo con datos y un nombre de
un archivo para guardar errores (los errores se agregan al final). El archivo con datos tiene el
siguiente formato:

año , mes , vendedor , cliente , monto

La funcion debe devolver un diccionario con los vendedores y los montos totales por vendedor
como valor. Cuando una linea no sea valida, la ejecucion no se puede detener, pero debe guardar
la linea en el archivo de errores.
'''

def diccionario_vendedores(ruta_datos, ruta_errores):
    res = {}
    with open(ruta_datos) as datos, open(ruta_errores, 'a') as errores:
        errores = csv.writer(errores)
        for linea in csv.reader(datos):
            if len(linea) != 5 or not linea[4].isdigit():
                errores.writerow(linea)
                continue
            vendedor, monto = linea[2], int(linea[4])
            if vendedor not in res:
                res[vendedor] = 0
            res[vendedor] += monto
    return res


'''
3. Se desea escribir una nota de rescate recortando letras de una revista.
Escribir una funcion que reciba por parametro la nota que se desea escribir y el texto
completo de la revista, y devuelva True si la revista contiene todas las letras necesarias para
escribir la nota (ignorando mayusculas y minusculas), False en caso contrario. Ejemplo: Si
la revista contiene "Algoritmos y Programacion", podemos escribir la nota "Gracias por la
moto"
'''
def escribir_nota(nota, texto):
    res = {}
    for letra in texto.lower():
        res[letra] = res.get(letra, 0) + 1
    for letra in nota.lower():
        if letra == ' ': continue
        res[letra] = res.get(letra, 0) -1
        if res[letra] < 0:
            return False
    return True


        

'''
Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la cantidad de localidades para el mismo;
de modo tal que cumpla el siguiente comportamiento:

>>> b = Boleteria("Rush",500)                       >>> b.localidades_agotadas()
>>> print(b)                                        False
Evento: Rush - Localidades vendidas: 0 de 500       >>> b.vender_localidades(100)
>>> b.vender_localidades(400)                       >>> b.localidades_agotadas()
>>> b.vender_localidades(200)                       True
Traceback (most recent call last):                  >>> print(b)
...                                                 Evento: Rush - Localidades vendidas: 500 de 500
ValueError: No hay localidades suficientes
'''

class Boleteria:
    def __init__(self, evento, capacidad):
        self.evento = evento
        self.capacidad = capacidad
        self.disponibles = capacidad
    
    def vender_localidades(self, cantidad):
        if self.disponibles - cantidad < 0:
            raise ValueError("No hay localidades suficientes")
        self.disponibles -= cantidad
    
    def localidades_agotadas(self):
        return self.disponibles == 0

    def __str__(self):
        return f"Evento: {self.evento} - Localidades vendidas: {self.capacidad - self.disponibles} de {self.capacidad}"
        



    
        
