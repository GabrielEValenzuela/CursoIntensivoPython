temperatura = 30
humedad     = 0.1 
if (temperatura >= 30): #Las sentencias if SIEMPRE terminan con :
    if (humedad > 0.5):
        #<-- Indentado del if interno, ojo !
        print("¡¿Por qué me persigue la desgracia?!")
    else:
        print("Que calor que hace en el balc\u00F3n de Paul \U0001F3B5")
else: #De nuevo, SIEMPRE terminar con :
    if (humedad < 0.2):
        print("Libre soy, libre soy \U0001F3B5 \U0001F3B5")
    else:
        print("¡Que hermoso día! \U00002744") #Y no olvidarse el indentado