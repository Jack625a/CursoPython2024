#Funcion (def ())
#Sintaxis
#def nombre_funcion(parametros):
    #Codigo 
 #   return opcion

def bienvenida():
    print("Bienvenido al curso")

#Llamar a una funcion 
bienvenida()

#Funciones con parametros
def bienvenida2(nombre):
    print(f" Hola {nombre} bienvenido al curso")

#Llamar a la funcion
bienvenida2("Kevin Arroyo")

#Funciones con valores de retorno (return)
def sumar(numero1,numero2):
    return numero1+numero2



def restar(a,b):
    return a-b

def multiplicar(x,y):
    return x*y

#Llamado a la funcion de retorno
resultadoSuma=sumar(7,3)
resultadoResta=restar(7,3)
resultadoMultiplicacion=multiplicar(7,3)

print("la suma es: ",resultadoSuma, " La resta es: ",resultadoResta, " La multiplicacion es: ",resultadoMultiplicacion)

#Valores de entrada (input): Almacena los datos por teclad como cadena de caracteres int float

numero1=int(input("INGRESE UN NUMERO: "))
numero2=int(input("Ingrese un numero: "))

print(f"La suma de {numero1}+{numero2}=",sumar(numero1,numero2))

#Funciones con parametros por defecto
def bienvenida3(nombre="Kevin Arroyo"):
    print(f"Hola bienvenido {nombre}")

bienvenida3("Jose")

#Funciones con multiples retornos
def calculos(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return suma, resta, multiplicacion, division 

#Llamar a la funcion con multiples retornos
calculos_suma, calculos_resta, calculos_multiplicacion, calculos_division=calculos(15,3)

print("La suma es:",calculos_suma)
print("La resta es: ",calculos_resta)
print("La multiplicacion es: ",calculos_multiplicacion)
print("La division es: "),calculos_division

#Funciones lambda (Anonimas)
sumar=lambda a,b:a+b
print(sumar(8,5))