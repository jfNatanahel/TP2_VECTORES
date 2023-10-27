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
dni=[]
saldo_disponible=[]
while True:
    dni2=int(input("Ingresar dni: "))
    dni.append(dni2)
    saldo=float(input("Ingresar el saldo: "))
    saldo_disponible.append(saldo)
    respuesta=input("¿Desea continuar?S/N: ").lower()
    if respuesta=="no":
        break
continuar=True
while continuar:
    print("CLIENTE")
    dni_cliente=int(input("Ingresar dni del cliente: "))
    if dni_cliente==0:
        continuar=False
    else:
        saldo_extraer=float(input("Ingresar el saldo a extraer: "))
        total_extraido=0
        total_No_extraido=0
        for i in range(dni):
            if dni_cliente==dni[i]:
                for j in range(saldo_disponible):
                    if saldo_extraer==saldo_disponible[j]:
                        if saldo_extraer>=saldo_disponible:
                            total_No_extraido=total_extraido+saldo_extraer
                            print("Saldo insuficiente")
                            print("Saldo actual",saldo_disponible[j])
                        else:
                            saldo=saldo_disponible[j]-saldo_extraer
                            saldo_disponible.replace(saldo_disponible[j],saldo)
                            print("Operacion exitosa")
                            print("Saldo:",saldo)
print("Montos totales extraidos",total_extraido)
print("Montos totales No extraidos",total_No_extraido)
saldo_disponible_ordenado,dni_ordenado=zip(*sorted(zip(dni,saldo_disponible), key=lambda x: x[1]))
print("Ordenado de menor a mayor")
print("Dni ordenado",dni_ordenado)
print("Saldo disponible",saldo_disponible_ordenado)