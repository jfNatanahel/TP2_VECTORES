#Dado un vector con N digitos, invertir sus elementos considerando lo siguiente:
#a. Usar un vector auxilar.
#b. Sin usar un vector auxiliar.

#A(ciclo for)
"""n=int(input("Ingresar la cantidad del vector: "))
v=[0]*n

for i in range(n):
    valor=int(input("Ingresar los valores del vector: "))
    v[i]=valor
    
print("El vector original es",v)
vector_auxiliar=[0]*n
for i in range(n):
    vector_auxiliar[i]=v[n-i-1]
print("El vector invertido es",vector_auxiliar)"""

#A(ciclo while)
n=int(input("Ingresar la cantidad de vector/lista: "))
v=[0]*n
i=0
while i<n:
    v[i]=int(input("Ingresar los elementos del vector: "))
    i=i+1
v_auxiliar=[0]*n
i=0
j=n-1
while i<n:
    v_auxiliar[i]=v[j]
    i=i+1
    j=j-1
print("El vector invertido es:",v_auxiliar)

#B(ciclo white)
n=int(input("Ingresar la cantidad de vector/lista: "))
v=[0]*n
i=0
while i<n:
    v[i]=int(input("Ingresar los elementos del vector: "))
    i=i+1
#Sprint("El vector original es:",v[i])
i=n-1
while i>=0:
    print(v[i])
    i=i-1