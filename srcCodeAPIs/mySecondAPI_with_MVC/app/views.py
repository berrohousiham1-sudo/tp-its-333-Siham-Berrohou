from app import app
from flask import render_template, request, jsonify

### EXO1 - Implement a route that returns "hello" printed in a webpage using an html template
@app.route('/hello')
def exo1():
    return render_template('index.html')
### EXO2 - Implement a route that returns "hello {name}" with the name declared in the route (add html template)
@app.route('/hello/<name>')
def exo2(name):
    return render_template('index.html', name=name)
### EXO3 - Implement a route that returns "hello {name}" with the name retrieved from url, eg retrieved from http://localhost:5000/api/salutation?nom=Alice
@app.route('/hello_query')
def exo3():
    # Extrait 'name' depuis les arguments de la requête
    nom_recupere = request.args.get('name', 'Stranger')
    return render_template('index.html', name=nom_recupere)