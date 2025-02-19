from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'super_secret_key'

lugares = {
    'templo': (10, 20),
    'pirámide': (5, 15),
    'selva': (1, 10),
    'ruinas': (-15, 20)  
}

@app.route('/')
def index():
    if 'reliquias' not in session:
        session['reliquias'] = 0
        session['actividades'] = []
        session['intentos'] = 0
    return render_template('index.html', reliquias=session['reliquias'], actividades=session['actividades'])

@app.route('/buscar_reliquias', methods=['POST'])
def buscar_reliquias():
    lugar = request.form.get('lugar')
    min_r, max_r = lugares.get(lugar, (0, 0))
    encontradas = random.randint(min_r, max_r)
    session['reliquias'] += encontradas
    session['intentos'] += 1
    
    color = "green" if encontradas >= 0 else "red"
    actividad = f"<li style='color:{color};'>Exploraste {lugar} y {'ganaste' if encontradas >= 0 else 'perdiste'} {abs(encontradas)} reliquias.</li>"
    session['actividades'].insert(0, actividad)  
    
    if session['reliquias'] >= 500 and session['intentos'] <= 15:
        session['actividades'].insert(0, "<li style='color:blue;'>¡Felicidades! Has ganado el juego.</li>")
    
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)