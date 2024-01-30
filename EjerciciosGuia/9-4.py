'''Ejercicio 9.4. Escribir una función que reciba un texto y para cada caracter presente en el texto
devuelva la cadena más larga en la que se encuentra ese caracter.'''

texto = "hola como estan el dia de hoy amigos"


def mas_larga(texto):
    res = {}
    palabras = texto.split()

    for c in texto:
        if c not in res and c != ' ':
            res[c] = ''

        for palabra in palabras:
            if c in palabra and len(res[c]) < len(palabra):
                res[c] = palabra
    
    return res

print(mas_larga(texto))