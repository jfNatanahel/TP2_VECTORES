#Encontrar la ubicacion correcta para insertar un elemento en una lista.
def encontrar_elemento(mi_lista,elemento):
    index=0
    while index<len(mi_lista) and mi_lista[index]<elemento:
        index+=1
    return index


mi_lista=[]
i=0
while i<=3:
    mi_lista[i]=int(input("Ingresar un numero: "))
    i=i+1
    mi_lista.append([i])
numero_insertar=int(input("Ingresar un numero para insertar en la lista: "))
posicion=int(input("Ingresar la posicion: "))
if posicion>len(mi_lista):
    print("Error el indice supera el rango de la lista ")
def insertar_elemento(mi_lista,elemento):
    index=encontrar_elemento(mi_lista,elemento)
    mi_lista.insert(posicion,numero_insertar)


