#Dado un vector con N numeros, determinar la cantidad de pares y sumarlos, tambien contar
#contar la cantidad de impares y multiplicarlos, mostrar los resultados.

#Carga del vector
n=int(input("Ingresar el tamaño del vector: "))
v=[0]*n #crear el vector
for i in range (n):
    valor=int(input("Ingresar el valor: "))
    
    v[i]=valor
print("El vector ingresado es: ",v)
c_par=0
suma_par=0
c_impar=0
multiplicacion_impar=1
i=0
while i<n:
    if v[i] %2==0:
        c_par+=1
        suma_par=suma_par+v[i]
    else:
        c_impar=c_impar+1
        multiplicacion_impar=multiplicacion_impar*v[i]
    i=i+1
print("La cantidad de pares es:",c_par,"La suma de pares es:",suma_par)
print("La cantidad de impares es:",c_impar,"La multiplicacion de impares es:",multiplicacion_impar)
#Cuando en tu código haces referencia a v[i], estás accediendo al elemento en la posición i del vector v. 
#En el contexto de tu código, v[i] representa el valor almacenado en la posición i del vector v.