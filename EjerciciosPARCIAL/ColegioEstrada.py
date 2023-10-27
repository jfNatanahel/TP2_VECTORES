vector_a=[]
vector_b=[]
while True:
    apellido=input("Ingresar el apellido: ")
    dni=str(input("Ingresar el dni: ")) #Dni tiene que estar almacenada como cadena
    vector_a.append((apellido,dni))
    long_nombre=len(apellido)
    dos_caracteres_apellido=apellido[:2]
    tres_ultimos_dni=dni[-3:]
    credencial=long_nombre+dos_caracteres_apellido
    vector_b.append((apellido,dni,credencial))
    respuesta=input("¿Desea continuar? S/N: ").lower()
    if respuesta=="si":
        break
print("El vector A",vector_a)
eliminar_duplicados=list(set(vector_a))
print("El vector A sin duplicados",eliminar_duplicados)
b_eliminar_duplicados=list(set(vector_b))
print("EL vector B",vector_b)
vector_b.sort
print("El vector B ordenado por apellido",vector_b)
