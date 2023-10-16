#1.SELECCION DIRECTA
"""
Consiste en encontrar el menor de todos los elementos del vector e intercambiarlo con el que esta en la
primera posicion. Luego el segundo mas pequeño, y asi sucesivamente hasta ordenarlo toda la lista.
"""
n=int(input("Ingresar la cantidad de numeros: "))
x=[None]*n
for i in range(n):
    x[i]=int(input("Ingresar los elementos: "))
for i in range(0,n-1):
    for j in range(i+1,n):
        if x[i]>x[j]:
            aux=x[i]
            x[i]=x[j]
            x[j]=aux
print(x)