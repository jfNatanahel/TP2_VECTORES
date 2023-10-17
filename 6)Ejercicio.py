m=int(input("Ingresar el tamaño de la LISTA1: "))
lista1=[None]*m
for i in range(m):
    lista1[i]=input("Ingresar caracteres L1: ")
n=int(input("Ingresar el tamaño de la LISTA2: "))
lista2=[None]*m
for j in range(n):
    lista2[j]=input("Ingersar caracteres L2: ")
for i in range(n):
    if lista1[i]==lista2[j]:
        print(f"Carater {lista2} LISTA 2 se encuentra en la LISTA 1")
    