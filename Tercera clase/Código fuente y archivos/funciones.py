def funcionTipoUno(): #¡Ojo! Aqui van dos puntos y hay que indentar
    #Diremos Tipo 1 a la función que no recive ni devuelve nada
    print('Hola, no recibo ni devuelvo nada')

def funcionTipoDos(mensaje):
    #Diremos Tipo 2 a la función que recive N args ni devuelve nada
    print('Hola, yo recibo {0}'.format(mensaje.upper()))

def funcionTipoTres():
    #Diremos Tipo 3 a la función que no recive nada pero devuelve algo
    print('Voy a devolver algo...')
    return 'algo'

def funcionTipoCuatro(mensaje):
    #Diremos Tipo 4 a la función que recive N args y devuelve algo
    print('Hola, yo recibo {0}'.format(mensaje.upper()))
    return 'algo'.lower()

#Llamadas a las funciones
mensaje = 'Mi MeNsAjE'
funcionTipoUno()
funcionTipoDos(mensaje)
mensaje = funcionTipoTres()
mensaje = funcionTipoCuatro(mensaje)
print(mensaje)