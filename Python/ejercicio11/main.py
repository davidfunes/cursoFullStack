# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo
# entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
#
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3
from faker import Faker
import pprint

faker = Faker()


def conectar_db():
    return sqlite3.connect('data.db')


def crear_cursor(conn):
    return conn.cursor()


def insertar_alumno(alumno):
    conn = conectar_db()
    cursor = crear_cursor(conn)

    query = 'INSERT INTO alumnos(nombre, apellido) VALUES(?,?)'
    cursor.execute(query, alumno)
    conn.commit()

    cursor.close()
    conn.close()


def buscar_alumno(nombre):
    conn = conectar_db()
    cursor = crear_cursor(conn)

    query = f'SELECT * FROM alumnos WHERE nombre="{nombre}"'
    rows = cursor.execute(query).fetchall()

    cursor.close()
    conn.close()
    return rows


conn = conectar_db()
cursor = crear_cursor(conn)

rows = cursor.execute('CREATE TABLE if not exists alumnos('
                      'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                      'nombre TEXT NOT NULL,'
                      'apellido TEXT NOT NULL)')

conn.commit()
cursor.close()
conn.close()


alumnos = []
for i in range(10):
    alumnos.append((faker.first_name(), faker.last_name()))

pprint.pprint(alumnos)
print(type(alumnos))

for alumno in alumnos:
    insertar_alumno(alumno)

rows = buscar_alumno("David")

if rows:
    print("He encontrado estos resultados\n")
    for row in rows:
        print(f'ID: {row[0]}\n'
              f'Nombre: {row[1]}\n'
              f'Apellido: {row[2]}\n')
else:
    print("No se ha econtrado el alumno!")
