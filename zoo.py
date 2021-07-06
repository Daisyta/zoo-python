from clases.delfin import Delfin
from clases.buho import Buho
from clases.loro import Loro

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_delfin(self,animal):
        self.animals.append(animal)
    def add_buho(self,animal):
        self.animals.append(animal)
    def add_loro(self,animal):
        self.animals.append(animal)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


delfin1 = Delfin( "Willy",25, 10, 30) #nombre,edad,nivelsalud,felicidad,tipo_de_comida,creacion del bjeto delfin1
delfin1.display_info()
buho1 = Buho("Azulito",31, 28, 33)
buho1.display_info() #objeto.metodo
loro1 = Loro("Lorenzo", 48, 23, 43 )
loro1.display_info()

zoo1 = Zoo("Dai Zoo")
zoo1.add_delfin(delfin1) 
zoo1.add_buho(buho1)
zoo1.add_loro(loro1)
zoo1.print_all_info()

zoo2 = Zoo("Kera Zoo")
zoo2.add_delfin(delfin1) 
zoo2.add_buho(buho1)
zoo2.add_loro(loro1)
zoo2.print_all_info()

for animal in zoo1.animals: 
    animal.alimentacion()
#clase.metodo.variable(objeto)


