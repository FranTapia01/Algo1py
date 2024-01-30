from re import A
from xml.dom.minidom import Element
from pila import Pila
from cola import Cola
"""
La suma digital de un número n es la suma de sus dígitos. 
Escribir la función recursiva suma_digital(n) que recibe un número entero positivo y devuelve su suma digital. 
No se permite convertir el número a cadena. Ejemplo: suma_digital(2019) → 12 (porque 2+0+1+9 = 12).
"""


def suma_digital(n):
    if  n//10 == 0:
        return n
    return n%10 + suma_digital(n//10)


"""
Escribir una función recursiva que recibe una cadena s y un caracter c, y devuelve la cantidad de apariciones de c en s.
"""

def _contar_apariciones(s, c, i):
    if i == len(s):
        return 0
    
    i += 1
    if s[i] == c:
        return contar_apariciones(s, c) +1
    return contar_apariciones(s, c) 
    

def contar_apariciones(s, c):

    return _contar_apariciones(s, c, 0)

#print(contar_apariciones('estrepitoso', 'e'))

"""
Escribir una función recursiva que reciba una pila la modifique de tal forma que el valor del tope se mueva hacia el fondo,  
manteniendo el orden del resto de los elementos. Por ejemplo, para la siguiente pila: 
fondo >| 5, 4, 3, 2, 1 >| tope 
la función debe modificarla para que quede: 
fondo >| 1, 5, 4, 3, 2 >| tope 
"""

def _mover_tope(pila, elemento):
    if pila.esta_vacia():
        pila.apilar(elemento)
        return
    siguiente = pila.desapilar()
    _mover_tope(pila, elemento)
    pila.apilar(siguiente)

def mover_tope(pila):
    elemento = pila.desapilar()
    _mover_tope(pila, elemento)

""" 
Ejercicio 187 colas
Dada una cola con enteros y un número k, escribir una función obtener_suma_maxima que devuelve 
la mayor suma posible entre cualquiera k elementos consecutivos de la estructura. 
Ejemplos para c = Cola([3, 1, 9, 2, 3, 6]):

obtener_suma_maxima(c, 3)  =>  Devuelve 14, por la suma de [9, 2, 3]
obtener_suma_maxima(c, 4)  =>  Devuelve 20, por la suma de [9, 2, 3, 6]
obtener_suma_maxima(c, 15)  =>  Devuelve 24, por la suma de todos los elementos
No es necesario que la cola quede en su estado original al finalizar la ejecución.
"""


def obtener_suma_maxima(cola, k):
    aux = []
    maxima = 0

    while not cola.esta_vacia():
        while len(aux) < k and not cola.esta_vacia():
            
            aux.append(cola.desencolar())

        
        if sumar(aux) > maxima:
            maxima = sumar(aux)
        aux.pop(0)
    return maxima

def sumar(l):
    print(l)
    suma = 0
    for i in range(len(l)):
        suma += l[i]
    return suma
    
cola = Cola()
cola. encolar(3)
cola. encolar(1)
cola. encolar(9)
cola. encolar(2)
cola. encolar(3)
cola. encolar(6)
print(obtener_suma_maxima(cola, 25))
        


