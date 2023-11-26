"""
Se debe realizar un programa a los fines de gestionar una lsita de espera de turno en una clinica. Cada
vez que llega un paciente nuevo, un enfermero registra su nombre y determina su nivel de urgencia 
(1:critico, 2:normal).. Si es un paciente critico se pone primero en la lista y si es normal se ubica
al ultimo. Con esos datosm el medico va llamando para atencion en el orden de la lista.
a)Ingresar un nuevo paciente normal a la lista de espera.
b)Determinar cual es el paciente a ser atendido, eliminar y arreglar la lista.
c) Si llega un paciente critico, arreglar la lista para que vaya al primer lugar.
d)Determinar cuantos pacientes faltan para atender a un x paciente.....
"""
lista_espera=[]
while True:
    #a)
    paciente=input("Ingresar nombre y apellido (fin para terminar):")
    if paciente=="fin":
        break
    urgencia=int(input("Ingresar nivel de urgencia 1:Critico, 2:Normal(ingresar numeros): "))
    #c)
    if urgencia==1:
        lista_espera.insert(0,paciente)
    else:
        lista_espera.append(paciente)
    #b)
    medico=input("¿Desea atender a un paciente? S/N: ").lower()
    if medico=="si":
        respuesta=input("Ingresar nombre del paciente: ")
        for i in range(lista_espera):
            if respuesta==paciente:
                lista_espera.remove(paciente)
                print(f"El paciente {respuesta} ha sido atendido")
                break
print("Lista de espera",lista_espera)
#d)
x=input("Determinar cuantos pacientes faltan para atender a un x paciente: ")
for i,paciente in enumerate(lista_espera):
    if x==paciente:
        print(f"El paciente {x} le falta {i} para ser atendido")
        break
