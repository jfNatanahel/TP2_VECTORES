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
    b[j]=int(input("Ingresar los elementos: "))
c=0
for j in range(m): 
    if b[j]==max_valor:
        c=c+1
        x=i
if c==1:
    print("El mayor de la lista A se encuentra en B, en la posicion:",x)
else:
    print("El mayor de la lista A no se encuentra en B")