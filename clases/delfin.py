from clases.animal import Animal


class Delfin(Animal):
    def __init__(self, nombre, edad, nivelsalud, felicidad):
        super().__init__(nombre, edad, nivelsalud, felicidad)
        super().alimentacion()
        self.alimentacion()
        self.nivelsalud = nivelsalud
        self.felicidad = felicidad

    # que actividad le produce felicidad al loro
    def nadar(self):
        self.felicidad = +60
        print(
            f"El delfin {self.nombre} nada,tiene un nivel de salud : {self.nivelsalud} y un nivel de felicidad {self.felicidad}"
        )
        return self


if __name__ == "__main__":
    try:
        delfin1 = Delfin("Willy",29, 44, 33, 50)
        delfin1.display_info()
        delfin1.alimentacion()
        delfin1.display_info()
        delfin1.nadar()
        delfin1.display_info()

    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Delfin")
