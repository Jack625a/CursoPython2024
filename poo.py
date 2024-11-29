#Programacion Orientada a Objetos
#Clases y Objetos
#Clase class
#Objetos 
#Atributos o parametros
#Metodos o Acciones def
#Encapsulamiento
#Herrencia

class Persona:
    #Constructor
    def __init__(self,nombre,edad,celular):
        #Atributos definidos
        self.nombre=nombre
        self.edad=edad
        self.celular=celular
    
    #Metodo o Accion de la clase
    def comer(self):
        print(self.nombre, "esta comiendo")
    
    def dormir(self):
        print(self.nombre, " esta durmiendo")

    def hablar(self):
        print(self.nombre, " esta hablando")


#Subclase 
class Estudiante(Persona): #HERENCIAS
    def estudiar(self):
        print(self.nombre, "esta estudiando para su examen")

#Objetos
persona1=Persona("Kevin Arroyo",28,65402398)
persona2=Persona("Juan Perez",25,73545132)
persona3=Persona("Ana Gomez",27,7188810)

estudiante1=Estudiante("Raul",25,65401456)

persona1.comer()
persona2.dormir()
persona3.hablar()
estudiante1.estudiar()
estudiante1.comer()



#Herencia
