n=int(input("Ingresar la cantidad de vector/lista: "))
v=[0]*n
v_aux=[0]*n
i=0
while i<n:
    v[i]=int(input("Ingresar los elementos del vector: "))
    v[i]=v_aux
    i=i+1
v_nuevo=[0]*n
i=0
j=0
y=0
while i<=n:
    r=v[i]%10
    y=y*10+r
    v[i]=v[i]//10
if v[i]==v_aux[i]:
    v_aux=v_nuevo
    j=j+1
    i=i+1
print("El vector con los numeros capicuas son:",v_nuevo)

