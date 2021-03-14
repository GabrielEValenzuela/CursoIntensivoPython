lista = list(range(5))
print('Lista original: {0}'.format(lista))
print('Método append')
#append(x) añade un elemento al final de la lista
lista.append(5)
print('Lista modificada: {0}'.format(lista))
print('Método insert')
#insert(i,x) inserta un elemento en una posición 
#determinada. Si existe elemento en esa posición,
#se desplazan los otros elementos
lista.insert(6,6)
print('Lista modificada: {0}'.format(lista))
print('Método remove')
#remove(x) remueve el PRIMER elemento cuyo valor
#es igual a x
lista.insert(6,6)
print('Lista modificada: {0}'.format(lista))
lista.remove(6)
print('Lista modificada: {0}'.format(lista))
print('Método count')
#Cuenta la cantidad de veces que x aparece
print('Cuenta {0}'.format(lista.count(6)))
print('Lista modificada: {0}'.format(lista))
print('Método index')
#Retorna el indidce del primer elemento cuyo valor
#es igual x. PUEDE GENERAR UN ValueError sino
#se encuentra
print('Valor en índice {0}: {1}'.format(6,lista.index(6)))
print('Método clear')
#Borra todos los elementos de la lista
lista.clear()
print('Lista modificada: {0}'.format(lista))
print('-----Fin programa-----')