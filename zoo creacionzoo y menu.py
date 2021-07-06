from delfin import Delfin
from loro import Loro


print(f"\n\nBienvenido al Zoologico")
listaZoo=[]
while True:
    print(f"\nMenu de opciones")
    print(f"Seleccione una opcion:  \n1.Crear un Zoo  \n2.Registrar un Buho  \n3.Registrar un loro \n4.Registrar un delfin \n5.Mostrar animales del Zoo \n0.Salir")
    n = int(input("Ingresa tu opcion: "))
    
    if n == 1:
        nombre = input("\nNombre del Zoo: ")
        zoo = Zoo(nombre)
        print("\nCreaste el zoologico: ", nombre)
        listaZoo.append(zoo)

    if n == 2:
        nombre = input("\nNombre del buho: ")
        edad = int(input("Edad: "))
        peso = int(input("Peso: "))
        buho = buho(0, nombre, edad, 0, 0, peso)
        buho.ulular()
        buho.display_info()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_buho(buho)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 3:
        nombre = input("\nNombre del loro: ")
        edad = int(input("Edad: "))
        loro = Loro(0, nombre, edad, 0, 0, 0)
        loro.display_info()
        loro.alimentacion()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_loro(loro)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 4:
        nombre = input("\nNombre del delfin: ")
        edad = int(input("Edad: "))
        #gen = input("Genero F/M: ")
        #if gen=="F" or gen == "f":
            #genero = "femenino"
        #elif gen=="M" or gen == "m":
            #genero = "masculino"
        #else:
            #print("Error de Seleccion")
        delfin = Delfin(0, nombre, edad, 0, 0)
        delfin.display_info()
        delfin.alimentacion()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_delfin(delfin)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 5:
        nombre_zoo = input("Ingresa el nombre del zoologico para ver los animales: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 0 :
        print("Hasta luego")
        break

