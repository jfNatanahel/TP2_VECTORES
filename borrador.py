n=int(input("Dimension A: "))
t=n*2

b=[None]*(t)

for j in range (0,t,2):

    b[j]=str(input(" nombre: "))

    b[j+1]=str(input("Nota: "))

print ("La lista ingresada: ")  

print (b)