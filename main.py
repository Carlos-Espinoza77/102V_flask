from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")# es un decorador que indica que la función hello_world() se ejecutará cuando se acceda a la ruta raíz del servidor web.
def hello_world():
    return render_template("index.html")# devuelve el contenido de la plantilla HTML "index.html" como respuesta a la solicitud HTTP.
