def ordenar_selecccion_menor_mayor(lista):
    for i in range(len(lista)-1,0,-1):
        indice_del_maximo=0
        for j in range(1,i+1):
            if lista[j]>lista[indice_del_maximo]:
                indice_del_maximo=j
        lista[i],lista[indice_del_maximo]=lista[indice_del_maximo],lista[i]
# Declarar una lista de números
numeros = [64, 25, 12, 22, 11]

# Ordenar la lista de mayor a menor utilizando el método de selección
ordenar_selecccion_menor_mayor(numeros)

# Mostrar la lista ordenada
print("Lista ordenada de menor a mayor:", numeros)