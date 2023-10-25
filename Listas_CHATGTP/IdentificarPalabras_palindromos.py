def es_palindromo(palabra):
    #Eliminar espacios y convertir a minuscula
    palabra=palabra.replace("","").lower()

    #Comprar con la version invertida
    return palabra==palabra[::-1]
def encontrar_palindromos(lista_palabras):
    palindromos=[]
    for palabra in lista_palabras:
        if es_palindromo(palabra):
            palindromos.append(palabra)
    return palindromos
lista_palabra=["reconocer","anilina","python","Radar"]
palindromos= encontrar_palindromos(lista_palabra)
print("Palindromos encontrados")
for palindromo in palindromos:
    print(palindromo)
print("Lista con palindromos es:",palindromos)