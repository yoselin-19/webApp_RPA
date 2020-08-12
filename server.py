from flask import Flask, request
from flask import render_template

app = Flask(__name__)


# Rutas del api

@app.route('/')
def index():
    datos = [{"nombre": "Hola"}, {"nombre": "Yoselin"}, {"nombre": "como"}, {"nombre": "estas?"}]
    return render_template('index.html', author="Yoselin", sunny=False, lista=datos)


@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if request.method == 'POST':
        pass
    return render_template('consulta.html')


@app.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        pass
    return render_template('insertar.html')


@app.route('/grupo', methods=['GET', 'POST'])
def grupo():
    if request.method == "POST":
        pass
    return render_template('grupo.html')


# @app.route('/grupo/int:<group_id>')
# def getgrupo(group_id):
#     return 'form_grupo ' + str(group_id)


if __name__ == 'main':
    app.run()
