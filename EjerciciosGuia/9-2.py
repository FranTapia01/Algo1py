import random
'''
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.

b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
dena de texto, y los devuelva en un diccionario.


c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
dados.
Nota: utilizar el módulo random para obtener tiradas aleatorias.
'''


import re


def contar_palabras(cadena):
    res = {}
    for palabra in cadena.split():
        res[palabra] = res.get(palabra, 0) + 1
    return res


def contar_caracteres(cadena):
    res = {}
    for c in cadena:
        if c != ' ':
            res[c] = res.get(c, 0) + 1
    return res


def tirada(cant):
    dado = [1, 2, 3, 4, 5, 6]
    tiradas = []
    res = {}
    for _ in range(cant):
        tiradas.append(random.choice(dado) + random.choice(dado))
   
    for tirada in tiradas:
        res[tirada] = res.get(tirada, 0) +1
    return res
