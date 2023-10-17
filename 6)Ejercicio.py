m=int(input("Ingresar el tamaño de la LISTA1: "))
lista1=[None]*m
for i in range(m):
    lista1[i]=input("Ingresar caracteres L1: ")
n=int(input("Ingresar el tamaño de la LISTA2: "))
lista2=[None]*n
for j in range(n):
    lista2[j]=input("Ingersar caracteres L2: ")
for i in range(m): #recorrer la primer lista
    for j in range(n): #ciclo anidado, recorrer la segunda lista
        if lista1[i]==lista2[j]:
            print(f"Carater {lista2[j]} LISTA 2 se encuentra en la LISTA 1")
#El programa puede tener un pequeño error, si existen dos elementos iguales se va a imprimir dos veces
#aun asi sigue siendo optimo....