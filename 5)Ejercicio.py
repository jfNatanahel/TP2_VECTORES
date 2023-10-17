n=int(input("Ingresar la cantidad del vector: "))
palabras=[None]*n
for i in range(n):
    palabras=input("Ingresar una palabra en minuscula")
    texto=palabras[::-1] #[::-1] sirve para invertir la palabra.
    if palabras==texto:
        print("Es una palabra palindromas")
    else:
        print("No es una palabra palindromas")