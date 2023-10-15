g=int(input("ingresar el grado del polinomio: "))
x=int(input("Ingresar el valor de x: "))
v=[None]*(g+1) #se inicializa con n+1 elementos, se utiliza para almacenar los coeficientes del polinomio.
for i in range(g+1):
    v[i]=int(input("Ingresar el valor de los coeficientes: "))
c=g #c es para rastrear el exponente de x en cada termino del polinomio
suma=0 #realizar la suma y el resultado del polinomio.
for i in range(g+1):
    y=v[i]*(x**c) #Coeficiente . el valor de x (elevado) al numero del grado del polinomio ingresado.
    suma=suma+y
    c=c-1
print(suma)