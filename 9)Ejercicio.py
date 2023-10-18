#Se tienen dos listas de N elementos. En la primera se almacenan los nombres de los alumnos 
#mientras que en la segunda, las notas obtenidas por los mismos en un parcial. Mostrar ordenada 
#en forma alfabética, las lista de alumnos aprobados (nota mayor >=60).
#1)SOLUCION: METODO DE ORDENAMIENTO INSERCION
#Ingreso las dos listas juntas.
"""n=int(input("Ingresar la cantidad de alumnos: "))
alumnos=[None]*n
notas=[None]*n
for i in range(n):
    alumnos[i]=str(input("Ingresar nombre del Alumno (primer letra en MAYUSCULA): "))
    notas[i]=int(input(f"Ingresar las notas del {alumnos[i]}: "))
#METODO DE ORDENAMIENTO 3)INSERCION:
    copia_nota=notas[i] #copiamos notas para no perder el valor
    copia_alumnos=alumnos[i]
    j=i-1
    while j>=0 and notas[j]>copia_nota:
        notas[j+1]=notas[j]
        alumnos[j+1]=alumnos[j]
        j=j-1
    notas[j+1]=copia_nota
    alumnos[j+1]=copia_alumnos
print("Lista de aprobados")
for i in range(n):
    if notas[i]>=60:
        print(f"El alumno: {alumnos[i]} su nota es: {notas[i]}")"""

#2. SOLUCION: Metodo de burbuja:
n=int(input("Ingresar la cantidad de alumnos: "))
alumnos=[None]*n
notas=[None]*n
for i in range(n):
    alumnos[i]=str(input("Ingresar nombre del Alumno (primer letra en MAYUSCULA): "))
    notas[i]=int(input(f"Ingresar las notas del {alumnos[i]}: "))
i=0
for i in range(n):
    for j in range(1,n-i-1):
        if notas[j]>notas[j+1]:
            aux1=notas[j]
            aux2=alumnos[j]
            notas[j]=notas[j+1]
            alumnos[j]=alumnos[j+1]
            notas[j+1]=aux1
            alumnos[j+1]=aux2
print("Alumnos aprobados")
for i in range(n):
    if notas[i]>=60:
        print(f"El alumno: {alumnos[i]} su nota es: {notas[i]}")



