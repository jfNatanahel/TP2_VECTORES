n=int(input("Ingresar el tamaño del vector/lista: "))
a=[None]*n
for i in range (n):
    a[i]=int(input("Ingresar los elementos: "))
print(a)
buscado=int(input("Ingresar el numero a buscar: "))
i=0
bandera=0
while i<n and bandera==0:
    if a[i]==buscado:
        print("El numero buscado es: ",buscado,"Se encuentra en la posicion: ",i)
        bandera=1 #corta el ciclo
    else:
        i=i+1
if bandera==0:
    print("No se encontre buscado")
