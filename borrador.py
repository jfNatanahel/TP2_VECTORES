#Carga de un vector con el ciclo for
"""n=int(input("Ingresar la cantidad de numeros en el vector: "))
vector=[None]*n #crear el vector
for i in range (n):
    valor=int(input("Ingresar el valor: "))#el usuario ingresar los numeros
    vector[i]=valor
print("El vector ingresado es: ",vector)"""

#Carga de un vector con el ciclo white
"""n = int(input("Ingresar la cantidad de números del vector: "))
vector = [0] * n  # Inicializa un vector de longitud n con valores 0

i = 0  # Inicializa el índice en 0

while i < n:
    vector[i] = int(input("Ingresar el valor: "))
    i = i + 1

# Mostrar el vector
i = 0  # Reinicia el índice en 0

while i < n:
    print(vector[i])
    i = i + 1"""
#
a=[5,3]
b=[7,2]
c=[]
c.append(a,b)
#c.append(b)
print(c)