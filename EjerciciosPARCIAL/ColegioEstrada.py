#Ejemplos probar el programa
"""
Luna 52488180
Acosta 52547840
Diaz 51995185
Acosta 52547840
"""
vector_a=[]
vector_b=[]
while True:
    apellido=input("Ingresar el apellido: ")
    dni=str(input("Ingresar el dni: ")) #Dni tiene que estar almacenada como cadena
    vector_a.append((apellido,dni))
    long_nombre=len(apellido)
    dos_caracteres_apellido=apellido[:2]
    tres_ultimos_dni=dni[-3:]
    credencial=f"{long_nombre}{dos_caracteres_apellido}{tres_ultimos_dni}"
    vector_b.append((apellido,dni,credencial))
    respuesta=input("¿Desea continuar? S/N: ").lower()
    if respuesta=="no":
        break
print("El vector A",vector_a)
eliminar_duplicados=list(set(vector_a))
print("El vector A sin duplicados",eliminar_duplicados)
b_eliminar_duplicados=list(set(vector_b))
print("EL vector B",b_eliminar_duplicados)
b_eliminar_duplicados.sort()
print("El vector B ordenado por apellido",b_eliminar_duplicados)
