def eliminar_palabras_repetidas(lista):
    lista_sin_repetir=[]
    for palabra in lista:
        if palabra not in lista_sin_repetir:
            lista_sin_repetir.append(palabra)
    return lista_sin_repetir
#Ejemplo
mi_lista=["manzana","pera","manzana","uva","pera"]
lista_sin_repetir=eliminar_palabras_repetidas(mi_lista)
print("Lista original:",mi_lista)
print("Lista sin palabras repetidas:",lista_sin_repetir)