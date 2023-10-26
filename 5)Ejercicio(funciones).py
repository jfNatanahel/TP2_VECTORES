def es_palindromo(palabra):
    palabra=palabra.replace("","").lower()
    return palabra==palabra[::-1]
def encontrar_palindromos(lista_palabras):
    palindromos=[]
    for palabra in lista_palabras:
        if es_palindromo(palabra):
            palindromos.append(palabra)
    return palindromos
n=int(input("Ingresar el tamaño del vector: "))
lista_palabras=[]
for i in range(n):
    palabra=input("Ingresar palabra: ")
    lista_palabras.append(palabra)
palabras_palindromas=encontrar_palindromos(lista_palabras)
print("La lista original es:",lista_palabras)
print("La lista con palindromos es:",palabras_palindromas)