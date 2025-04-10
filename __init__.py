from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(name)

@app.route('/')
def hello_world():
    return render_template('hello.html')  #Comm3

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptpage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token>')
def decryptpage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur = f.decrypt(token_bytes).decode()  # Décryptage + conversion en str
        return f"Valeur décryptée : {valeur}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

if name == "main":
    app.run(debug=True)
