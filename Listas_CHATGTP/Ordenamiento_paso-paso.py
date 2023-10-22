def ordenar_seleccion_pasos(lista):
    pasos = []  # Lista para almacenar los resultados parciales
    for i in range(len(lista) - 1, 0, -1):
        indice_del_maximo = 0
        for j in range(1, i + 1):
            if lista[j] > lista[indice_del_maximo]:
                indice_del_maximo = j
        lista[i], lista[indice_del_maximo] = lista[indice_del_maximo], lista[i]
        pasos.append(lista[:])  # Agregar una copia de la lista en este paso

    return pasos  # Devolver la lista de resultados parciales

# Declarar una lista de números
numeros = [64, 25, 12, 22, 11]

# Llamar a la función de ordenamiento y obtener los resultados en pasos
resultados_pasos = ordenar_seleccion_pasos(numeros)

# Mostrar el resultado en cada paso
for i, paso in enumerate(resultados_pasos):
    print(f"Paso {i + 1}: {paso}")

# Mostrar la lista completamente ordenada
print("Lista ordenada de mayor a menor:", resultados_pasos[-1])