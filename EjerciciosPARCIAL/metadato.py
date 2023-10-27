"""Los metadatos son muy importantes en una investigacion forense. Particularmente los
metadatos de un archivo son un grupo de datos que describen sus caracteristicas,tales
como fecha de creacion o modificacion, tamaño, programa y usuario que lo genere entre otros.
Un perito informatico recibe un metadato correspondiente a archivos. Este metadato es 
un string de longitud fija (45 caracteres), que contiene la siguiente informacion separada
por comas.
Formato: (fecha(8), tamaño del byte(8), nombre del programa(15), nombre del usuario(10))
En base a ello:
a) Solicitar el metadato y validar su longitud fija. Si no es correcta, mostrar un error y 
volver a solicitarlo hasta que se verifique.
b)Generar un vector con los metadatos (sin tomar en cuenta las comas)
c)Ordenar el vector generado por el tamaño (menor a mayor) sin alterar el vector original.
Ejemplo:"20231001,00000145,Microsoft Word, cpacheco "
"""
#
v_generado=[]
while True:
    continuar=True
    while continuar:
        metadato=input("45 caracteres (con las ,): ")
        if len(metadato) != 45 or metadato.count(",") != 3:
            print("Error. El metadato debe tener 45 caracteres y contener tres comas.")
        continue
    metadato=metadato.replace("","")
    fecha = metadato[0:8]
    tamaño_byte = metadato[9:17]
    nombre_programa = metadato[18:33]
    nombre_usuario = metadato[34:]
    v_generado.append((fecha,tamaño_byte,nombre_programa,nombre_usuario))
    respuesta=input("¿Desea continuar? S/N: ").lower()
    if respuesta=="no":
        break
print("Vector generado:",v_generado)
v_generado.sort(key=lambda x: x[1])
print("Vector ordenado de menor a mayor",v_generado)
