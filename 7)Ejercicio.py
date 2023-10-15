n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=int(input("Ingresar los elementos: "))
i=0
while i<=n-2:
    j=i+1
    while j<=n-1:
        if v[i]==v[j]:
            for k in range(j,n-1):
                v[k]=v[k+1]
            n=n-1
        else:
            j=j+1
    i=i+1
for i in range(n):
    v[i]=v[k]
print("El vector es:",v)