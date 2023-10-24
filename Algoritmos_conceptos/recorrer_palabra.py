palabra=str(input("Ingrese un nombre: "))
palabra=palabra.upper() #funcion upper: convierte los caracteres a MAYUSCULAS. 
c=len(palabra) #calcula la longitud del nombre (la cantidad de caracteres)
print(palabra.upper(),c)
for i in range(c): #ciclo for recorre cada caracter en la cadena palabra. Desde (0,c) c=longitud del nombre.
    if palabra[i]=="A":
        print("Vocal:",palabra[i],"posicion: ",i)
#¿Para qué  utilizamos la funcion upeer?
#Pasar todos los caracteres a mayusculas y al buscar la letra "A" va a encontrar todas. Ya que algunas pueden estar en mayuscula o minuscula.
