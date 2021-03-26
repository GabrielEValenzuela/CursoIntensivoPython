import random as rd
class Moneda:
    #Para crear una clase se usa la palabra
    #reservada class seguida del nombre de la clase.
    def __init__(self):
    #Este método es una característica de Python que se usa
    #para dos razones:
    #Primero inicializa el objeto, poniendolo en un estado apropiado
    #cuando se crea
    #Segundo es que __init__ puede tomar muchas formas, permitiendo
    #poder definir como se crea el objeto o inicializa
        self.cara_cruz = 'cara'
    def lanzar(self):
        '''
        Método que genera un número aleatorio y determina el estado de la moneda
        @param Ninguno
        @return Nada
        '''
        #self es lo que marca la diferencia entre método o función 
        # (Si bien son prácticamente lo mismo).
        #Es un análogo al "this" de otros lenguajes, 
        # y lo que hace es una referencia al objeto que
        # el método hace cuando se invoca. 
        #Podemos acceder a atributos y métodos
        # de un objeto como si fuera cualquier otro objeto.
        if (rd.randint(0,1)):
            self.cara_cruz = 'cara'
            print('Toss a coin to your Witcher...')
        else:
            self.cara_cruz = 'cruz'
            print('O\' Valley of Plenty...')
    def getEstado(self):
        '''
        Devuelve el estado de la moneda
        @param Ninguno
        @return Estado de la moneda 'cara' o 'cruz'
        '''
        return self.cara_cruz
    def setEstado(self,estado):
        '''
        Establece el estado de la moneda
        @param Nuevo estado
        @return Nada
        '''
        self.cara_cruz = estado    
#Los métodos get y set se llaman mutadores y son la principal herramienta
#para poder establecer (set) u obtener (get) el estado de un objeto
def main():
    moneda_geralt = Moneda() #Con esta linea, creamos una nueva instancia de 
    #un objeto moneda
    print(moneda_geralt.getEstado()) #Invocamos el metodo get
    for l in range(3):
        moneda_geralt.lanzar()
        print(moneda_geralt.getEstado())
    if moneda_geralt.getEstado() == 'cara':
        moneda_geralt.setEstado('cruz')
    else:
        moneda_geralt.cara_cruz = 'cara'
    print('Fin programa')
main()