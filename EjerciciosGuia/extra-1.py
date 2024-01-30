'''
Se tiene un archivo con el siguiente formato <nombre persona>;<lugar>;<momento en que la persona estuvo alli>.

Escribir una funcion que reciba la ruta a este archivo y el nombre de una persona y devuelva un conjunto con todas las personas con las que tuvo contacto. 
Una persona tuvo contacto con otra si estuvieron en el mismo lugar en el mismo momento).

Notas:

El archivo no se encuentra ordenado bajo ningún criterio y no posee errores de formato ni de tipo de datos. No posee encabezado.
El archivo puede recorrerse una única vez.
Cada persona puede haber estado en multiples lugares en múltiples momentos distintos (inclusive múltiples momentos para el mismo lugar).
El tipo de dato para el "momento" no importa, tratarlo como una cadena.
'''
import csv

def encuentros(ruta, persona):
    res = {}
    with open(ruta) as f:
        for nombre, lugar, momento in csv.reader(f, delimiter=';'):
            res[nombre] = res.get(nombre, [])
            res[nombre].append([lugar, momento])

    encuentro = set()
    for nombre in res:
        for lugar_y_momento in res[nombre]:
            if lugar_y_momento in res[persona] and nombre != persona:
                encuentro.add(nombre)

    return encuentro

print(encuentros('datos.txt', 'julian'))