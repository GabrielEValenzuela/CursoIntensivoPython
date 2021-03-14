listaPares = list(range(0,10,2))
listaImpares = list(range(1,9,2))
print('Lista pares {0} \nE impares {1}'.format(listaPares,listaImpares))
listaTotal = listaPares + listaImpares
print(listaTotal)
print('\n------------------\n')
#Creo una copia
copiaLista = listaTotal
print('Lista original {0} \nCopia: {1}'.format(listaTotal,copiaLista))
print('------------------')
listaTotal[0] = 10
print('Lista original {0} \nCopia: {1}'.format(listaTotal,copiaLista))
#¿Qué pasó?