#1.UNION
n=int(input("Ingresar tamaño lista 1: "))
a=[None]*n
for i in range(n):
    a[i]=int(input("Ingresar los elementos L1: "))
m=int(input("Ingresar tamaño lista 2: "))
b=[None]*m
for j in range(m):
    b[j]=int(input("Ingresar los elementos L2: "))
c=[]
for i in range(n):#primer vector
    existe=0
    for j in range(m):#segundo vector
        if a[i]==b[j]:
            existe=1
    if existe==0:
        c.append(a[i])
for j in range(m):
    existe=0
    for i in range(n):
        if b[j]==a[i]:
            existe=1
    if existe==0:
        c.append(b[j])
print("Vector a:")
print(a)
print("Vector b:")
print(b)
print("Vector c:")
print(c)
#conjuntos1f NO FUNCIONA