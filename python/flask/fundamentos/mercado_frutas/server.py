from flask import Flask, render_template, request

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")

    fresa = int(request.form.get("fresa", 0))
    frambuesa = int(request.form.get("frambuesa", 0))
    manzana = int(request.form.get("manzana", 0))

    total_frutas = fresa + frambuesa + manzana

    print(f"Total de frutas: {total_frutas}")

    return render_template(
        "checkout.html",
        nombre=nombre,
        apellido=apellido,
        email=email,
        fresa=fresa,
        frambuesa=frambuesa,
        manzana=manzana,
        total_frutas=total_frutas
    )

@app.route('/frutas')         
def fruits():
    return render_template("frutas.html")

if __name__=="__main__":   
    app.run(debug=True)
