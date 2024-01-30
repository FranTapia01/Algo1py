'''
Ejercicio 12.5. Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:
17

>>> analisis2 = Materia("61.03", "Análisis 2", 8)
>>> fisica2 = Materia("62.01", "Física 2", 8)
>>> algo1 = Materia("75.40", "Algoritmos 1", 6)
>>> c = Carrera([analisis2, fisica2, algo1])
>>> str(c)
Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
>>> c.aprobar("95.14", 7)
ValueError: La materia 75.14 no es parte del plan de estudios
>>> c.aprobar("75.40", 10)
>>> c.aprobar("62.01", 7)
>>> str(c)
Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
75.40 Algoritmos 1 (10)
62.01 Física 2 (7)
'''

class Materia():
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

class Carrera():
    def __init__(self, materias):
        self.materias = materias
        self.creditos = 0
        self.promedio = "N/A"
        self.materias_aprobadas = []


    def __str__(self):
        return f"Creditos: {self.creditos} -- Promedio: {self.promedio} -- Materias Aprobadas: {self._materias_a_str()}"#falta


    def aprobar(self, codigo, nota):
        for materia in self.materias:
            if codigo == materia.codigo:
                self.creditos += materia.creditos
                self.materias_aprobadas.append([materia.codigo, materia.nombre, nota])
                self.promedio = self._calcular_promedio()
                return
        raise ValueError(f"La materia {codigo} no es parte del plan de estudios")


    def _calcular_promedio(self):
        suma = 0
        for materia in self.materias_aprobadas:
            suma += materia[2]
        return suma / len(self.materias_aprobadas)
            
    def _materias_a_str(self):
        texto = ''
        for materia in self.materias_aprobadas:
            texto += f"\n{materia[0]} {materia[1]} ({materia[2]})"
        return texto
