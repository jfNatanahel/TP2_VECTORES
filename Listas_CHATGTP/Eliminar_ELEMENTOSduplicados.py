def eliminar_duplicados(lista):
    #Convierte la lista en un conjunto para eliminar duplicados
    conjunto_temporal=set(lista)
    
    #Convierte el conjunto de nuevo en una lista
    lista_sin_duplicados=list(conjunto_temporal)
    return lista_sin_duplicados
#Ejemplo
mi_lista=[1,2,2,3,4,4,5]
lista_sin_duplicados=eliminar_duplicados(mi_lista)
print("Lista origina:",mi_lista)
print("Lista sin duplicados:",lista_sin_duplicados)