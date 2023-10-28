"""
Dada una serie de fechas (dia/mes/año), la cantidad de pasajeros transportados por una linea aerea
en esa fecha y el monto recaudado en dolares, realizar un programa:
a)Determinar y mostrar las fechas hasta superar los 2000 pasajeros (puede no haber ninguno), y que 
monto se recaudo. Luego contabilizar hasta el final de la lista.
b)Emitir un listado de las fechas, en el que el monto recaudado supero los 250.000 dolares (puede
no haber ninguno). Luego continuar contabilizando hasta el final de la lista.
"""
# Inicializamos las variables
fechas_pasajeros = []
monto_recaudado = 0
fechas_superaron_2000_pasajeros = []
monto_total_superado_250000 = 0

# Función para procesar una fecha
def procesar_fecha(fecha, pasajeros, monto):
    fechas_pasajeros.append((fecha, pasajeros))
    monto_recaudado += monto

    if pasajeros > 2000:
        fechas_superaron_2000_pasajeros.append((fecha, monto))
    
    if monto > 250000:
        print(f"Fecha: {fecha}, Monto recaudado: {monto}")
        monto_total_superado_250000 += monto

# Entrada de datos (puedes ajustar esta parte según cómo tengas los datos)
datos = [
    ("01/08/2021", 400, 40000),
    ("05/08/2021", 350, 35000),
    ("07/08/2021", 703, 70300),
    ("09/08/2021", 600, 60000),
    ("30/08/2021", 300, 30000),
    ("01/09/2021", 250, 25000),
    ("05/09/2021", 100, 10000),
    ("15/09/2021", 700, 70000),
    ("17/09/2021", 700, 70000),
    ("20/09/2021", 255, 125500),
    ("25/09/2021", 200, 20000),
    # Agregar más datos aquí
]

# Procesar los datos
for fecha, pasajeros, monto in datos:
    procesar_fecha(fecha, pasajeros, monto)

# Resultados
print("\nFechas con más de 2000 pasajeros:")
for fecha, monto in fechas_superaron_2000_pasajeros:
    print(f"Fecha: {fecha}, Monto recaudado: {monto}")

print("\nMonto total recaudado:", monto_recaudado)

print("\nMonto total superado 250,000:", monto_total_superado_250000)
