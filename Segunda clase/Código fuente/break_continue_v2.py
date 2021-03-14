import random as rd

aleatorio = 0
intentos  = 0

ACIERTO   = 7 #Declaracion de valor constante (Mayúsculas)

while(True): #bucle infinito...
    aleatorio = rd.randint(0,10)
    if(aleatorio == ACIERTO):
        break #Termina ejecución de bucle y las
    #sentencias posteriores NO se ejecutan
    else:
        continue #Se vuelve al comienzo del loop
        #¿Qué produce esto?
        intentos += 1
print('Se necesitaron {0} intentos'.format(intentos))