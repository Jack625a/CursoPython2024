#Variables 
#Tipos de datos
#1. Numerericos
numero=25
numero2=3.14 
suma=numero+numero2
print(suma)
#2. Textos "" ''
nombre="Kevin Arroyo"
curso='Programación'

print("Docente:",nombre, "Curso:", curso)
#3. Booleanos True False
encender=True
print(encender)

#4. Estructuras 
#LISTAS, TUPLAS Y DICCIONARIOS
#4.1 Listas (MUTABLES) 
#Operaciones de las listas
#Agregado de elementos - Ordenado de Elementos, Eliminacion de Elementos, Longitud de Elementos
#Las listas en Python se crearn con []
colores=["Rojo","Verde","Amarillo","Cafe","Azul","Rosado","Anaranjado","Lila"]

#Mostrar el elemento 1
print(colores[0])
#Mostrar el elemento 3
print(colores[2])
#Mostar el ultimo elemento de la lista [-1]
print(colores[-1])

#Actualizacion de elementos (Actualizar el color Cafe de la lista de colores Nuevo Color "Mostaza")
colores[3]="Mostaza"
print(colores)
#Actualizar el ultimpo color de la lista a color "Negro"
colores[-1]="Negro"
print(colores)
#Agregar elementos en la lista (append)
colores.append("Blanco")
print(colores)
#Insertar varios elementos a la lista (insert)

#Insertar el color Plomo a lado del color verde
colores.insert(2,"Plomo")
print(colores)
colores.insert(0,"Cafe")
print(colores)
#Eliminacion de un elemento (Remove)
colores.remove("Mostaza")
print(colores)

#Longitud de una lista (len)
print(len(colores))

#Ordenado de elementos de una lista (sort) (sorted)
#Metodo Sort - Ordenar los elemento de forma ascendente (la lista original)
numeros=[4,5,1,9,8,11,55,64,3,12,63,96]
print("Lista de numeros original ",numeros)
numeros.sort(reverse=True)
print("Lista de numeros orginal ordenado ",numeros)

numeros.append(85)
print(numeros)

#Metodo Sorted - Ordenar los elementos de forma ascendente de la lista (Crea una nueva lista)
numeros2=[7,8,45,1,3,9,87,12,36,115,88,96,1723]
numerosOrdenados=sorted(numeros2,reverse=True)
print("LISTA DE NUMEROS ORDENADOS: ",numerosOrdenados)
print("LISTA DE NUMERO ORIGINALES: ",numeros2)


#Ordenado de elementos ASCENDENTE - DESCENDENTE

#Ordenar los colores (Ordenado de forma alfabeticamente)
colores.sort()#Ordenado de colores de forma ascendete
print(colores)
colores.sort(reverse=True)
print(colores)
