n = int(input("Ingresar la cantidad de números del vector: "))
a = [0] * n  # Inicializa un vector de longitud n con valores 0
i = 0  # Inicializa el índice en 0

while i < n:
    a[i] = int(input("Ingresar el valor: "))
    i = i + 1
###
b1 = int(input("Ingresar la cantidad de números del vector: "))
b = [0] * b1  # Inicializa un vector de longitud n con valores 0
j = 0  # Inicializa el índice en 0

while j < b1:
    b[j] = int(input("Ingresar el valor: "))
    j = j + 1
resultado=(((a[0]*10+b[1])*10+a[1])*10+b[0])
resultado2=str(a[0])+str(b[1])+str(a[1])+str(b[0]) #los paso a cadena de caracteres y puedo realizar la concatenacion.


print("1.El numero compuesto por el Vector A y Vector B es:",resultado)
print("2.El numero compuesto por el Vector A y Vector B es:",resultado2)