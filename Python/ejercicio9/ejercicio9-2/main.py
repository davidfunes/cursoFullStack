# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada
# por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce


def get_impar(lis):
    return list(filter(lambda x: x % 2, lis))


lista = list(range(10))
print(f"La lista original: {lista}")
listaFiltrada = get_impar(lista)
print(f"Lista filtrada: {listaFiltrada}")

resultado = reduce(lambda x, y: x + y, listaFiltrada)
print(f"El resultado es: {resultado}")
