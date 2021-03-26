import random as rd
class Moneda:
    def __init__(self):
        self.__cara_cruz = 'cara'
    def lanzar(self):
        '''
        Método que genera un número aleatorio y determina el estado de la moneda
        @param Ninguno
        @return Nada
        '''
        if (rd.randint(0,1)):
            self.__cara_cruz = 'cara'
            print('Toss a coin to your Witcher...')
        else:
            self.__cara_cruz = 'cruz'
            print('O\' Valley of Plenty...')
    def getEstado(self):
        '''
        Devuelve el estado de la moneda
        @param Ninguno
        @return Estado de la moneda 'cara' o 'cruz'
        '''
        return self.__cara_cruz
    def setEstado(self,estado):
        '''
        Establece el estado de la moneda
        @param Nuevo estado
        @return Nada
        '''
        self.__cara_cruz = estado    
def main():
    moneda_geralt = Moneda() 
    print(moneda_geralt.getEstado())
    for l in range(3):
        moneda_geralt.lanzar()
        print(moneda_geralt.getEstado())
    if moneda_geralt.getEstado() == 'cara':
        moneda_geralt.setEstado('cruz')
    else:
        moneda_geralt.__cara_cruz = 'cara'
    print('Estado final',moneda_geralt.getEstado())
    print('Fin programa')
main()