def leerArchivo(ubicacion_nombre):
    archivo = open(ubicacion_nombre,"r")
    #open(path,modo) permite abrir el archivo en diversos modos
    #r -> Lectura           w-> Escritura           a-> Añadir
    #rb -> Lectura binario  wb-> Escritura binario
    #El path en Windows debe hacerse con r'LocacionArchivo'
    todo_contenido = archivo.read()
    print('Todo el contenido:')
    print(todo_contenido)
    print('Se imprime linea por linea:')
    archivo.seek(0) #Se resetea el valor de la posicion de lectura
    for linea in archivo:
        print(linea,end='')
    archivo.seek(0)
    print('\nLectura mediante while y readline():')
    linea = archivo.readline() #Se lee hasta un '\n'
    while (linea != ''):
        print(linea,end='')
        linea = archivo.readline()
    archivo.close() #FUNDAMENTAL ¡NO OLVIDARSE DE CERRAR EL ARCHIVO!

def main():
    archivo = "archivo.txt"
    leerArchivo(archivo)
    print('\nFin programa')
main()