from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "key"

cartas = [
    "0 - Carta no válida",
    "1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", "5  El paraguas",
    "6  La sirena", "7  La escalera", "8  La botella", "9  El barril", "10 El árbol",
    "11 El melón", "12 El valiente", "13 El gorrito", "14 La muerte", "15 La pera",
    "16 La bandera", "17 El bandolón", "18 El violoncello", "19 La garza", "20 El pájaro",
    "21 La mano", "22 La bota", "23 La luna", "24 El cotorro", "25 El borracho",
    "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", "30 El camarón",
    "31 Las jaras", "32 El músico", "33 La araña", "34 El soldado", "35 La estrella",
    "36 El cazo", "37 El mundo", "38 El apache", "39 El nopal", "40 El alacrán",
    "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito", "45 El venado",
    "46 El sol", "47 La corona", "48 La chalupa", "49 El pino", "50 El pescado",
    "51 La palma", "52 La maceta", "53 El arpa", "54 La rana"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 54)
        session["intentos"] = 0
    
    mensaje = ""
    color = "black"
    
    if request.method == "POST":
        try:
            numero_usuario = int(request.form["adivinar"])
            session["intentos"] += 1
            
            if numero_usuario < session["numero_secreto"]:
                mensaje = "El número es mayor. Inténtalo de nuevo."
                color = "blue"
            elif numero_usuario > session["numero_secreto"]:
                mensaje = "El número es menor. Inténtalo de nuevo."
                color = "red"
            else:
                mensaje = f"¡Lotería! Has adivinado en {session['intentos']} intentos. La carta es: {cartas[session['numero_secreto']]}"
                color = "green"
                session.pop("numero_secreto")  
                session.pop("intentos")
        except ValueError:
            mensaje = "Por favor, ingresa un número válido."
            color = "orange"
    
    return render_template("index.html", mensaje=mensaje, color=color)

if __name__ == "__main__":
    app.run(debug=True)
