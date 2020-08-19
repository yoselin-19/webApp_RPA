from flask import Flask, request, flash, redirect
from flask import render_template, url_for
import sqlite3

# Configuraciones
app = Flask(__name__)
app.config['SECRET_KEY'] = "MSG"


# Conexion con la base de datos
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Rutas del api

@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM student').fetchall()
    conn.close()
    print(students)
    datos = [{"nombre": "Hola"}, {"nombre": "Yoselin"}, {"nombre": "como"}, {"nombre": "estas?"}]
    return render_template('index.html', author="Yoselin", sunny=False, lista=datos, estudiantes=students)


@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if request.method == 'POST':
        carne = request.form['carne']
        año = request.form['año']
        semestre = request.form['semestre']

        if not (carne and semestre and año):
            flash('No se llenaron todos los campos del formulario, para consultar estudiante')
            return redirect(url_for('consulta'))
        else:
            cadena = "SELECT grupo FROM student WHERE año='{0}' AND semestre='{1}' AND carne='{2}'".format(año,semestre,carne)
            conn = get_db_connection()
            num = conn.execute(cadena).fetchall()
            conn.commit()
            conn.close()
            return render_template('consulta.html', num=num, presiono=True)

    return render_template('consulta.html')


@app.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        carne = request.form['carne']
        dpi = request.form['dpi']
        semestre = request.form['semestre']
        año = request.form['año']
        grupo = request.form['grupo']
        correo = request.form['correo']

        if not (nombre and carne and dpi and semestre and grupo and correo):
            flash('No se llenaron todos los campos del formulario, para insertar estudiante')
            return redirect(url_for('insertar'))
        else:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO student (nombre, carne, dpi, correo, semestre, año, grupo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (nombre, carne, dpi, correo, semestre, año, grupo)
                )
            conn.commit()
            conn.close()
            flash('Se inserto con exito')
            return redirect(url_for('insertar'))

    return render_template('insertar.html')


@app.route('/grupo', methods=['GET', 'POST'])
def grupo():
    if request.method == "POST":
        grupo = request.form['grupo']

        if not grupo:
            flash('No se llenaron todos los campos del formulario, para consultar grupo')
            return redirect(url_for('grupo'))
        else:
            cadena = "SELECT carne, correo FROM student WHERE grupo='{0}'".format(grupo)
            conn = get_db_connection()
            datos = conn.execute(cadena).fetchall()
            conn.commit()
            conn.close()
            return render_template('grupo.html', datos=datos)

    return render_template('grupo.html')


# @app.route('/grupo/int:<group_id>')
# def getgrupo(group_id):
#     return 'form_grupo ' + str(group_id)


if __name__ == 'main':
    app.run()
