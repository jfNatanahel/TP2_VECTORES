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
    notas[i]=int(input(f"Ingresar las notas del {alumnos[i]}: "))
#METODO DE ORDENAMIENTO 3)INSERCION:
    copia_nota=notas[i]
    copia_alumnos=alumnos[i]
    j=i-1
    while j>=0 and notas[j]>copia_nota:
        notas[j+1]=notas[j]
        alumnos[j+1]=alumnos[j]
        j=j-1
    notas[j+1]=copia_nota
    alumnos[j+1]=copia_alumnos
    
        
