from clases.animal import Animal


class Loro(Animal):
    def __init__(self, nombre,edad,nivelsalud,felicidad):
        super().__init__(nombre,edad,nivelsalud,felicidad)
        super().alimentacion()
        self.alimentacion()
        self.nivelsalud = nivelsalud
        self.felicidad = felicidad


#que actividad le produce felicidad al loro
    def cacarear(self):
        self.felicidad =+35
        print(f"El loro {self.nombre} cacarea,tiene un nivel de salud : {self.nivelsalud} y un nivel de felicidad {self.felicidad}")
        return self

if __name__ == '__main__':
    try:
        loro1 = Loro( "Lorenzo", 33, 20, 30, 50 )
        loro1.display_info()
        loro1.alimentacion()
        loro1.display_info()
        loro1.cacarear()
        loro1.display_info()
        
    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Loro")
