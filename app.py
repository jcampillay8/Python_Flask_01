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

@app.route('/repeat/<word>/<number>')
def repeat(word,number):
    word = word
    number = number
    return render_template ("index.html",word = word, number = number)

if __name__ == "__main__":
    app.run(debug=True)