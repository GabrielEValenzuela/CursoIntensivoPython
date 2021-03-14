myConjunto = set() #Crea un conjunto vacío, puede tomarse
#un objeto itrable (lista,tupla,cadena)
myConjunto = set('aaabc')
print(myConjunto)
myConjuntoDos = set(['a','b','c'])
myConjuntoTres = set(['a','d','e'])
print('Longitud del conjunto {0}'.format(len(myConjunto)))
myConjunto.add('d') #add(x) añade el elemnto x al conjunto
print(myConjunto)
myConjunto.update(['abc','def']) #update(iterable) añade una secuencia de valores
print(myConjunto)
myConjunto.discard('d') #discard(x) remueve x del conjunto
print(myConjunto)
#Para iterar se puede usar un ciclo for
for dato in myConjunto:
    print(dato)
#Y in o not in para buscar un valor
if 'abc' in myConjunto:
    print('abc!')
#Los conjuntos se pueden "concatenar" mediante la union
print(myConjuntoDos.union(myConjuntoTres))
#Los elementos son todos los del conjutuno uno y dos
#Se puede hacer una intersección tambien
print(myConjuntoDos.intersection(myConjuntoTres))
#Solo tienen los valores que tienen en común ambos conjuntos
#La diferencia retorna los elementos que están en el primer
#conjunto y no en el segundo
print(myConjuntoDos.difference(myConjuntoTres))
#La diferencia simétrica devuelve los elementos que
#se encuentran en el primer o segundo conjunto pero no
#en ambos
print(myConjuntoDos.symmetric_difference(myConjuntoTres))
#Se puede saber si un subconjunto está dentro de un conjunto
#O superconjunto
print(myConjuntoDos.issubset(myConjuntoTres))
print(myConjuntoDos.issuperset(myConjuntoTres))