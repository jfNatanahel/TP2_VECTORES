palabra=str(input("Ingrese un nombre: "))
palabra=palabra.upper()
c=len(palabra)
print(palabra.upper(),c)
for i in range(c):
    if palabra[i]=="A":
        print("Vocal:",palabra[i],"posicion: ",i)