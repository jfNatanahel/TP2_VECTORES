#1.SELECCION DIRECTA: ordenar de menor a mayor(INEFICIENTE).
#Consiste en encontrar el menor de todos los elementos del vector e intercambiarlo con el que esta en la
#primera posicion. Luego el segundo mas pequeño, y asi sucesivamente hasta ordenarlo toda la lista.
"""n=int(input("Ingresar la cantidad de numeros: "))
x=[None]*n
for i in range(n):
    x[i]=int(input("Ingresar los elementos: "))
##########ALGORITMO SELECTION SHORT##########
for i in range(0,n-1):
    for j in range(i+1,n):
        if x[i]>x[j]:
            aux=x[i] #Guardamos el valor de v[i] para no perderlo.
            x[i]=x[j] #Perdermos el valor de x[i]
            x[j]=aux #El valor de v[j] es igual a el auxiliar era el valor "UBICACIÓN" de v[i]
print(x)"""
#2.BURBUJA (va de 2 en 2):
#Funciona reevisando cada elemento de la lista que va a ser ordenada con el siguiente, intercambiandolos
#de posicion si estan en el orden equivocado. Finaliza cuando encuentre  el menor de todos.
"""n=int(input("Ingresar la cantidad de numeros: "))
x=[None]*n
for i in range (n):
    x[i]=int(input("Ingresar los elementos: "))
print(x)
for i in range(0,n):
    for j in range(0,n-i-1):
        if x[j]>x[j+1]: #Posicion j=0, j[j+1] posicion j=1
            aux=x[j] #Guardar el valor de x[j] posicion 0 para no perderlo.
            x[j]=x[j+1]
            x[j+1]=aux
print(x)"""

#3.INSERCION.
#Este metdo es uno de los mas optimos, ya que a medida que van ingresando los numeros, la lista se va
#ordenando. Como su nombre lo indica, cada vez que se ingresa un numero nuevo, el algoritmo detecta en que
#posicion de la sublista ordenada debe ubicarse. Luego de ello, realiza un corrimiento dejando la ubi
#exacta para insertar el numero en el lugra correspondiente.
n=int(input("Ingresar la cantidad de numeros: "))
x=[None]*n
for i in range (n): 
    x[i]=int(input("Ingresar los elementos: "))
    print(x[i])
    v=x[i]
    j=i-1 #avanzamos hacia atras
    print(j)
    while j>=0 and x[j]>v:
        x[j+1]=x[j] #mover a la derecha
        j=j-1
    x[j+1]=v #mover a la izquierda
print(x)