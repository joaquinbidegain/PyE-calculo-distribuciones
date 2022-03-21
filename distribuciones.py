
import math
from scipy.stats import norm


cantidad = int(input("Ingrese el tamano del arreglo: "))
numeros = []
media = 0;
sumacuad = 0;
for i in range(cantidad):
    numero = input(f"Ingresa el número {i + 1}: ")
    numero = float(numero)
    media = numero + media;
    sumacuad = sumacuad + numero*numero;
    numeros.append(numero)

media = float(media/cantidad);

sngrande = float(math.sqrt((sumacuad/cantidad) - (media**2)))
sn = float(math.sqrt((sumacuad/(cantidad - 1)) - (media**2)))

bandera = True;

while bandera == True: 
    mostrar = int(input("Mostrar: 1- MediaMuestral 2-SnGrande 3 - SnChico: "))
    if (mostrar == 1):
        print(f"La media muestral es:{media}")
    elif (mostrar == 2):
        print(f"Sn grande es: {sngrande}")
    elif (mostrar == 3):
        print(f"sn chico es: {sn}")

    aux = int(input("1- Mostrar otro dato, 0- no: "))
    if(aux == 0):
        bandera = False 
    print("---------------------")


tipo = int(input("Seleccione el tipo de distribucion 1-NORMAL 2-EXPONENCIAL 3-LILLIEFORTS: "))

i = 1
cuenta=0

def func_maximo(valor1,valor2):
    maximo = max(valor1)
    maximo2 = max(valor2)
    if (maximo >= maximo2):
        print(f"EL MAXIMO DE LA TABLA ES: {maximo} ")
    elif (maximo < maximo2):
        print(f"EL MAXIMO DE LA TABLA ES: {maximo2}")

if tipo == 1:  
    mu = float(input("Seleccione el valor de mu: "))
    sigma = float(input("Seleccione el valor de sigma: "))
    print("PRIMER COLUMNA:")
    aux = []
    for numero in numeros:
        cuenta = (norm.cdf((numero-mu)/sigma))
        print(abs((i/cantidad)-(cuenta)))
        aux.append(abs((i/cantidad)-(cuenta)))
        i = i + 1

    i=1
    print("-----------------------")
    print("SEGUNDA COLUMNA: ")
    aux2 = []
    for numero in numeros:
        cuenta = (norm.cdf((numero-mu)/sigma))
        print(abs(((i-1)/cantidad)-(cuenta)))
        aux2.append(abs(((i-1)/cantidad)-(cuenta)))
        i = i + 1    
    print("----------------------------")
    func_maximo(aux, aux2)
    print("---------------------")
    
elif (tipo == 2):
    landa = float(input("seleccione el lambda: "))
    print("Te mostraré la cuenta que queres hacer: ")
    print("PRIMER COLUMNA:")
    aux = []
    for numero in numeros:
        cuenta = abs((i/cantidad) - 1 + math.exp(landa*numero))
        aux.append(abs((i/cantidad) - 1 + math.exp(landa*numero)))
        i = i+1
        print(cuenta)
    
    i = 1
    print("SEGUNDA COLUMNA:")
    aux2 = []
    for numero in numeros:
        cuenta = abs(((i-1)/cantidad) - 1 + math.exp(landa*numero))
        aux2.append(abs(((i-1)/cantidad) - 1 + math.exp(landa*numero)))
        i = i+1
        print(cuenta)
    print("----------------------------")
    func_maximo(aux, aux2)
    print("----------------------------")

elif (tipo == 3):
    cuenta = 0;
    print("----------------------------")
    print("PRIMER COLUMNA: (VALOR - MEDIA / SN) ")
    for numero in numeros:
        cuenta = abs((numero - media)/sn);
        print(cuenta);

    cuenta = 0;
    print("----------------------------")
    print("SEGUNDA COLUMNA: (PHI DE LO ANTERIOR)")
    for numero in numeros:
        cuenta = ((numero - media)/sn);
        cuenta = norm.cdf(cuenta)
        print(cuenta);

    cuenta = 0;
    i= 1;
    print("----------------------------")
    print("TERCERA COLUMNA: ")
    aux4 = []
    for numero in numeros: 
        cuenta = ((numero - media)/sn);
        cuenta = norm.cdf(cuenta)
        cuenta = abs((i/cantidad) - cuenta)
        aux4.append(cuenta)
        print(cuenta);
        i = i+1;
    
    print("----------------------------")
    print("CUARTACOLUMNA: ")
    aux5= []
    for numero in numeros: 
        cuenta = ((numero - media)/sn);
        cuenta = norm.cdf(cuenta)
        cuenta = abs(((i-1)/cantidad) - cuenta)
        aux5.append(cuenta)
        print(cuenta);
        i = i+1;
    print("----------------------------")    
    func_maximo(aux4, aux5)

