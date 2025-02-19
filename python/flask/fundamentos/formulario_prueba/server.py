from flask import Flask, render_template, request, redirect, sessions

app = Flask(__name__)

app.secret_key = 'payaso'

@app.route('/') 
def index():
    return render_template("index.html")

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    print("Recibiendo informacion")
    print("request.form")
    session['nombre_usuario'] = request.form['nombre']
    session['email_usuario'] = request.form['email']
    return redirect('/mostrar_usuario')

@app.route('/mostrar_usuario')

def mostrar_usuario():
    print("Usuario redirigido")
    print(session['nombre_usuario'])
    print(session['email_usuario'])
    return render_template("mostrar.html")

if __name__ == "__main__":
    app.run(debug = True)


