import random as rd

lista = list(range(20))
#Range devuelve una secuencia de 0 a 19
#Esa secuencia se pasa a la función list que la transforma
#en una lista
print('Lista desde for')
for dato in lista:
    print('El dato es {0}'.format(dato))
#El resultado sería igual a
print('\nLista desde for accedido por indice')
for indice in range(len(lista)): #len(secuencia) nos devuelve la longitud
    #de una secuencia, al ser un valor entero, range lo toma y calcula la 
    #secuencia desde 0 hasta longitudSecuencia - 1
    print('El dato es {0}'.format(lista[indice])) #El operador de indexación es []
print('--------')
#A través de dicho operador se puede llevar a cabo las modificaciones
indiceAleatorio = rd.randint(0,len(lista)-1) #0,19
numeroAleatorio = rd.randint(-len(lista),len(lista)) #-20,20
print('Lista antes de modificarse: {0}'.format(lista))
lista[indiceAleatorio] = numeroAleatorio
print('Lista despues de modificarse: {0} en {1} con el valor {2}'.format
(lista,indiceAleatorio,numeroAleatorio))