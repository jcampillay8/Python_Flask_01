from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hola_mudo():
    return "Hola Mundo"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<nombre>")
def saludo(nombre):
    return "¡Hola "+nombre+"!"

@app.route('/repeat/<word>')
def repeat(word):
    word = word
    return render_template ("index.html",word = word)

if __name__ == "__main__":
    app.run(debug=True)