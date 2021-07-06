from clases.animal import Animal

class Buho(Animal):
    def __init__(self, nombre,edad,nivelsalud,felicidad):
        super().__init__(nombre,edad,nivelsalud,felicidad)
        super().alimentacion()
        self.alimentacion()
        self.nivelsalud = nivelsalud
        self.felicidad = felicidad
        

#que actividad le produce felicidad al loro
    def ulular(self):
        self.felicidad =+63
        print(f"El buho {self.nombre} ululea,tiene un nivel de salud : {self.nivelsalud} y un nivel de felicidad {self.felicidad}")
        return self

if __name__ == "__main__":
    try:
        buho1 = Buho("Azulito", 22, 65, 21, 50)
        buho1.display_info()
        buho1.alimentacion()
        buho1.display_info()
        buho1.ulular()
        buho1.display_info()

    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Delfin")
