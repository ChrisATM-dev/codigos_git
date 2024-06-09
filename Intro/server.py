## 1.- pipenv install flask para agregar los archivos
## 2.- pyhton <nombre del archivo>
## 3.- ctrl + c para detener el seridor
## 4.- Para salirnos del entorno virtual


from flask import  Flask, render_template

app = Flask(__name__) # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/') # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def inicio():
    return "¡Hola desde Flask!" # Devuelve la cadena '¡¡Hola desde Flask!!' como respuesta

@app.route('/hola/<name>') # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def te_amito(name):
    return f"Este es un saludo para {name}"
 
@app.route('/hola/<int:n>') # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def numero(n):
    return f"el numero es: {n}"

# 1) Crear la ruta /reto y al ir ahí, que muestre “Bienvenido al reto”
@app.route('/reto')
def reto():
    return "Bienvenido al reto"
# 2) Que el link reciba una frase en su URL, y que imprima: “Bienvenido al reto” y luego se despliegue la frase de la URL
@app.route('/reto/<frase>')
def reto_frase(frase):
    return f"Bienvenido al reto, {frase}"
# 3) Colocar luego de la frase, un número, y que la frase se repita la cantidad de veces del número
@app.route('/reto/<frase>/<int:numero>')
def reto_frase_numero(frase, numero):
    
    return  "Bienvenido al reto " + ((frase+ " ") * numero)

########### clase 2 ###########
@app.route("/bienvenidas")
def binevenidas():
    return render_template("index.html") #la carpeta del archivo siempre se debe lllamar "templates"

@app.route("/usuarios/<name>/<int:num>")
def usuarios(name, num):
    usuarios = ["Christian", "Francisca", "Vicente", "Marla"]
    return render_template("usuarios.html", nombre=name, numero=num, usuarios=usuarios)


if __name__ == "__main__": # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente

    app.run(debug=True)# Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo



