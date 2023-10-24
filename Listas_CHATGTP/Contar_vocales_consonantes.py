def contar_vocales_consonantes(lista_palabras):
    conteo_total_consonantes=0
    conteo_total_vocales=0
    for palabra in lista_palabras: #Recorre cada palabra en la lista.
        vocales=0
        consonantes=0
        for letra in palabra: #Recorrer cada letra en la palabra actual.
            if letra.isalpha(): #Meotod .isalpha() es para verificar si la letra es una letra del alfabeto.
                if letra.lower() in "aeiou": #Verificamos si es una vocal. Con el metodo lower pasando a minuscula.
                    vocales+=1
                else:
                    consonantes+=1
        print(f"palabra:{palabra},vocal:{vocales},consonantes:{consonantes}")
    conteo_total_consonantes+=consonantes
    conteo_total_vocales+=vocales
    print(f"CONTEO TOTAL - Vocales:{conteo_total_vocales},consonantes:{conteo_total_consonantes}")
palabras=["hola","python","programacion"]
contar_vocales_consonantes(palabras)