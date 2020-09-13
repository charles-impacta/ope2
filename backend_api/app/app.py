import os
import sys

from flask import Flask, request, jsonify
from .model import db, Usuario
from .controller_estabelecimentos import ControllerEstabelecimentos
from .controller_usuarios import ControllerUsuarios

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

controller_estabelecimentos = ControllerEstabelecimentos()
controller_usuarios = ControllerUsuarios()

#
# /estabelecimentos/
#

@app.route('/estabelecimentos/', methods=['POST'])
def post_estabelecimentos():
    return controller_estabelecimentos.post_estabelecimentos(request)


@app.route('/estabelecimentos/<id_estabelecimento>', methods=['DELETE'])
def delete_estabelecimentos(id_estabelecimento):
    return controller_estabelecimentos.delete_estabelecimentos(id_estabelecimento)


@app.route('/estabelecimentos/<id_estabelecimento>', methods=['GET'])
def get_estabelecimentos_id(id_estabelecimento):
    return controller_estabelecimentos.get_estabelecimentos_id(id_estabelecimento)


@app.route('/estabelecimentos/', methods=['GET'])
def get_estabelecimentos():
    return controller_estabelecimentos.get_estabelecimentos()


@app.route('/estabelecimentos/<id_estabelecimento>', methods=['PUT'])
def put_estabelecimentos(id_estabelecimento):
    return controller_estabelecimentos.put_estabelecimentos(id_estabelecimento, request)

#
# /usuarios/
#

@app.route('/usuarios/', methods=['POST'])
def post_usuarios():
    return controller_usuarios.post_usuarios(request)


@app.route('/usuarios/<id_usuario>', methods=['DELETE'])
def delete_usuarios(id_usuario):
    return controller_usuarios.delete_usuarios(id_usuario)


@app.route('/usuarios/<id_usuario>', methods=['GET'])
def get_usuarios_id(id_usuario):
    return controller_usuarios.get_usuarios_id(id_usuario)

@app.route('/usuarios/', methods=['GET'])
def get_usuarios():
    return controller_usuarios.get_usuarios()

@app.route('/usuarios/<id_usuario>', methods=['PUT'])
def put_usuarios(id_usuario):
    return controller_usuarios.put_usuarios(id_usuario, request)
