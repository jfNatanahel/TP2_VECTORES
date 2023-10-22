def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Declarar una lista de números
numeros = [64, 25, 12, 22, 11]

# Ordenar la lista de mayor a menor
ordenar_burbuja(numeros)

# Mostrar la lista ordenada
print("Lista ordenada de mayor a menor:", numeros)
