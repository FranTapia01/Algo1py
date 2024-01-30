'''
1. Escribir un programa que abra un archivo separado por comas y le pida al usuario dos
numeros. El programa debe escribir en otro archivo el contenido del primero con las columnas
del archivo CSV intercambiadas segun los numeros del usuario. Por ejemplo, si una linea del
archivo es lunes,martes,miercoles,jueves" y los numeros del usuario son 1 y 3, el archivo de
salida sera miercoles,martes,lunes,jueves" (las columnas 1 y 3 estan intercambiadas)
'''
import csv

def intercambiar_columnas(ruta_origen, ruta_destino, c1, c2):
	with open(ruta_origen) as origen, open(ruta_destino, 'w') as destino:
		destino = csv.writer(destino, delimiter='-')
		for fila in csv.reader(origen, delimiter=';'): # fila = [lunes, martes, miercoles, jueves]
			#if max(c1, c2) > len(fila) or min(c1, c2) < 0:
			#	raise IndexError('Estas intentando intercambiar columnas fuera de rango')
			
			fila[c1], fila[c2] = fila[c2], fila[c1]
			print(fila)
			destino.writerow(fila)

def pedir_numero():
	while True:
		entrada = input("Ingrese un numero de columna")
		if entrada.isdigit():
			return int(entrada)
		print("Ingrese un numero no otra cosa")

def main():
	n1, n2 = pedir_numero() - 1, pedir_numero() - 1
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

VENDEDOR = 2
MONTO = 4
CANT_COLUMNAS = 5

def calcular_montos_por_vendedor(ruta_datos, ruta_errores):
	vendedores = {}
	with open(ruta_datos) as datos, open(ruta_errores, 'a') as errores:
		errores = csv.writer(errores)
		for fila in csv.reader(datos): # fila = [año, mes, vendedor, cliente, monto]
			#try:
			#	vendedores[fila[VENDEDOR]] = int(fila[MONTO])
			#except (IndexError, ValueError):
			#	errores.writerow(fila)
			if len(fila) != CANT_COLUMNAS or not fila[MONTO].isdigit():
				errores.writerow(fila)
				continue
			#if fila[VENDEDOR] not in vendedores:
			#	vendedores[fila[VENDEDOR]] = 0
			#vendedores[fila[VENDEDOR]] += int(fila[MONTO])
			
			vendedores[fila[VENDEDOR]] = vendedores.get(fila[VENDEDOR], 0) + int(fila[MONTO])
	return vendedores

# print(calcular_montos_por_vendedor("vendedores.csv", "errores.log"))

'''
3. Se desea escribir una nota de rescate recortando letras de una revista.
Escribir una funcion que reciba por parametro la nota que se desea escribir y el texto
completo de la revista, y devuelva True si la revista contiene todas las letras necesarias para
escribir la nota (ignorando mayusculas y minusculas), False en caso contrario. Ejemplo: Si
la revista contiene "Algoritmos y Programacion", podemos escribir la nota "Gracias por la
moto", pero no se puede escribir "Porotos amargos" (falta una s).
'''

def alcanza_el_texto(revista, texto):
	apariciones = {}
	for letra in revista.lower():
		apariciones[letra] = apariciones.get(letra, 0) + 1
	for letra in texto.lower():
		if letra == ' ': continue
		#if letra not in apariciones or apariciones[letra] < 1:
		#	return False
		apariciones[letra] = apariciones.get(letra, 0) - 1
		if apariciones[letra] < 0:
			return False

	return True

print(alcanza_el_texto('Algoritmos y programacion', 'Gracias por la moto'))
print(alcanza_el_texto('Algoritmos y programacion', 'Porotos amargos'))

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

	def __init__(self, nombre, cantidad_de_localidades):
		self.capacidad = cantidad_de_localidades
		self.nombre = nombre
		self.vendidas = 0

	def __str__(self):
		return f'Evento: {self.nombre} - Localidades vendidas: {self.vendidas} de {self.capacidad}'

	def vender_localidades(self, cantidad_a_vender):
		if self.vendidas + cantidad_a_vender > self.capacidad:
			#print('ValueError: No hay localidades suficientes') !!!! NO !!!!
			#return
			raise ValueError('No hay localidades suficientes')
		self.vendidas += cantidad_a_vender

	def localidades_agotadas(self):
		return self.vendidas == self.capacidad


class Prenda:
	def __init__(self, nombre, tamanio):
		self.tamanio = tamanio
		self.nombre = nombre

class Perchero:

	def __init__(self, capacidad):
		self.capacidad = capacidad
		self.cantidad = 0
		self.prendas = []

	def agregar_prenda(self, prenda):
		if self.cantidad + prenda.tamanio > self.capacidad:
			raise ValueError('No hay espacio suficiente')
		self.prendas.append(prenda)
		self.cantidad += prenda.tamanio

	def remover_prenda(self, una_prenda):
		for i in range(len(self.prendas)):
			if self.prendas[i].nombre == una_prenda.nombre:
				prenda_removida = self.prendas.pop(i)
				self.cantidad -= prenda_removida.tamanio
				return prenda_removida
		raise ValueError('No se encontro la prenda')



'''
Ejercicio 119 objetos
Implementar una clase Carta, que se crea a partir de un palo y un valor.
Las cartas deben poder imprimirse de la forma <valor> de <palo>.
Las cartas deben poder compararse entre ellas: 
Una carta vale menos que otra si al ser del mismo palo su valor es menor, 
o si al ser de distintos palos el propio es menor que el palo de la otra carta
(suponer que ya está implementada una clase Palo, que implementa los métodos __eq__, __lt__ y __str__).
cuando dice  suponer que ya está implementada una clase Palo, que implementa los métodos __eq__, __lt__ y __str__ 

'''


class Carta: # Ojo con probar esto porque la clase Palo no está implementada.

	def __init__(self, valor, palo):
		self.palo = palo
		self.valor = valor

	def __str__(self):
		return f'{self.valor} de {str(self.palo)}'

	def __eq__(self, otro):
		return otro.palo == self.palo and self.valor == otro.valor

	def __lt__(self, otro):
		if self.palo != otro.palo:
			return self.palo < otro.palo
		return self.valor < otro.valor