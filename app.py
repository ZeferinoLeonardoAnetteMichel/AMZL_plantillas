from flask import Flask, render_template,request, redirect, url_for, flash
app = Flask(__name__)
app.config['SECRET_KEY']='una_clave_secreta_muy_larga_y_dificil_de_adivinar'
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/animales')
def animales_exoticos():
    return render_template('animales_exoticos.html')

@app.route('/vehiculos')
def vehiculos_antiguos():
    return render_template('vehiculos_antiguos.html')

@app.route('/maravillas')
def maravillas_del_mundo():
    return render_template('maravillas_del_mundo.html')

@app.route('/acerca')
def acerca_de():
    return render_template('acerca_de.html')

@app.route('/formulario', methods = ("GET","POST"))
def formulario():
    error=None
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        fechadenacimiento = request.form ["fechadenacimiento"]
        genero = request.form ["genero"]
        email = request.form ["email"]
        password = request.form["password"]
        
    if password != password:
            error ="La contraseña no coincide"
            if error != None:
                flash(error)
                return render_template('platillainicio.html')
            else:
                flash(f"¡Registro exitoso para el usuario:{nombre}")
                return render_template("inicio.html")
    return render_template('platillainicio.html')
           
if __name__ == '__main__':
    app.run(debug=True)