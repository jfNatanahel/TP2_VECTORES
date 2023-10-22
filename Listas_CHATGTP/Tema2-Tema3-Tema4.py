lista1=[5,9,3]
lista2=["natu","fer","nahi"]
#2.Accede elementos especificos de ambas listas.
#LISTA1
p_e=lista1[0]
s_e=lista1[1]
t_e=lista1[2]
print("1.Elemento LISTA1: ",p_e,"2.Elemento LISTA1: ",s_e,"3.Elemento LISTA1: ",t_e)
#LISTA2
p_e2=lista2[0]
s_e2=lista2[1]
t_e2=lista2[2]
print("1. Elemento LISTA2: ",p_e2,"2.Elemento LISTA2: ",s_e2,"3.Elemento LISTA2: ",t_e2)
#3.Combiar elementos en una tercera lista llamada "lista_combinada"
lista_combinada=lista1+lista2
print("Lista combinada es:",lista_combinada)
#4.Acceder a un rango de elemento en "Lista_combinada" utilizando notacion rebanadas:
sub_lista=lista_combinada[2:4]
print("Rebanada de la lista combinada: ",sub_lista)