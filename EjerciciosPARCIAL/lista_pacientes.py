"""
Se desea elaborar una lista de pacientes que esperen ser atendidos en un consultorio
medico. Para ello inicialmente la lista de espera esta vacia. Realizar lo sigiente:
a)Ingresar un nuevo paciente a la lista de espera.
b)Determinar y mostrar cual es el paciente a ser atendido, atender y eliminarlo de la lista.
c)Atender un paciente con suma urgencia y arreglar y mostrar la lista.
d)Determinar cuantos pacientes faltan para ser atendidos un paciente x.
"""
lista_espera=[]
continuar=True
while continuar:
    paciente=input("Ingresar el nombre del paciente: ")
    lista_espera.append(paciente)
    doctor=True
    while doctor:
        recepcion=input("Desea atender a un paciente? Si: Ingresar nombre: ").lower()
        if recepcion=="si":
            if recepcion in lista_espera:
                lista_espera.remove(recepcion)
                print(f"El paciente {recepcion} ha sido atendido")
            else:
                print(f"el paciente{recepcion} no se encuentra en la lista de espera")
        else:
            doctor=False
    respuesta=input("¿Desea continuar?S/N: ").lower()
    if respuesta!="si":
        continuar=False
print("Lista de pacientes",lista_espera)
x=input("Ingresar el paciente a determinar cuanto falta para ser atendido: ")
if x in lista_espera:
    index=lista_espera.index(x)
    print(f"El paciente {x} falta ser atendido en la posicion {index}")
