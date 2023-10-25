def insertar_lugar_corresponda(lista,elemento):
    index=0
    if index<len(lista) and lista[index]<elemento:
        index+=1
    return index
def insertar_numeros_ordenados(lista_original,numeros_insertar):
    for numero in numeros_insertar:
        index=insertar_lugar_corresponda(lista_original,numeros_insertar)
        lista_original.insert(index,numeros_insertar)
n=int(input("Ingresar el tamaño de la lista: "))
lista=[None]*n
for i in range(n):
    lista[i]=int(input("Ingresar elementos: "))
numeros_insertar=int(input("Ingresar elementos: "))
insertar_numeros_ordenados(lista,numeros_insertar)
print("Lista con el numero insertado y ordenado: ",lista)