import random as rd

MAX_CANTIDAD_ALUMNOS    = 9 
MAX_CANTIDAD_EXAMENES   = 3
cantidadAlumnos         = 0
total                   = 0  
promedio                = 0

while(cantidadAlumnos < MAX_CANTIDAD_ALUMNOS):
    print('Alumno N°{0}'.format(cantidadAlumnos+1))
    print('------------')
    for nota in range(MAX_CANTIDAD_EXAMENES):
        total += rd.randint(2,11) #2 - 10 valores
    promedio = total/MAX_CANTIDAD_EXAMENES
    print('Promedio obtenido {0:.2f}'.format(promedio))
    print('------------------------------------')
    total = 0
    promedio = 0
    cantidadAlumnos += 1
print('Fin programa')