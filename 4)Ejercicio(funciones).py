def contar_vocales_consonantes(palabra):
    contador_vocales=0
    contador_consonantes=0
    posicion_vocales=[]
    for i, letra in enumerate(palabra):
        if letra.isalpha():
            if letra in "aeiou":
                contador_vocales+=1
                posicion_vocales.append(i)
            else:
                contador_consonantes+=1
    return contador_consonantes,contador_vocales,posicion_vocales
n=int(input("Ingresar el tamaño del vector: "))
v=[]
for i in range(n):
    palabra=input("Ingresar las palabras: ")
    palabra.lower()
    v.append(palabra)
for palabra in v:
    vocales, consonantes, posiciones_vocales= contar_vocales_consonantes(palabra)
    print(f"Palabra:{palabra}")
    print(f"Numero de vocales:{vocales}")
    print(f"Posicion de la vocal:{posiciones_vocales}")
    print(f"Numero de consonantes:{consonantes}")