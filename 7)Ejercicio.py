n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=int(input("Ingresar los elementos: "))
i=0
while i<=n-2:
    j=i+1 #J se apunta al 2 elemento de la lista.
    while j<=n-1:
        ####ALGORITMO PARA LOS ELEMENTOS REPETIDOS####
        if v[i]==v[j]: 
            for k in range(j,n-1): #K empieza en J
                v[k]=v[k+1] #Elemento v[K] se sobrescribe con el siguiente elemento. Esto elimina el duplicado.
            n=n-1
        ####ALGORITMO PARA LOS ELEMENTOS REPETIDOS####
        else:
            j=j+1
    i=i+1
for i in range(n):
    print(v[i])