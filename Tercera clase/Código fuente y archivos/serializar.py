import pickle #Librería para serializar los objetos
SUELDO_BASE = 80000
"""
    Definiremos un diccionario 
    Empleado que tiene los siguientes
    atributos:
    +------------+
    |  Empleado  |
    +------------+
    |IDEmpleado  |
    +------------+
    |Nombre      |
    +------------+
    |Apellido    |
    +------------+
    |Antiguedad  |
    +------------+
    |Sueldo*     | (Base = 80.000, 15% por aca año de antiguedad)
    +------------+
"""
def serializar(lista_empleados,nombre_archivo,escribir_agregar):
    modo = 'wb' if escribir_agregar == True else 'a' #SE DEBE ESCRIBIR EN BINARIO
    with open(nombre_archivo,modo) as archivo:
        for empleado in lista_empleados:
            pickle.dump(empleado,archivo) #Serializa el objeto

def deserilizar(nombre_archivo,lista_empleados):
    with open(nombre_archivo,'rb') as archivo:
        fin_archivo = False
        while (not fin_archivo):
            try:
                empleado = pickle.load(archivo)
                lista_empleados.append(empleado)
            except EOFError:
                fin_archivo = True

def imprimir_datos(empleado):
    print('Empleado ID: {0}'.format(empleado.get('IDEmpleado','Error en key')))
    print('Nombre: {0} \t Apellido: {1}'.format(
        empleado.get('Nombre','Error en key'),
        empleado.get('Apellido','Error en key')
        ))
    print('==========================')
    print('Antiguedad: {0} años \t Sueldo Neto: {1:.2f}'.format(
        empleado.get('Antiguedad','Error en key'),
        SUELDO_BASE*0.15*empleado.get('Antiguedad','Error en key')
        ))
    print('\t\t---o---')

def main():
    empleado = {}
    lista_empleados = []
    empleado['IDEmpleado'] = '00000001'
    empleado['Nombre']     = 'Homero'
    empleado['Apellido']   = 'Simpson'
    empleado['Antiguedad'] = 25
    lista_empleados.append(empleado)
    empleado = {}
    empleado['IDEmpleado'] = '00000010'
    empleado['Nombre']     = 'Peter'
    empleado['Apellido']   = 'Griffin'
    empleado['Antiguedad'] = 10
    lista_empleados.append(empleado)
    empleado = {}
    empleado['IDEmpleado'] = '00000011'
    empleado['Nombre']     = 'Stan'
    empleado['Apellido']   = 'Smith'
    empleado['Antiguedad'] = 30
    lista_empleados.append(empleado)        
    print('Datos:')
    for empleado in lista_empleados:
        imprimir_datos(empleado)
    archivo = 'empleado.data'
    serializar(lista_empleados,archivo,True)
    print('Serializacion finalizada')
    lista_deserilizacion = []
    deserilizar(archivo,lista_deserilizacion)
    print('Objetos leidos... Imprimiendo datos')
    for empleado in lista_deserilizacion:
        imprimir_datos(empleado)
main()