class Vehiculo:
    def __init__(self, tipo, marca, matricula, color):
        self.tipo = tipo
        self.marca = marca
        self.matricula = matricula
        self.color = color

    def __str__(self):
        return f"Tipo: {self.tipo}\n" \
               f"Marca: {self.marca}\n" \
               f"Matrícula: {self.matricula}\n" \
               f"Color: {self.color}\n"