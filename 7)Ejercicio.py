#Eliminar elementos repetidos sin utilizar un vector auxiliar.
"""n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=int(input("Ingresar los elementos: "))
i=0
while i<=n-2:
    j=i+1 #J se apunta al 2 elemento de la lista.
    while j<=n-1:
        ####ALGORITMO PARA LOS ELEMENTOS REPETIDOS(sin un vector auxiliar)####
        if v[i]==v[j]: 
            for k in range(j,n-1): #K empieza en J
                v[k]=v[k+1] #Elemento v[K] se sobrescribe con el siguiente elemento. Esto elimina el duplicado.
            n=n-1
        ####ALGORITMO PARA LOS ELEMENTOS REPETIDOS(sin un vector auxiliar)####
        else:
            j=j+1
    i=i+1
for i in range(n):
    print(v[i])"""
#Eliminar elementos repetidos USANDO UN VECTOR AUXILIAR.
""""n = int(input("Ingrese la longitud del vector: "))  # Longitud del vector

vector = []  # Inicializar un vector vacío

for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))  # Pedir cada elemento
    vector.append(elemento)  # Agregar el elemento al vector


vector_sin_repetir = list(set(vector))
# Mostrar el nuevo vector sin elementos repetidos CON FUNCIONES
print("El vector sin elementos repetidos es:", vector_sin_repetir)""" # Eliminar elementos repetidos creando un nuevo vector
"""
list(): La función list() se utiliza para convertir otro tipo de objeto iterable en una lista. 
Puede tomar una cadena, una tupla, un conjunto, un rango u otro objeto iterable y lo convierte en una lista.

set(): La función set() se utiliza para crear un conjunto en Python. Un conjunto es una colección no ordenada
de elementos únicos. Puedes usar set() para eliminar duplicados de una lista u otra secuencia y para realizar
operaciones de conjuntos como intersección, unión y diferencia.
"""
# Mostrar el nuevo vector sin elementos repetidos SIN FUNCIONES
n=int(input("Ingrese la cantidad de elementos de la lista: "))
v=[None]*n
for i in range (n):
    v[i]=int(input("Ingrese los elementos de la lista: "))
    a=[None]*n
    c=0
    for i in range (n):
        b=0
        for j in range (i+1,n,1):
            if v[i]==v[j]:
                b=1
        if b!=1:
            a[c]=v[i]
            c=c+1
print()
for i in range (c):
 print (a[i])

