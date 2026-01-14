from flask import Flask, jsonify, request

app = Flask(__name__)

## EXO1: API GET: renvoyer un helloworld - API end point name: "api/salutation"
@app.route('/api/salutation', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})
## EXO2: API POST: renvoyer un nom fourni en parametre - API end point name: "api/utilisateurs"
@app.route('/api/utilisateurs', methods=['POST'])
def post_nom():
    # On récupère les données JSON envoyées dans le corps (body) de la requête
    data = request.get_json()
    
    # On extrait la valeur associée à la clé "nom"
    # .get('nom') permet d'éviter une erreur si la clé est absente
    nom_utilisateur = data.get('nom', 'Utilisateur inconnu')
    
    # On retourne une réponse au format JSON
    return jsonify({
        "message": "Nom reçu avec succès",
        "nom": nom_utilisateur
    })
# to be tested with curl

# Commandes bash (attention, à adapter pour powershell)
# >> curl -i -X GET http://localhost:5000/api/salutation
# >> curl -i -X POST -H 'Content-Type: application/json' -d '{"nom": "Bob"}' http://localhost:5000/api/utilisateurs

if __name__ == '__main__':
    app.run(debug=True)
