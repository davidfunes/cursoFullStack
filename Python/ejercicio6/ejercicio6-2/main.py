# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como
# atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(self, nota):
        if nota < 5:
            return "El alumno {} ha suspendido".format(self.nombre)
        else:
            return "El alumno {} ha aprobado".format(self.nombre)

    def __str__(self):
        return "Nombre: {}\nNota: {}\n{}\n".format(self.nombre, self.nota, self.resultado(self.nota))

alumno1 = Alumno("Matías", 9)
alumno2 = Alumno("Rosa", 4)
alumno3 = Alumno("David", 9.98)

print(alumno1)
print(alumno2)
print(alumno3)