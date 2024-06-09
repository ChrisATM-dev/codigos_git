
from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/') 
def inicio():
    return "¡Hola desde Flask!"


@app.route("/loteria")
def loteria():
    return render_template("Loteria_Mexicana.html")

@app.route("/loteria/<int:numero>")
def loteria_numero(numero):
    return render_template("Loteria_Mexicana_numero.html", numero=numero)

@app.route("/loteria/<int:fila>/<int:columna>")
def loteria_XY(fila,columna):
    return render_template("Loteria_Mexicana_XY.html", fila=fila, columna=columna)


@app.route("/<int:fila>/<int:columna>")
def contador(fila,columna):
    return render_template("contador.html", fila=fila, columna=columna)

@app.route("/loteria2/<int:fila>/<int:columna>")
def bonus(fila,columna):
    return render_template("Loteria_Mexicana_mejorado.html", fila=fila, columna=columna)

if __name__ == "__main__":
    app.run(debug=True)



