def encontrar_ubicacion(mi_lista,elemento):
    index=0
    while index<len(mi_lista) and mi_lista[index]<=elemento:
        index=index+1
    return index
def insertar_numeros_ordenados (lista_original,numeros_insertar):
    for numero in numeros_insertar:
        index=encontrar_ubicacion(lista_original,numero)
        lista_original.insert(index,numero)
#Ejemplo
mi_lista=[1,3,5,6,7,9]
numeros_insertar=[2,4,6,8]
insertar_numeros_ordenados(mi_lista,numeros_insertar)
print("Lista con numeros insertar y ordenados: ",mi_lista)