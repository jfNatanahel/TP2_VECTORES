#Se tienen dos listas de N elementos. En la primera se almacenan los nombres de los alumnos 
#mientras que en la segunda, las notas obtenidas por los mismos en un parcial. Mostrar ordenada 
#en forma alfabética, las lista de alumnos aprobados (nota mayor >=60).

#preguntas si aprobar
#ir ordenandolos mientras estan aprobandos
n=int(input("Ingresar la cantidad de alumnos"))
alumnos=[None]*n
notas=[None]*n
for i in range(n):
    alumnos[i]=str(input("Ingresar nombre del Alumno (primer letra en MAYUSCULA): "))
    notas[j]=int(input("Ingresar las notas del {alumnos[i]}: "))
    v=notas[i]
    j=i-1 #avanzamos hacia atras
    print(j)
    while j>=0 and notas[j]>v:
        notas[j+1]=notas[j] #mover a la derecha
        j=j-1
    notas[j+1]=v #mover a la izquierda
print(notas)
"""
i=0
for i in range(n):
    if notas<=60:
        i=i+1
    else:
        for k in range(i):

"""
"""n=int(input("Ingresar la cantidad de numeros: "))
x=[None]*n
for i in range (n): 
    x[i]=int(input("Ingresar los elementos: "))
    print(x[i])
   #####ALGORITMO######
    v=x[i]
    j=i-1 #avanzamos hacia atras
    print(j)
    while j>=0 and x[j]>v:
        x[j+1]=x[j] #mover a la derecha
        j=j-1
    x[j+1]=v #mover a la izquierda
print(x)
"""