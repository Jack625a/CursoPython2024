#Diccionarios (clave-valor) {} clave inmutables, valor mutable

docente={
    "Nombre":"Kevin Arroyo",
    "Profesion":"Ingeniero de Sistemas",
    "Celular":69596299
}

print(docente)

#Acceso a valores de las clave
print(docente["Nombre"])
print(docente["Profesion"])

#Modificar valores  
docente["Celular"]=65402398
print(docente)

#Agregado de nuevos pares de clave-valor
docente["Correo"]="k@gmail.com"
print(docente)

#Eliminacion de elementos
del docente["Profesion"]
print(docente)