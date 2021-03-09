#Nuevo fomato de sintaxis que soporta nuevas y diferentes opciones
print('{0}, {1}, {2}'.format('a','b','c'))
#Se puede acceder por nombre de las variables
print('Coordendas: {lat}, {long}'.format(lat='38.23N',long='-114.81O')) 
#Salida en diferentes representaciones numéricas
print('int: {0:d}, hex: {0:x}, oct {0:o}, bin{0:b}'.format(16)) 
#Despliega la cantidad de cifras decimales
print('Valor decimal: {:.2%}'.format(1/3)) 