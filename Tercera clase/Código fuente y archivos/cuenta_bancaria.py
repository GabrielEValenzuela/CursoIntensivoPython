import random as rd

class CuentaBancaria:

    def __init__(self,balance):
        self.__balance = balance #__variable significa que la variable es "PRIVADA"
    
    def deposito(self, cantidad): #Setter
        self.__balance += cantidad

    def extraccion(self,cantidad): #Setter
        if(cantidad > self.__balance): 
            #Definir una excepción particular
            raise Exception("No tenes guita papu")
        else:
            self.__balance -= cantidad
    def getBalance(self):
        return self.__balance

def main():
    cuenta = CuentaBancaria(1000)
    print('Balance inicial {0}'.format(cuenta.getBalance()))
    while(True):
        metodo = rd.randint(0,1)
        try:
            if(metodo):
                cuenta.deposito(rd.randint(10,100))
                print('Nuevo balance {0}'.format(cuenta.getBalance()))
            else:
                cuenta.extraccion(rd.randint(20,1000))
                print('Nuevo balance {0}'.format(cuenta.getBalance()))
        except Exception as e:
            print(e)
            break
    cuenta.__balance = 10000
    print('Balance final {0}'.format(cuenta.getBalance()))
    print('Sin fondos')
main()