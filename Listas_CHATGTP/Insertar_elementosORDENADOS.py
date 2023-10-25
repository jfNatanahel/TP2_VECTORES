def insertar_elementos_ordenados(lista_a, lista_b):
    for elemento in lista_b:
        index=0
        while index<len(lista_a) and elemento>lista_a[index]:
            index+=1
        lista_a.insert(index,elemento)
lista_a=["a","b","d","j","m"]
lista_b=["c","e","f","g","n"]
insertar_elementos_ordenados(lista_a,lista_b)
print("Lista A despues de la insercion:",lista_a)