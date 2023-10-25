#Se tienen dos listas de N elementos. En la primera se almacenan los nombres de los alumnos 
#mientras que en la segunda, las notas obtenidas por los mismos en un parcial. Mostrar ordenada 
#en forma alfabética, las lista de alumnos aprobados (nota mayor >=60).
n=int(input("Ingresar la cantidad de alumnos: "))
#Creamos listas para nombres y notas
nombres=[None]*n
notas=[None]*n

#Solicitar nombres y notas
for i in range(n):
    nombres[i]=input("Ingresar el nombres del alumno: ")
    notas[i]=int(input(f"ingresar la nota de {nombres[i]}: "))
#Creo una lista de aprobados
aprobados=[]
for i in range(n):
    if notas[i]>=60:
        aprobados.append((nombres[i],notas[i]))
#Ordenar la lista de aprobados alfabeticamente
aprobados.sort()
print("La lista ordenada alfabeticamente con los aprobados: ",aprobados)
