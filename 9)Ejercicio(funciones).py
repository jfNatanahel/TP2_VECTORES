#Se tienen dos listas de N elementos. En la primera se almacenan los nombres de los alumnos 
#mientras que en la segunda, las notas obtenidas por los mismos en un parcial. Mostrar ordenada 
#en forma alfabética, las lista de alumnos aprobados (nota mayor >=60).
n=int(input("Ingresar la cantidad de alumnos: "))
nombres=[None]*n
for i in range(n):
    nombres[i]=input("Ingresar los nombres de cada alumno: ")
notas=[None]*n
for i in range(n):
    notas[i]=int(input(f"Ingresar las nota de {nombres[i]}: "))
lista_ordenada=nombres.sort()
print(lista_ordenada)
for i in range(n):
    if notas>=60:
        print("APROBADOS")
        print(f"{nombres} tiene una calificacion de{notas}:")
