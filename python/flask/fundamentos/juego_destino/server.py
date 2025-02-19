from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "Pata"  

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    session['nombre'] = request.form.get("nombre", "")
    session['lugar'] = request.form.get("lugar", "")
    session['numero'] = request.form.get("numero", "")
    session['comida'] = request.form.get("comida", "")
    session['profesion'] = request.form.get("profesion", "")

    return redirect(url_for("future"))

@app.route("/futuro")
def future():
    nombre = session.get('nombre', "[nombre]")
    lugar = session.get('lugar', "[lugar]")
    numero = session.get('numero', "[numero]")
    comida = session.get('comida', "[comida]")
    profesion = session.get('profesion', "")

    mensaje1 = f"Soy el adivino del Dojo, {nombre} tendrá un viaje muy largo dentro de {numero} años a {lugar} y estará el resto de sus días preparando {comida} para todas las personas que quiere."
    
    mensaje2 = f"Soy el adivino del Dojo, {nombre} tendrá {numero} años de mala suerte, nunca conocerá {lugar} y jamás volvió a comer {comida}."
    
    mensaje3 = f"Puedo predecir que {nombre} te ocurrirá algo en {numero} años donde conocerás la más espectacular {comida} en {lugar}."

    mensaje = random.choice([mensaje1, mensaje2, mensaje3])

    return render_template("futuro.html", mensaje=mensaje, profesion=profesion)

if __name__ == "__main__":
    app.run(debug=True)
