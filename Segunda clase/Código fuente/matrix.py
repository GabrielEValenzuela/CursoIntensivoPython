import random as rd 

FILAS    = 4
COLUMNAS = 3

matrix = [[0]*COLUMNAS]*FILAS
print('Matrix vacia {0}'.format(matrix))

for i in range(FILAS):
    for j in range(COLUMNAS):
        matrix[i][j] = rd.randint(0,(FILAS*COLUMNAS)) 
        #Para matrices se usa el primer
        #[] para fila y el segundo [] la columna
print('Matrix modificada {0}'.format(matrix))