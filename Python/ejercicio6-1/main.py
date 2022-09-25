# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#
# Color
# Ruedas
# Puertas
#
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#
# Velocidad
# Cilindrada
#
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):

    velocidad = 160.97
    cilindrada = 1.6

coche = Coche()

print("Color:",coche.color)
print("Ruedas:",coche.ruedas)
print("Puertas:",coche.puertas)
print("Velocidad:",coche.velocidad)
print("Cilindrada:",coche.cilindrada)