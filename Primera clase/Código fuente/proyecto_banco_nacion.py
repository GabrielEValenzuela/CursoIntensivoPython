"""
    Interés compuesto

    Cf = Ci*(1 + t)**n

    t = 35%

    Requerimos del usuario:
    -----------------------
        Capital inicial
        Periodo de tiempo
    Salida esperada:
    ----------------
    "Al cabo de n meses, su capital final es de $xxxx. Ud obtuvo $yyyy de ganancia con una tasa de zz.zz%"

"""
TASAINTERES = 0.35 #35% --> Generalmente, las mayusculas representan un valor constante
capitalInicial = 0
capitalFinal   = 0 #Sintaxis camelCase 
periodoTiempo  = 0
#-----------------
print('\t\t Bienvenido al calculador de interes v.0.1 \t\t')
capitalInicial = float(input('Por favor, ingrese su capital inicial: '))
periodoTiempo  = int(input('¿Por cuanto tiempo va a depositar su dinero? '))
capitalFinal   = capitalInicial*(1+TASAINTERES)**periodoTiempo
print("Al cabo de {0} meses, su capital final es de ${1:.2f}. Ud obtuvo ${2:.2f} de ganancia con una tasa de {3:.2%}".format(periodoTiempo,capitalFinal,(capitalFinal-capitalInicial),TASAINTERES))


"""
    Interés compuesto v.2.0.0

    Cf = Ci*(1 + r/n)**nt

    r = Interes anual
    n = La cantidad de veces al año que el interes se calcula
    t = La cantidad de años

    Requerimos del usuario:
    -----------------------
        Capital inicial
        Interes anual
        El numero de veces que el interes se aplica, por ejemplo, si se calcula
        mensualmente, 12. Si se calcula por cuatrimestre seria 4
        El numero de años que se calcula el interes
    Salida esperada:
    ----------------
    "Al cabo de n años con un periodo r, su capital final es de $xxxx. Ud obtuvo $yyyy de ganancia con una tasa de zz.zz%"

"""