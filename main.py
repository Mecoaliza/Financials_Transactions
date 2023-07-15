from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('consulta.html')

@app.route('/login', methods=['POST'])
def login():

    user_id = request.form.get('user_id')

    with open('dataset.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)
        cont = 0
        for usuario in usuarios:
            cont += 1
            if usuario['user_id'] == user_id:
                return render_template("consulta.html")
            
            if cont >= len(usuarios):
                flash('USUÁRIO INVÁLIDO')
                return redirect("/")





if __name__ in "__main__":
    app.run(debug=True)   