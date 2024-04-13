from flask import Flask, render_template

app = Flask(__name__)

# Criando página
@app.route("/")
def home():
    return render_template('home.html') # chamando conteúdo de um html

@app.route("/contato")
def contato():
    return render_template('contato.html') # chamando conteúdo de um html

if __name__ == "__main__":
    app.run(debug=True)
