#Condicionales
# if condicion
# else
# elif

#Ejercicios
numero=150
numero2=180
#si el numero es mayor a numero2 mostrar el numero es mayor que el numero numero 2
if numero>numero2:
    print(numero," es mayor que ",numero2)
else:
    print(numero," es menor que ",numero2)
#Evaluar las notas de los estudiantes
#si la nota es mayor o igual a 90 mostrar Excelente
#Si la nota es mayor o igual a 51 mostrar Aprobado
#Si la nota es menor a 51 mostrar Reprobado
nota=10
if nota>=90:
    print("Excelente")
elif nota>=51:
    print("Aprobado")
else:
    print("Reprobado")

#Condicionales con operadores Logicos (and, or, not)
numero3=101
if numero3>1 and numero3<100:
    print(numero3, "esta entre el rango de 1 y 100")

