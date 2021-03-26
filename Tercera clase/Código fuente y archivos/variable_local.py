def main():
    obtenerNombre()
    print('Hola {0}'.format(nombre)) #¡Error!

def obtenerNombre():
    nombre = input('¿Como te llamas?')

main()