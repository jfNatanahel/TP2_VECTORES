n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=int(input("Ingersar los elementos del vector: "))
m=int(input("Ingresar un numero para insertar en la lista en el lugar que corresponda: "))
i=0
b=True
while (i<=n-1) and b:
    if m>v[i]: #El valor es mayor al V[i] AUN no encontramos la posicion para ubicarlo.
        i=i+1 #Entonces aumentamos un lugar al "i" verficar con el siguiente numero.
    else: #Encontramos el lugar para ubicar el numero.
        n=n+1 #Aumentamos un lugar en la posicion de nuestro vector.
        for k in range(n-1,i,-1): #Ciclo for para mover los lugares hacia la derecha. Por eso va desde n-1 hasta i.
            v[k]=v[k-1]
        v[i]=m #Se inserta el valor x en la posicion correcta i
        b=False
print("La lista con el valor insertado")
for i in range(n):
    print(v[i])
