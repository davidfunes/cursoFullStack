# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del
# archivo. Para ello, tendréis que acceder dos veces al archivo creado.

# Trucamos archivo y añadimos una lista
file = open('data.txt', 'w')
datos = ['**Primer acceso al archivo','dato 1', 'dato 2', 'dato 3\n', 'dato 4', 'dato 5']

for dato in datos:
    if not dato.endswith('\n'):
        dato += '\n'
        file.write(dato)
    else:
        file.write(dato)

file.close()

# Abrimos por segunda vez en modo lectura para actualizar
file = open('data.txt', 'r+')
file.readlines()
file.write("**Segundo acceso al archivo\n")
file.write("Añadimos una linea extra de prueba")
file.close()

# Volvemos a cargar el archivo para mostrar los datos
file = open('data.txt', 'r+')
datos = file.readlines()

for dato in datos:
    dato = dato.rstrip('\n')
    print(dato)

file.close()
