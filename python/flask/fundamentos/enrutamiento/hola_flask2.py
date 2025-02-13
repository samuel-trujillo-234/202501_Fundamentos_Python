from flask import Flask

app = Flask(__name__)  

@app.route('/')  
def home():
    return '¡Hola desde Flask!' 


@app.route('/ruta')  
def buscar_ruta():
    return '¿Qué ruta estás buscando?'


@app.route('/bienvenido/<string:nombre>')  
def bienvenido(nombre):
    return f'Bienvenid@ a esta ruta {nombre}'


@app.route('/repite/<int:veces>/<string:palabra>')  
def repetir_palabra(veces, palabra):
    resultado = "Repite después de mí: "
    for _ in range(veces):
        resultado += palabra + " "
    return resultado

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return '¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo.', 404

if __name__ == "__main__":  
    app.run(debug=True)
