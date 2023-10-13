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
resultado=(((a[i==0]*10+b[j==1])*10+a[i==1])*10+b[j==0])
print("El numero compuesto por el Vector A y Vector B es:",resultado)