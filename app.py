from flask import Flask, session, redirect, url_for, request, jsonify
from flask import render_template
import json
app = Flask(__name__)
app.secret_key = "secreto"
#Archivos json
with open("usuarios.json", encoding='utf-8') as users:
    usuarios_data = json.load(users)
@app.route("/",methods=["GET"])
def home(nombre='perfil'):
    with open("peliculas.json", encoding='utf-8') as pelis:
        pelis_data = json.load(pelis)
    session['contador'] = session.get('contador',0) + 1
    contador_visitas=session['contador']
    return render_template('index.html',name=nombre,peliculas=pelis_data,visitas=contador_visitas)

@app.route("/ingresar" )
def ingresar():
    return render_template('ingresar.html')

@app.route("/login", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        for i in (usuarios_data):
            if i["nombre"]==request.form["username"] and i["contrasenia"] == request.form["password"]:
                session["user"]=i["nombre"]
                return redirect(url_for("log", name=session["user"]))
        return "Usuario o contrasenia incorrectos"   
    

@app.route("/<name>")
def log(name):
    if 'user' in session:
        return render_template("logueado.html", name=name)
    else: 
        return "Necesita estar logueado"

@app.route("/directores")
def directores():
    with open("peliculas.json", encoding='utf-8') as pelis:
        pelis_data = json.load(pelis)
    return render_template('directores.html',peliculas=pelis_data)
@app.route("/generos")
def generos():
    with open("peliculas.json", encoding='utf-8') as pelis:
        pelis_data = json.load(pelis)
    return render_template('generos.html',peliculas=pelis_data)
@app.route("/imagenes")
def imagenes():
    with open("peliculas.json", encoding='utf-8') as pelis:
        pelis_data = json.load(pelis)
    return render_template('imagenes.html',peliculas=pelis_data)
@app.route("/buscarDirectores")
def buscar_directores():
    with open("peliculas.json", encoding='utf-8') as pelis:
        pelis_data = json.load(pelis)
    return render_template('buscar_directores.html',peliculas=pelis_data)
@app.route("/buscarPeliculas")
def buscar_peliculas():
    with open("peliculas.json", encoding='utf-8') as pelis:
        pelis_data = json.load(pelis)
    return render_template('buscar_peliculas.html',peliculas=pelis_data)
@app.route("/buscarActores")
def buscar_actores():
    with open("peliculas.json", encoding='utf-8') as pelis:
        pelis_data = json.load(pelis)
    return render_template('buscar_actores.html',peliculas=pelis_data)
@app.route("/agregarPeli")
def agregar():
    return render_template('agregarPeli.html')
@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('home'))
app.run( debug=True, port=8000 )