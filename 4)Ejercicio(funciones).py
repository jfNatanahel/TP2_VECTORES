def contar_vocales_consonantes(palabra):
    contador_vocales=0
    contador_consonantes=0
    posicion_vocales=[] #Creamos una lista para guardar las posiciones.
    for i, letra in enumerate(palabra): #Ciclo for con el i (guardar las posiciones), recorra cada letra.
        if letra.isalpha(): #Verificar si es una letra del alfabeto.
            if letra in "aeiou": #Si letra es == "aeiou"
                contador_vocales+=1
                posicion_vocales.append(i) #Guardamos la posicion de la vocal.
            else:
                contador_consonantes+=1
    return contador_consonantes,contador_vocales,posicion_vocales
n=int(input("Ingresar el tamaño del vector: "))
v=[]
for i in range(n):
    palabra=input("Ingresar las palabras: ")
    palabra.lower()
    v.append(palabra)
for palabra in v: #Recorremos cada palabra del vector.
    vocales, consonantes, posiciones_vocales= contar_vocales_consonantes(palabra)
#Esta asignacion multiple permite que cada uno de estos valores se almacene en una variable separada,
#lo que facilita su posterior uso o impresion. 
    print(f"Palabra:{palabra}")
    print(f"Numero de vocales:{vocales}")
    print(f"Posicion de la vocal:{posiciones_vocales}")
    print(f"Numero de consonantes:{consonantes}")