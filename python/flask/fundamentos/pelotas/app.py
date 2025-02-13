from flask import Flask, render_template

app = Flask(__name__)

@app.route('/juego')
@app.route('/juego/<int:x>')
@app.route('/juego/<int:x>/<color>')
def juego(x=3, color='red'):
    return render_template('juego.html', x=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)

