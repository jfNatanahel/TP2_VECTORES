n=int(input("Ingresar la cantidad de numeros: "))
a=[None]*n
for i in range (n):
    a[i]=int(input("Ingresar los elementos: "))
print(a)
max_valor=a[0]
for i in range(1,n):
    if a[i]>max_valor:
        max_valor=a[i]
print("El numero mayor de la lista a es:",max_valor)
b=0
m=int(input("Ingresar la cantidad de numeros: "))
b=[None]*n
for j in range (m):
    b[i]=int(input("Ingresar los elementos: "))
    if b[i]==max_valor:
        b=b+1
        x=i
if b==1:
    print("El mayor de la lista A se encuentra en B, en la posicion:",x)