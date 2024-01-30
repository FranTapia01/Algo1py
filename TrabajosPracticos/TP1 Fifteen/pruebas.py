from code import interact
from operator import truediv
from sqlite3 import enable_callback_tracebacks


def verificar_codigo(codigo):
    suma = 0
    codigo = codigo.split("-")
    print(codigo)
    for i in range (len(codigo[0])):
        suma += int(codigo[0][i])
    
    if suma % 10 == int(codigo[1]):
        print("valido")
    else:
        print("invalido")

def sumar_columnas(matriz):
    resultado = []

    for j in range(len(matriz[0])):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        resultado.append(suma)
    return resultado


def lista_super():
    lista = []
    while True:
        entrada = input("ingrese mensaje: ")
        for x in entrada:
            if x.isdigit:
                break


    