n=int(input("Ingresar la cantidad de vector/lista: "))
v=[0]*n
i=0
while i<n:
    v[i]=int(input("Ingresar los elementos del vector: "))
    i=i+1
#Vector para almacenar los numeros capicuas
v_nuevo=[] #vacio
i=0
while i<n:
    num=v[i] #el numero en la posicion i la guardo en una variable num.
    num_str=str(num)#convierte el numero en una cadena de caracteres. 
    if num_str==num_str[::-1]: #Comprobar si el numero es capicua
                            #[::-1] -> para obtener una version invertida de la cadena. Ej:112 -> 211
        v_nuevo.append(num)
    i=i+1
print("El vector con los numeros capicuas es: ",v_nuevo)

