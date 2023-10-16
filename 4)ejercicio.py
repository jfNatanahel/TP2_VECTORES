n=int(input("Ingresar palabra en minuscula: "))
v=[None]*n
for i in range(n):
    palabra=str(input("Ingresar una palabra en minuscula: "))
long=len(palabra)
cv=0
cc=0
for i in range(n):
    for i in range(long):
        if palabra[i]=="a" or "e" or "i" or "o" or "u":
            cv=cv+1
        else:
            cc=cc+1
    print("La palabra posicion",i,"Cantidad de vocales: ",cv,"Cantidad de consonantes: ",cc)
