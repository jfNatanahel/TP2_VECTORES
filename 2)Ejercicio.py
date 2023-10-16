#Se tiene una lista de números enteros, ordenar la misma de mayor a menor. Mostrar en cada 
#paso como va quedando el vector. Aplicar el método de Selección y el de la Burbuja.

#1.Metodo de SELECCION;(TRABAJAMOS CON DOS INDICES (I,J))
"""n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=int(input("Ingresar los elementes; "))
for i in range(0,n-1):
    for j in range(i+1,n):
        if v[i]>v[j]:
            aux=v[i]
            v[i]=v[j]
            v[j]=aux
print("El vector va desde menor a mayor es:",v)"""

#2.Metodo burbuja. (TRABAJAMOS CON UN SOLO INDICE AL HACER EL ORDENAMIENTO "J")
n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=int(input("Ingresar los elementes; "))
for i in range(0,n):
    for j in range(0,n-i-1):
        if v[j]>v[j+1]:
            aux=v[j]
            v[j]=v[j+1]
            v[j+1]=aux
print("el vector ordenado de menor a mayor es:",v)