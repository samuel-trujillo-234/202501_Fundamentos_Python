from flask import Flask, render_template, request, redirect, session, make_response
import json
""""By Samuel Trujillo"""

app = Flask(__name__)
app.secret_key = "PATO"


@app.route('/')
def index():
    session.setdefault("visitas", 0)
    session.setdefault("reinicios", 0)
    visitas_guardadas = request.cookies.get("visitas")
    visitas_guardadas = json.loads(visitas_guardadas) if visitas_guardadas else {}
    return render_template("index.html", visitas=session["visitas"], reinicios=session["reinicios"], historial=visitas_guardadas)


@app.route('/incrementar', methods=['POST'])
def incrementar():
    session["visitas"] += 2
    return redirect('/')


@app.route('/aumentar_visitas', methods=['POST'])
def aumentar_visitas():
    try:
        cantidad = int(request.form.get("cantidad", 1))  
        session["visitas"] += cantidad
    except ValueError:
        pass  
    return redirect('/')


@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    session["reinicios"] += 1
    visitas_guardadas = request.cookies.get("visitas")
    visitas_guardadas = json.loads(visitas_guardadas) if visitas_guardadas else {}

    visitas_guardadas[f"Reinicio {session['reinicios']}"] = session["visitas"]
    session["visitas"] = 0

    resp = make_response(redirect('/'))
    resp.set_cookie("visitas", json.dumps(visitas_guardadas))
    return resp


@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
