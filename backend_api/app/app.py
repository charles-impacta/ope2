import os
import sys
from flask import Flask, request, jsonify
from .model import db, Usuario
from .controller_estabelecimentos import ControllerEstabelecimentos
from .controller_usuarios import ControllerUsuarios
from .controller_categorias import ControllerCategorias
from .controller_produtos import ControllerProdutos
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

controller_estabelecimentos = ControllerEstabelecimentos()
controller_usuarios = ControllerUsuarios()
controller_categorias = ControllerCategorias()
controller_produtos = ControllerProdutos()

#
# /estabelecimentos/
#

@app.route('/estabelecimentos/', methods=['POST'])
def post_estabelecimentos():
    try:
        return controller_estabelecimentos.post_estabelecimentos(request)
    except Exception as e:
        return str(e) , 400


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

@app.route('/usuarios/login', methods=['POST'])
def post_usuarios_login():
    try:
        return controller_usuarios.post_usuarios_login(request)
    except Exception as e:
        return str(e) , 400

@app.route('/usuarios/validar-login/<login>', methods=['GET'])
def get_validar_login(login):
    try:
        controller_usuarios.get_validar_usuario_login(login)
        return jsonify("ok")
    except Exception as e:
        return str(e) , 400
#
# /categorias/
#

@app.route('/categorias/', methods=['POST'])
def post_categorias():
    try:
        return controller_categorias.post_categorias(request)
    except Exception as e:
        return str(e) , 400


@app.route('/categorias/<id_categoria>', methods=['DELETE'])
def delete_categorias(id_categoria):
    return controller_categorias.delete_categorias(id_categoria)

@app.route('/categorias/', methods=['PUT'])
def put_categorias():
    try:
        return controller_categorias.put_categorias(request)
    except Exception as e:
        return str(e) , 400

@app.route('/categorias/<id_categoria>', methods=['GET'])
def get_categorias_id(id_categoria):
    return controller_categorias.get_categorias_id(id_categoria)


@app.route('/categorias/', methods=['GET'])
def get_categorias():
    return controller_categorias.get_categorias()

@app.route('/categorias-ativas/', methods=['GET'])
def get_categorias_ativas():
    return controller_categorias.get_categorias_ativas()


#
# /produtos/
#

@app.route('/produtos/', methods=['POST'])
def post_produtos():
    try:
        return controller_produtos.post_produtos(request)
    except Exception as e:  
        return str(e), 400

@app.route('/produtos/', methods=['PUT'])
def put_produtos():
    try:
        return controller_produtos.put_produtos(request)
    except Exception as e:
        return str(e), 400

@app.route('/produtos/<id_produto>', methods=['DELETE'])
def delete_produtos(id_produto):
    return controller_produtos.delete_produtos(id_produto)


@app.route('/produtos/<id_produto>', methods=['GET'])
def get_produtos_id(id_produto):
    return controller_produtos.get_produtos_id(id_produto)

@app.route('/produtos-estabelecimento/<id_estabelecimento>', methods=['GET'])
def get_produtos_estabelecimento_id(id_estabelecimento):
    return controller_produtos.get_produtos_estabelecimento_id(id_estabelecimento)

@app.route('/produtos-estabelecimento-ativo/<id_estabelecimento>', methods=['GET'])
def get_produtos_estabelecimento_id_ativo(id_estabelecimento):
    return controller_produtos.get_produtos_estabelecimento_id_ativo(id_estabelecimento)

@app.route('/produtos-categoria-ativo/<id_categoria>', methods=['GET'])
def get_produtos_categoria_id_ativo(id_categoria):
    return controller_produtos.get_produtos_categoria_id_ativo(id_categoria)

@app.route('/produtos-categoria/<id_categoria>', methods=['GET'])
def get_produtos_categoria_id(id_categoria):
    return controller_produtos.get_produtos_categoria_id(id_categoria)

@app.route('/produtos/', methods=['GET'])
def get_produtos():
    return controller_produtos.get_produtos()

@app.route('/produtos-ativos/', methods=['GET'])
def get_produtos_ativos():
    return controller_produtos.get_produtos_ativos()    



