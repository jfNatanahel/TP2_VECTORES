"""
la clave se genera sustituyendo cada letra del apellido y nombre por el numero de posicion que tiene 
esa letra en el vector MURCIELAGO, en el caso que no estuviera se repite la letra en la clave y no se
considera el epsacio en blanco, ni la coma
"""
murcielago = ["M", "U", "R", "C", "I", "E", "L", "A", "G", "O"]
datos = []

while True:
    nombre_apellido = input("Ingresar el nombre y apellido (separados por una coma) PARA TERMINAR (fin): ")

    if nombre_apellido == "fin":
        break

    #nombre, apellido = nombre_apellido.split(",")  # Separar nombre y apellido

    # Función para generar la contraseña
    password = ""
    for letra in nombre_apellido:
        if letra.upper() in murcielago:
            password += str(murcielago.index(letra.upper()))
        else:
            if letra != "," and letra != " ":  # Ignorar comas y espacios
                password += letra
    
    datos.append((nombre_apellido, password))
datos.sort()
print("El vector con el Nombre y apellido, contraseña es:", datos)