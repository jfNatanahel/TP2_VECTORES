"""
La policia de seguridad vial de la provincia efectua operativos en diferentes
puntos de la provincia, estrategicamente ubicados y equipados con dispositivos
moviles de relevamiento en linea.
El procedimiento consiste: revision de documentacion, uso de cinturon de seguridad
, alcoholemia, seguro, y revesa; cargando en el sistema los siguientes datos: 
-Dominio Automotor (N° patente)
-DNI del conductor
-Tipo de infraccion consiste en: ALCO(alcoholemia), CEDU(falta de cedula verde)
CINTU(falta de cinturon de seguridad) REVE (Certificado vigente de Revesa),
SEGU( seguro contra terceros vigente) y CEL(conducir manipulando cel con imprudencia)
Dado un operativo en el acceso a Portezuelo, se solicita:
a) Generar un vector con el relevamiento de infraccion (no se conoce el total)
b) Generar un vector con el ranking de infraccion relevadas, ordenadas de mayor a menor
(cantidad de infracciones agrupadas por tipo de infraccion).
Observaciones:
-Usar solo programacion en Python.
-Puede usar cualquier funcion de Python.
-No se conoce el total de infracciones. Debe consultar al usuario si desea ingresar mas
datos o no para terminar la carga del vector del inciso a)
Metodo de correcion:
- 15 puntos por sintaxis correcta de python.
- 10 punto por sintaxis correcta de vectores.
- 5 puntos por cargar el vector.
- 25 puntos por el inciso a)
- 45 puntos por el inciso b)
"""
procedimiento=[]
continuar=True
alco=0
cedu=0
cintu=0
reve=0
segu=0
cel=0
infracciones_relevadas=[]
while continuar:
    #a)
    n_patente=input("Ingresar el numero de la patente: ")
    dni=int(input("Ingresar el DNI: "))
    tipo_infraccion=input("Ingresar el tipo de infraccion (ALCO),(CEDU),(CINTU),(REVE),(SEGU),CEL: ").lower()
    procedimiento.append((n_patente,dni,tipo_infraccion))
    if tipo_infraccion=="alco":
        alco+=1
    elif tipo_infraccion=="cedu":
        cedu+=1
    elif tipo_infraccion=="cintu":
        cintu+=1
    elif tipo_infraccion=="reve":
        reve+=1
    elif tipo_infraccion=="segu":
        segu+=1
    elif tipo_infraccion=="cel":
        cel+=1
    
    
    respuesta=input("¿Desea continuar?S/N: ").lower()
    if respuesta!="si":
        continuar=False
#b)
infracciones_relevadas.append(("ALCO",alco))
infracciones_relevadas.append(("CEDU",cedu))
infracciones_relevadas.append(("CINTU",cintu))
infracciones_relevadas.append(("REVE",reve))
infracciones_relevadas.append(("SEGU",segu))
infracciones_relevadas.append(("CEL",cel))
mayor_menor=infracciones_relevadas.sort(key=lambda x: x[1],reverse=True)
print("Registro de infracciones:", procedimiento)
print("Ranking de infracciones:")
print(infracciones_relevadas)