#Ejercicio
"""
Se debe realizar un programa en el cual inicialemnte se deben cargar dos vectores, uno con el DNI de
los clientes del banco y el segundo con el saldo disponible de la caja de ahorro (ambos vectores en
la misma posicion deben tener la informacion del mismo cliente).
Luego se debe ingresar el DNI de un cliente y el saldo a extraer(repetir mientras el dni cargado sea
distinto a cero).
1. Calcular si el saldo del cliente es suficiente:
a)Si el saldo es suficiente restar el monto a extraer, actualizando el valor del vector. Mostrar un 
mensaje de "operacion exitosa" y mostrar el nuevo saldo.
b)si el saldo no es suficiente mostrar el mensaje "Saldo insuficiente" y mostrar el saldo actual.
2. Se debe llevar en una variable el monto total extraido satisfactoriamente, y en otra el monto que
no se pudo extraer.
3.Cuando se ingresa el DNI en cero(fin de la operatoria) se debe informar los montos totales extraidos
y los montos totales que no se pudieron extraer, como asi tambien el saldo final de cada uno de los 
clientes ordenados de menor a mayor de acuerdo al DNI
"""
#Ejemplo
"""
Vector de Dni y en paralelo el otro Vector Saldos:
30344852 15.600
10451647 658.25
27985365 185.00000
47215369 67.33969
14653283 24.50000

"""
dni_clientes_banco=[]
saldo_disponible=[]
total_no_extraido=0
total_extraido=0
while True:
    clientes=int(input("Ingresar dni de los clientes(fin para terminar)"))
    if clientes=="fin":
        break
    caja_ahorro=float(input("Ingresar saldo disponible: "))
    dni_clientes_banco.append(clientes)
    saldo_disponible.append
while True:
    dni_cliente=int(input("Ingresar el dni del cliente(0 para terminar): "))
    if dni_cliente==0:
        break
    saldo_extraer=float(input(f"Ingresar el saldo a extrar del dni {dni_cliente}: "))
#primero buscamos la posicion del Dni.
    posicion=dni_clientes_banco.index(dni_cliente)
#Una vez encontrado buscamos el saldo disponible.
    saldo=saldo_disponible[posicion]
    if saldo < saldo_extraer:
        total_no_extraido+=saldo_extraer
        print("Saldo insuficiente")
        print("Saldo actual:",saldo)
