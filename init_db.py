import sqlite3

# Creando archivo donde se almacenara la BD
connection = sqlite3.connect('database.db')

with open('schema.txt', "r", encoding="utf-8") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO student (nombre, carne, dpi, correo, semestre, año, grupo) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Yoselin Lemus', '201403819', '2382216360101', 'prueba@gmail.com', 2, 2020, 1)
            )

connection.commit()
connection.close()
