lista = list(range(10))
print(lista) #Lista original
primerosTres = lista[0:3] #[0,1,2]
#El slicing se compone de la forma:
#   lista[inicio : fin]
#Y toma los elementos desde inicio, hasta
# (fin-1)
ultimosTres = lista[-3:]
#La ultima posición es -1, y desde esa posición
#hacia adelante se decrementa en 1
print(primerosTres)
print(ultimosTres)
tomaDeADos = lista[::2] #Si no se establace
#el inicio o fin, se toma la primera y ultima
#posición de la lista
print(tomaDeADos)