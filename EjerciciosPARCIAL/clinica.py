lista_espera=[]
while True:
    paciente=input("Ingresar nombre y apellido (fin para terminar):")
    if paciente=="fin":
        break
    urgencia=int(input("Ingresar nivel de urgencia 1:Critico, 2:Normal(ingresar numeros): "))
    if urgencia==1:
        lista_espera.insert(0,paciente)
    else:
        lista_espera.append(paciente)
    medico=input("¿Desea atender a un paciente? S/N: ").lower()
    if medico=="si":
        respuesta=input("Ingresar nombre del paciente: ")
        for i in range(lista_espera):
            if respuesta==paciente:
                lista_espera.remove(paciente)
                print(f"El paciente {respuesta} ha sido atendido")
                break
print("Lista de espera",lista_espera)
x=input("Determinar cuantos pacientes faltan para atender a un x paciente: ")
for i,paciente in enumerate(lista_espera):
    if x==paciente:
        print(f"El paciente {x} le falta {i} para ser atendido")
        break