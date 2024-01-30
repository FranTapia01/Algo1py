
cosa = [1,2,3,4,5]
a = set(cosa)
a.add(9)
a.add('pato')
hola = a.copy()
hola.add(66)
a.add(10)
a.remove(1)
a.clear()



print (a & hola)