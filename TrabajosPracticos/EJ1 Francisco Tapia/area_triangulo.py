import vectores

"""funcion que pide 3 puntos en r3 y devuelve el area del triangulo que forma"""

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    
    ab_x, ab_y, ab_z = vectores.diferencia(x2, y2, z2, x1, y1, z1)
    ac_x, ac_y, ac_z = vectores.diferencia(x3, y3, z3, x1, y1, z1)
    
    xp, yp, zp = vectores.prod_vectorial(ab_x, ab_y, ab_z, ac_x, ac_y, ac_z )

    area = vectores.norma(xp, yp, zp)

    return (area/2)

assert area_triangulo(-2, 0, 2, -5, 2, 0, 6, -3, 7) == (4.06201920231798)
assert area_triangulo(8, 1, 3, 6, 5, 0, 2, 1, 2) == (14.560219778561036)
assert area_triangulo(5, 1, 5, 50, 23, 2, 25, 21, 3) == (230.62740513651016)