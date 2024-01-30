from __future__ import print_function
from audioop import mul


def ordenar_parimpar(lista):
    nueva_lista = []
    for x in lista:
        if x % 2 == 0:
            nueva_lista.insert(0, x)
        else:
            nueva_lista.append(x)
    return nueva_lista

def rotar(palabra):
    lista_n = [palabra]
    for _ in range(len(palabra)-1):
        palabra += palabra[0]
        palabra = palabra[1:]
        lista_n.append(palabra[:])
    return lista_n

def multiplos():
    while True:
        a = input("ingrese primer numero positivo entero: ")
        b = input("ingrese segundo numero positivo entero: ")
        if a.isdigit() and b.isdigit():
            break
        print("error intente nuevamente con numeros validos")

    for i in range(int(a)):
        print(int(b)*i)
    return


multiplos()
