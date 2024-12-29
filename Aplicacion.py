from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# Configuuracion de proyecto
application = Flask(__name__)
cors= CORS(application)
application.config["CORS_HEADERS"]= "Content-Type"

# Metodos de llamada
@application.route("/api/")
def indice_contenidos():
    return"<button>Hola<button>"
