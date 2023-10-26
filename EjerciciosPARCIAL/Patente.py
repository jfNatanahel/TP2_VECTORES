"""
El sistema de patente unica para automotores de la Republica Argentina posee un algortimo que permite
generar el numero de Patente de los propietarios de vehiculos 0 km. El mismo consiste en:
-Solicitar el nombre y apellido y DNI del propietario.
-El numero de patente tiene el siguiente formato: RE DD LLA, donde E y L son letras, D son digitos
numericos y RA corresponde a las iniciales de Republica Argentina.
-Los 3 digitos corresponden a los 3 ultimos digitos del DNI.
-La letra "E" corresponde a la primera letra del apellido y L la ultima letra del apellido.
Dada una lista de datos de propieratorios ingresados en un vector, se solicita:
a)Generar las patentes de los mismo en el mismo vector.
b)Controlar que no se generen elementos repetidos. Si fuese el caso, eliminarlos del vector 
ingresado el inciso a) ingresar la patente repetida en un vector de reclamos con los datos del
propietario, para su verificacion.

"""

sistema_patente=set()
reclamos=[]
republica_argentina="RA"
continuar=True
while continuar:
    apellido=input("Ingresar el apellido: ").upper()
    dni=int(input("Ingresar el dni: "))
    #Generar la patente RE DDD LA
    E=apellido[0] #Primera letra del apellido
    L=apellido[-1] #Ultima letra del apellido
    D=str(dni)[-3:] #Los 3 ultimos digitos del dni
    R=republica_argentina[0]
    A=republica_argentina[:-1]
    patente=str(R+E+D+L+A)
    #Vector resultante
    if patente in sistema_patente:
        reclamos.append((apellido,dni,patente))
    else:
        sistema_patente.add((apellido,dni,patente))
    respuesta=input("Desea continuar? SI/NO: ").lower()
    if respuesta!="si":
        continuar=False
sistema_patente=list(sistema_patente)
print("El vector resultante con sus patentes: ",sistema_patente)
print("El vector de reclamos: ",reclamos)
