from flask import Flask, jsonify, make_response, request
from db import Clientes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/clientes', methods=['GET'])
def get_clientes():
    return make_response(
        jsonify(lista_de_clientes = Clientes))
    
@app.route('/clientes', methods=['POST'])
def create_cliente():
    cliente = request.json
    Clientes.append(cliente)
    return make_response(jsonify(cliente_criado = cliente))

app.run()