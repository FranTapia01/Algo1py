'''Ejercicio 11.3. Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.'''

def wc(ruta):
    lineas = 0
    palabras = 0
    caracteres = 0
    with open(ruta) as f:
        for linea in f:
            lineas += 1
            for palabra in linea.split():
                palabras += 1
            for c in linea:
                caracteres += 1 
    print(f"el archivo tiene {lineas} lineas, {palabras} palabras y {caracteres} caracteres")


wc("archivo.txt")