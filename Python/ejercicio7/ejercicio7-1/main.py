# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar,
# restar, multiplicar y dividir.
#
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que
# mostrarlos por consola.


import operaciones as o

a = 5
b = 3

print("{} + {} = {}".format(a, b, o.sumar(a, b)))
print("{} - {} = {}".format(a, b, o.restar(a, b)))
print("{} * {} = {}".format(a, b, o.multiplicar(a, b)))
print("{} / {} = {}".format(a, b, round(o.dividir(a, b),4)))

