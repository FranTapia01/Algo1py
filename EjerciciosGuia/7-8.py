def invertir(lista):
    for i in range(len(lista)):   
        lista.insert(0, lista.pop(i))
        

lista = ['Di', 'buen', 'día', 'a', 'papa']
invertir(lista)
print(lista)
