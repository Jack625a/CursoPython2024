#Ejercicio practico sobre POO 
#Cajero Automatico
#Paso 1. DEFINIR LA CLASE
class Cajero:
    #Paso 2. CONSTRUCTOR
    def __init__(self,nombre,saldo):
        #Atributos
        self.nombre=nombre
        self.saldo=saldo

    #Paso 3. DEFINIR LOS METODOS O ACCIONES DE LA CLASE (RETIRAR, DEPOSITAR, VER SALDO)
    def retirar(self,cantidad):
        if cantidad>0 and cantidad<=self.saldo:
            self.saldo-=cantidad
            return f"Retiro exitoso - Saldo actual: {self.saldo} Bs"
        else:
            return "Saldo insuficiente!"
    def depositar(self,cantidad):
        if cantidad>0:
            self.saldo+=cantidad
            return f"Deposito exitoso - Saldo Actual: {self.saldo}Bs"
        else:
            return "Error"
        
    def verSaldo(self):
        return f"Saldo Actual: {self.saldo}Bs"
    
#SUBCLASE (HERENCIA)
class CajeroBnb(Cajero):
    def __init__(self,nombre,saldo=0):
        super().__init__(nombre,saldo)
    
    def menuPrincipal(self):
        #Interfaz para el cajero
        while True:
            print("Bienvenido al Cajero")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Saldo")
            print("4. Salir")

            opcion=input("Seleccion la opcion que desea realizar: ")
            if opcion=="1":
                monto=int(input("Ingrese la cantidad a depositar: "))
                print(cuenta1.depositar(monto))
            elif opcion=="2":
                retiro=int(input("Ingrese la cantidad a retirar: "))
                print(cuenta1.retirar(retiro))
            elif opcion=="3":
                print(cuenta1.verSaldo())
            elif opcion=="4":
                print("Gracias por utlizar nuestros servicios...")
                break
            else: 
                print("Error opcion invalida")






#Paso 4. Definir los objetos de la clase
cuenta1=CajeroBnb("Kevin Arroyo")
cuenta1.menuPrincipal()
