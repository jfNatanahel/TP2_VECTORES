#Dada una lista de tamaño n, de numeros enteros, se desa modificar cada numero de la lista, eliminando 
#del numero los digitos mayores e iguales a 5.
n=int(input("Ingresar el tamaño del vector: "))
a=[None]*n
for i in range(n):
    a[i]=int(input("Ingresar los elementos: "))
print(a)
b=0
for i in range(n):#iterar en cada numero del vector o en cada indice.
    p=0
    num=0
    x=a[i]
    while x>0:
        d=d%10
        print(d)
        if d<5:
            num=num+(d*10**p) #formula para borrar el numero que no es mayor a 5. Todos los numeros < se van a ir armando.
            p=p+1
            b=1
        x=x//10
    if b==1:
        a[i]=num
print("la nueva lsita es:")
print(a)
