import os
import sys

from flask import Flask, jsonify, request
from .model import db, Usuario
from .controller_estabelecimento import ControllerEstabelecimento

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

controller_estabelecimento = ControllerEstabelecimento()


@app.route('/estabelecimentos/', methods=['POST'])
def post_estabelecimentos():
    nome = request.json['nome']
    cnpj = request.json['cnpj']
    id_novo_estabelecimento = controller_estabelecimento.criar_estabelecimento(nome, cnpj)
    return jsonify(
        mensagem='Estabelecimento criado com sucesso.',
        id = id_novo_estabelecimento
    )


@app.route('/estabelecimentos/<id_estabelecimento>', methods=['DELETE'])
def delete_estabelecimentos(id_estabelecimento):
    controller_estabelecimento.deletar_estabelecimento(id_estabelecimento)
    return jsonify(
        mensagem = 'Estabelecimento deletado com sucesso.'
    )


@app.route('/estabelecimentos/<id_estabelecimento>', methods=['GET'])
def get_estabelecimentos_id(id_estabelecimento):
    estabelecimento = controller_estabelecimento.buscar_estabelecimento(id_estabelecimento)
    return jsonify (
        id = estabelecimento.id,
        nome = estabelecimento.nome,
        cnpj = estabelecimento.cnpj
    )


@app.route('/estabelecimentos/', methods=['GET'])
def get_estabelecimentos():
    estabelecimentos = controller_estabelecimento.listar_todos_estabelecimentos()
    json_response = []
    for estabelecimento in estabelecimentos:
        json_response.append({
            'id': estabelecimento.id,
            'nome': estabelecimento.nome,
            'cnpj': estabelecimento.cnpj
        })    
    return jsonify (json_response)


@app.route('/estabelecimentos/<id_estabelecimento>', methods=['PUT'])
def put_estabelecimentos(id_estabelecimento):
    nome = request.json['nome']
    cnpj = request.json['cnpj']
    controller_estabelecimento.atualizar_estabelecimento(id_estabelecimento, nome, cnpj)
    estabelecimento = controller_estabelecimento.buscar_estabelecimento(id_estabelecimento)
    return jsonify (
        id = estabelecimento.id,
        nome = estabelecimento.nome,
        cnpj = estabelecimento.cnpj
    )
