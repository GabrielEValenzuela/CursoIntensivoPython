import math as m

def leerArchivoContextManager(ubicacion_nombre):
    with open(ubicacion_nombre,"r") as archivo:#El context manager automaticamte
        #cierra el archivo
        for linea in archivo:
            print(linea,end='')

def escribirArchivo(ubicacion_archivo,nuevo_append,lista_datos):
    modo = "w" if nuevo_append == True else "a"
    archivo = open(ubicacion_archivo,modo)
    for dato in lista_datos:
        archivo.write(dato)
    archivo.close()
def main():
    archivo = "archivo.txt"
    leerArchivoContextManager(archivo)
    print('\nAhora se añaden datos...')
    datos = [
        '\n***\n',
        'Esto es la nueva linea y debe añadirse\n',
        'Siempre debe ser una cadena\n',
        '¡Ojo!\n',
        'Para Python pi='+str(m.pi)+'\n'
        ]
    escribirArchivo(archivo,False,datos)
    print('Se lee con nueva funcion:')
    leerArchivoContextManager(archivo)
    print('\nFin programa')
main()