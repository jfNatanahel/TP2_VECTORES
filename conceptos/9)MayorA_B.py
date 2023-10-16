n=int(input("Ingresar la cantidad de numeros: "))
a=[None]*n
for i in range (n):
    a[i]=int(input("Ingresar los elementos: "))
print(a)
for i in range(n):
    for j in range(n,-i-1):
        if a[j]<a[j+1]: #Buscar el mayor de la lista y colocalo en a[0]
            aux=a[j]
            a[j]=a[j+1]
            a[j+1]=aux
print("El mayor valor de la lista A es:",a[0])