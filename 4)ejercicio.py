n=int(input("Ingresar tamaño del vector: "))
v=[None]*n
for i in range(n): #iterar a travez de cada palabra.
    palabra=(input("Ingresar una palabra en minuscula: ")) 
#¿Por qué no puse palabra[i]? 
#Ingersamos una palabra a la vez y procesamos cada palabra por separado en un bucle. Estaba interesado en procesar cada palabra individualmente.
    long=len(palabra) #contamos la longitud de la palabra ingresada.
    cant_vocales=0
    cant_consonantes=0
    for i in range(long): #iterar a travez de cada letra en la palabra.
        if palabra[i]=="a" or palabra[i]=="e" or palabra[i]=="i" or palabra[i]=="o" or palabra[i]=="u" :
            cant_vocales+=1
            print(f"Vocal:{palabra[i]} posicion:{i}")

        else:
            cant_consonantes+=1
    print(f"Cantidad de vocales:{cant_vocales}")
    print(f"Cantidad de consonatnes:{cant_consonantes}")