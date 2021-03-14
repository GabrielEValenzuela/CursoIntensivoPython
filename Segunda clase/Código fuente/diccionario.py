agenda = {'Batman':'555-1111','Iron Man':'555-2222','Wonder Woman':'555-33333'}
print(agenda)
#Para acceder a los datos del diccionario se usa el operador
#[]. SI LA LLAVE NO EXISTE GENERA UN KEYERROR
print('El teléfono de Batman es {0}'.format(agenda['Batman']))
#Para añadir un dato, hacemos uso del mismo operador
agenda['Superman'] = '555-5555'
print(agenda)
#Nota: Las comparaciones de cadenas son sensibles a mayúsculas
#Puede usarse in y not in para prevenir los KeyError
if 'Guason' in agenda:
    print('HAAAAAAAAHAHAHA')
else:
    print('Falta the joker')
#Para eliminar un elemento hacemos uso de la funcion del
del agenda['Iron Man']
print(agenda)
#La funcion len nos dice cuantos elementos tiene el diccionario
print('Diccionario de {0} elementos'.format(len(agenda)))
#Los diccionarios pueden tener multiples valores
dicc = {'A':1,'B':3.14,'C':[0,1,2],'D':'E'}
print(dicc)
#Un diccionario puede crearse vacío
diccionarioVacio = {}
#O con la funcion dict()
diccionarioDict = dict(m=8, n=9)
#Algunos métodos son
dicc.clear() #Elimina todos los elementos
dicc.get('Batman','No key') #Obtiene un valor por la llave
#Y sino existe devuelve el valor por defecto sin generar
#excepción
dicc.items() #Retorna el conjunto de llave-valor
dicc.keys() #Retorna todas las llaves del diccionario en una secuencia
dicc.pop('Batman','No key') #Similar a get para remover elemento
dicc.values() #Retorna todas los valores del diccionario en una secuencia