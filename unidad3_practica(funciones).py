#Find regresa el indice correspondiente al primer caracter de la cadena original que coincide con lo que estamos buscando.
#EJEMPLO 1
"""
s="tucuman"
t=s.find("n",2,len(s))
print(t)
"""
#EJEMPLO 2
s= "tucuman"
t= s.find("u",0,len(s))
print(t)
while t>=0 and t<=len(s):
  print ("Las letras u en el texto ",s, " se encuentran en las posiciones:", t)
  t= s.find("u",t+1,len(s))
