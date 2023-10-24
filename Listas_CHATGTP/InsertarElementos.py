#Encontrar la ubicacion correcta para insertar un elemento en una lista.
def encontrar_elemento(mi_lista,elemento):
    index=0
    while index<len(mi_lista) and mi_lista[index]<elemento:
        index+=1
    return index


mi_lista=[]
i=0
while i<3:
    numero=int(input("Ingresar un numero: "))
    i=i+1
    mi_lista.append(numero)
numero_insertar=int(input("Ingresar un numero para insertar en la lista: "))
posicion=int(input("Ingresar la posicion: "))
if posicion>len(mi_lista):
    print("Error el indice supera el rango de la lista ")
else:
    #Encontrar el ubicacion correcta para insertar el numero.
    index=encontrar_elemento(mi_lista,numero_insertar)
    
    #Insertar el numero en la posicion especifica.
    mi_lista.insert(posicion,numero_insertar)
    print("La lista con el elemento insertado:",mi_lista)


