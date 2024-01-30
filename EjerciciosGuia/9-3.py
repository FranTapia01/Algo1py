'''
Ejercicio 9.3. Continuación de la agenda.
Escribir un programa que vaya solicitando al usuario que ingrese nombres.
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena ”*”, para salir del programa.
'''

def agenda():

    agenda = {}
    while True:
        
        nombre = input("ingrese un nombre o '*' para salir: ")
        if nombre == "*":
            break

        if nombre not in agenda:
            agenda[nombre] = "sin numero"
        print(f"{nombre} -> {agenda[nombre]}")
    
        numero = input(f"si quiere cambiar el numero de {nombre} ingreselo, sino presione enter: ")
        if numero != '':
            agenda[nombre] = numero
            print(f"el nuevo numero de {nombre} es {numero}")
        
agenda()
        



