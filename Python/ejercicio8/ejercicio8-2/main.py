# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto
# de ella, lo guardaréis en un archivo y luego lo cargamos.

from pickle import *
from library.Vehiculo import Vehiculo

def main():
    vehiculo1 = Vehiculo("Coche", "Skoda", "0037GHN","Negro")
    print(vehiculo1)

    file = open("data_object", "w+b")

    dump(vehiculo1, file)

    file.seek(0)
    vehiculo2 = load(file)

    print(f"Este es el vehículo recuperado\n"
          f"\n"
          f"{vehiculo2}")

if __name__ == "__main__":
    main()
