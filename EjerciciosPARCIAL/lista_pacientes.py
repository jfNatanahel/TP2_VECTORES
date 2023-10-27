"""
Se desea elaborar una lista de pacientes que esperen ser atendidos en un consultorio
medico. Para ello inicialmente la lista de espera esta vacia. Realizar lo sigiente:
a)Ingresar un nuevo paciente a la lista de espera.
b)Determinar y mostrar cual es el paciente a ser atendido, atender y eliminarlo de la lista.
c)Atender un paciente con suma urgencia y arreglar y mostrar la lista.
d)Determinar cuantos pacientes faltan para ser atendidos un paciente x.
"""
lista_espera=[]
#continuar=True
while True:
    paciente=input("Ingresar el nombre del paciente(o fin para terminar): ")
    if paciente=="fin":
        break
    lista_espera.append(paciente)
    continuar=True
    while continuar:
        respuesta=input("¿Desea atender a un paciente? S/N: ").lower()
        if respuesta=="si":
            atender=input("Ingrese el nombre del paciente anteder: ")
            if atender in lista_espera:
                lista_espera.remove(atender)
                print(f"El paciente {atender} ha sido atendido y eliminado de la lista")
                continuar=False
        else:
            continuar=False
print("Lista de pacientes en espera:",lista_espera)
x=input("Ingresar el paciente saber cuanto le falta para atender: ")
for i, paciente in enumerate(lista_espera):
    #enumarte para obtener tanto el indice como el valor
    if x==paciente:
        print(f"El paciente {x} le falta por atender: {i}")
        break
else:
    print(f"El paciente {x} no se encuentra en la lista de espera")