#Crear una lista que represente el texto
texto=[
    "Este es un ejemplo de texto.",
    "Python es un lenguaje de programacion.",
    "Aprende a reemplazar texto en una lista.",
]
#FUNCION PARA MOSTRAR EL TEXTO ACTUAL
def mostrar_texto(texto):
    for linea in texto:
        print(linea)

#FUNCION PARA ENCONTRAR Y REEMPLAZAR TEXTO EN LA LISTA
def encontrar_y_reemplazar(texto,buscar,reemplazar):
    for i in range(len(texto)):
        #Remplazar el texto en la linea acutal si se encuentra
        texto[i]=texto[i].replace(buscar,reemplazar)

#Mostrar texto original.
print("Texto original:")
mostrar_texto(texto)

texto_a_buscar=input("Ingresar el texto a buscar: ")
texto_a_reemplazar=input("Ingresar el texto a reemplazar: ")

#ENCONTRAR Y REEMPLAZAR EL TEXTO INGRESADO
encontrar_y_reemplazar(texto,texto_a_buscar,texto_a_reemplazar)

print("\nTexto despues del reemplaza:")
mostrar_texto(texto)