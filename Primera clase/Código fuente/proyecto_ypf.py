import math as m #Una libreria con un alias
import time
#from math import pi Una funcion o variable
#import math Toda la libreria
"""
    El volumen de combustible almacenado en un tanque cilíndrico enterrado en el subsuelo
    a 200 metros de profundidad está determinado por la medición de la distancia de la parte
    superior del tanque a la superficie del combustible. Conociendo esta distancia y el radio
    del tanque, el volumen de combustible en el tanque puede determinarse usando la
    fórmula volumen = π radio**2*(200 – distancia).

    Datos del usuario:
    ------------------
        Distancia medida
        Tipo de combustible
        Número de tanque
        Nombre del encargado
        Radio del tanque

    Salida esperada:
    ----------------
    Tanque N°: NN       Encargado: AAAAAAAAAA
    Tipo combustible:   CCCCCCCCCCCCC
    --------Características---------- (10's -)
    Radio: RR [m]      Distancia medida: MM [m]
    ---------------------------------
    Volumen de combustible: VV [m3]
"""
distanciaMedida = 0
radioTanque     = 0.0
volumenTanque   = 0.0
tipoCombustible = ""
encargado       = ""
numeroTanque    = ""
print('\t \t Calculador de volumen de combustible v.0.1')
distanciaMedida = float(input('Distancia medida (m) >> '))
radioTanque     = float(input('Radio del tanque (m) >> '))
tipoCombustible = input('Tipo de combustible >> ')
encargado       = input('Encargado  >> ')
numeroTanque    = input('Numero de tanque >> ')
volumenTanque   = m.pi*(radioTanque**2)*(200-distanciaMedida)
print('Procesando informacion.')
time.sleep(2)
print('Procesando informacion..')
time.sleep(2)
print('Procesando informacion...\n \n')
print('\t Resultados \n')
print('Tanque N°: {0} \t \t Encargado: {1}'.format(numeroTanque,encargado))
print('Tipo combustible:',tipoCombustible,sep='\t')
print('--------Características----------')
print('Radio: {0:.2f}[m]      Distancia medida: {1:.2f}[m]'.format(radioTanque,distanciaMedida))
print('---------------------------------')
print('Volumen de combustible: {0:.2f}[m3]'.format(volumenTanque))