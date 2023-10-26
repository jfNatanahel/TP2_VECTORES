#Definimos la primera funcion para encontrar la ubicacion correcta del elemento
def ubicacion (lista,elemento):
    index=0 #rastrear sobre la "lista" ubicacion correcta.
    while index<len(lista) and lista[index]<elemento:
        index+=1
    return index
#Definimos la segunda funcion para insertar los elementos en la ubicacion correcta
def insertar_elemento(lista_original,elemento_insertar): 
    #Lista_original: es la lista que esta ordenada.
    #Elemento_insertar es la lista valga la redundancia donde insertaremos los elementos.
    for numero in elemento_insertar:
        #Encontrar su "ubicacion" correcta.
        index=ubicacion(lista_original,numero)
        lista_original.insert(index,numero)
n=int(input("Ingresar el tamaño de lista original: "))
lista_original=[]
for i in range(n):
    numeros=int(input("Ingresar los numeros: "))
    lista_original.append(numeros)
m=int(input("Ingresar el tamaño de los elementos a ingresar: "))
elemento_insertar=[]
for j in range(m):
    numero2=int(input("Ingresar los numeros: "))
    elemento_insertar.append(numero2)
lista_ordenada=insertar_elemento(lista_original,elemento_insertar)
print("Lista con los numeros insertados y ordenados: ",lista_original)