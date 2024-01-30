'''
Ejercicio 12.3.
a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
misma cantidad de elementos debe levantar una excepción.
c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
los elementos multiplicados por ese número.
'''

class Vector:
    def __init__(self, vector):    
        self.vector = vector
    
    def __str__(self):
        return(f"{self.vector}")
    
    def __add__(self, otro):
        if len(otro.vector) == len(self.vector):
            nuevo = []
            for i in range(len(otro.vector)):
                nuevo.append(otro.vector[i]+self.vector[i])
            return Vector(nuevo)
        raise ValueError("vectores de diferente longitud")
        

    def __mul__(self, numero):
        nuevo = []
        for cord in self.vector:
            nuevo.append(cord*numero)
        return Vector(nuevo)

