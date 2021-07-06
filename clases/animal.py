class Animal:
    def __init__(self,nombre,edad,nivelsalud,felicidad):
        self.nombre = nombre #estos son atributos de objetos
        self.edad = edad
        self.nivelsalud = nivelsalud
        self.felicidad = felicidad
        
            #el self se usa detro de las clases,no afuera
    def alimentacion(self): #es un metodo
        self.nivelsalud =+10
        self.felicidad =+10 
        print(f"El animal {self.nombre} se ha alimentado")
        return self

    def __str__(self): #este es un metodo str,es el comportamiwnto que tienen los objetos,a los metodos se les asocia con una clase
        return (f" El animal {self.nombre}, de : {self.edad} años, tiene un nivel de salud {self.nivelsalud} y felicidad {self.felicidad}")

    def display_info(self):   
        print(f" El animal {self.nombre}, de : {self.edad} años, tiene un nivel de salud {self.nivelsalud} y felicidad {self.felicidad}")
        return self

if __name__ == '__main__':
    try:
        animal1=Animal( "Kitu", 25, 10, 50)
        print(animal1)
        animal1.alimentacion()
        
        animal1.display_info()
    except Exception as e:
        print("Error", e)
        print("Hay un error en la clase animal")

# le puedo dar valore definidos e la linea 24 ,los niveles de edad,nivel salud felicidad. 
# si no le doy los valores definidos en la linea 24, se le puede dar en el self 10 y 11 valores definidos de self