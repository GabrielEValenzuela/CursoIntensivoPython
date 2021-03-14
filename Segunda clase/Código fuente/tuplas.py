tupla = tuple(range(10))
print('Tupla {0}'.format(tupla))
tuplaVacia = ()
print('Tupla vacía {0}'.format(tuplaVacia))
generador = (0,) * 10
print('Generador {0}'.format(generador))
concatenacion = generador + tupla
print('Concatenacion {0}'.format(concatenacion))
print(concatenacion[18]) #Acceso elemento
print(tupla[1:5]) #Slicing