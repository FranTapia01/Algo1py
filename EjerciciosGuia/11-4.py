'''
Ejercicio 11.4. Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima
las líneas del archivo que contienen la cadena recibida.
'''

def grep(cadena, archivo):
    with open(archivo) as f:
        for linea in f:
            if cadena in linea:
                print(linea.strip("\n"))


grep('s', "archivo.txt")