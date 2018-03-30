#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def accueil():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    return render_template('index.html', titre="Bienvenue !", mots=mots)

if __name__ == '__main__':
    app.run(debug=True)

