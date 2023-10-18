#Dado un listado de alumnos con su correspondiente nota, se solicita ordenar el vector y 
#luego solicitar insertar un nuevo alumno con su nota, sin perder el orden, quiere decir 
#insertando en oden.
#Dado un listado de alumnos con su correspondiente nota, se solicita ordenar el vector
n=int(input("Ingresar la cantidad de alumnos: "))
t=n*2
alumnos_notas=[None]*(t+2)
for i in range (0,t,2):
    alumnos_notas[i]=str(input("Ingresar el alumno: "))
    alumnos_notas[i+1]=int(input("Ingresar la nota del alumno: "))

    copia_alumno=alumnos_notas[i] #alumno
    copia_nota=alumnos_notas[i+1] #nota
    j=i-1
    while (j>=n) and (alumnos_notas[j]>copia_nota):
        alumnos_notas[j+2]=alumnos_notas[j]
        alumnos_notas[j+1]=alumnos_notas[j]
        
        j=j-1
    alumnos_notas[j+2]=copia_alumno
    alumnos_notas[j+1]=copia_nota
    
print("El vector con el Nombre y las Notas es:",alumnos_notas)
