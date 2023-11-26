#Dado un vector de K elementos que contiene palabras, realizar un programa para eliminar las palabras
#repetidas. El vector resultante debe ser un vector de m elemenntos no repetidos.
"""n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=input("Ingresar palabra")
########ALGORITMO ELIMINAR ELEMENTOS REPETIDOS########"""
"""¿CUAL ES LA IDEA DE LOS DOS CICLOS WHILE?
La idea es que i representa el índice del elemento actual que estamos comparando, y j se utiliza
para rastrear el índice del siguiente elemento en el vector que queremos comparar con el elemento
en la posición i. Esto asegura que estemos comparando cada elemento con los elementos posteriores 
en el vector para detectar duplicados."""
"""i=0
while i<=n-2: #1er ciclo para "i"
#¿Por qué i<=n-2?
#primer elemento hasta el penúltimo elemento (hasta n-2).Esto se hace para seleccionar
#un elemento en la posición i para compararlo con los elementos subsiguientes en el bucle interno.
    j=i+1 #J toma el proximo valor de i entonces compara v[0]"i" con v[1]"j"
    while j<=n-1:
        if v[i]==v[j]:
            for k in range(j,n-1):
                v[k]=v[k+1]
            n=n-1 #IMPORTANTE restarle uno al vector.
        else:
            j=j+1
    i=i+1
print("Lista sin repetidos:")
for i in range(n):
    print(v[i])
print("Vector resultante es:",v[:n])"""
#RESOLVIENDO EL PROBLEMA CON FUNCIONES
