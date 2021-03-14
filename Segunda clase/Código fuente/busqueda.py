dias = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
buscarDia = input('Ingrese día: ')
if buscarDia in dias:
    print('El día existe')
else:
    print('404 - Calendario not found')