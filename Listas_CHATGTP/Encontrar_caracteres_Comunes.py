def caracteres_comunes(lista1 , lista2):
    #convierte las listas en conjuntos (sets) para eliminar duplicados.
    set1=set(lista1)
    set2=set(lista2)
    
    #Encuentra la interseccion de los conjuntos para obtener caracteres comunes.
    caracteres_comunes=set1.intersection(set2)
    #Convierte el resultado de nuevo en una lista.
    lista_comun=list(caracteres_comunes)
    return lista_comun
#Ejemplo
lista1=["a","b","c","d","e"]
lista2=["c","d","e","f","g"]
resultado=caracteres_comunes(lista1,lista2)
print("Caracteres comunes:",resultado)