rango_v1 = range(5) #0,1,2,3,4
rango_v2 = range(-5,5) #-5,-4,-3,-2,-1,0,1,2,3,4
rango_v3 = range(-5,5,2) #-5,-3,-1,1,3
#range(inicio,final,salto) es una función definida en Python
#Viene de 3 sabores:
#   -> range(final): 
#   genera una secuencia de datos desde 0 hasta final - 1
#   -> range(inicio,final): 
#   genera una secuencia de datos desde inicio hasta final - 1
#   -> range(inicio,final,salto): 
#   genera una secuencia de datos desde inicio hasta final - 1, cada salto valores
for valor in rango_v1:
    print(valor,end='\t')
print('\nFin for v1')
for valor in rango_v2:
    print(valor,end='\t')
print('\nFin for v2')
for valor in rango_v3:
    print(valor,end='\t')
print('\nFin for v3')