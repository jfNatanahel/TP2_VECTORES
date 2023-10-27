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
    lista_espera.append(paciente)
    if paciente=="fin":
        break
    atender=input("Ingresar el paciente que desea atender: ")
    for posicion in paciente:
        if paciente in atender:
            paciente=lista_espera.pop(paciente)
        else:
            print("El paciente no esta en la lista de espera")
print(lista_espera)