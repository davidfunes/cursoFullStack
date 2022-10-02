# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una
# lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países
# ordenados alfabéticamente y separados por comas.

paises = input("Ingresa una lista de paises separados por comas: " )
paises = paises.split(',')
paises = set(paises) # Creamos un conjuto único
paises = sorted(paises)
paises = ", ".join(paises)

print(f"Listado de paises ordenado: {paises}")