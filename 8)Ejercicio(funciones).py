#Dada una lista de N numeros ordenados, insertar M numeros en los lugares que corresponda de tal manera
#que la lista preserve el orden.
def insertar_lugar_corresponda(lista,elemento):
    index=0
    while index<len(lista) and lista[index]<elemento:
        index+=1
    return index
def insertar_numeros_ordenados(lista_original,numeros_insertar):
    for numero in numeros_insertar:
        index=insertar_lugar_corresponda(lista_original,numero)
        lista_original.insert(index,numero)
n=int(input("Ingresar el tamaño de la lista: "))
lista=[None]*n
for i in range(n):
    lista[i]=int(input("Ingresar elementos: "))
numeros_insertar=[int(x) for x in input("Ingresar elementos a insertar (separados por espacios): ").split()]
#.Split(): divida la cadena en palabras, utilizando los espacios como delimitadores.Esto crea una lista de cadenas.
#[int (x) for x in]: Se utiliza una comprension de lista para recorrer cada elemento de la lsita resultante del paso
#anterior (las palabras separadas por espacios) y convertirlas en enteros. Para cada elemento de x.
insertar_numeros_ordenados(lista,numeros_insertar)
print("Lista con el numero insertado y ordenado: ",lista)