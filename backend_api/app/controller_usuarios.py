from .model import db, Usuario, Estabelecimento
from flask import jsonify


class ControllerUsuarios:

    def post_usuarios(self, request):
        login = request.json['login']
        senha = request.json['senha']
        id_estabelecimento = request.json['id_estabelecimento']
        novo_usuario = self._criar_usuario(login, senha, id_estabelecimento)
        return jsonify(
            mensagem=u'Usuário criado com sucesso.',
            id=novo_usuario.id
        )

    def delete_usuarios(self, id_usuario):
        self._deletar_usuario(id_usuario)
        return jsonify(
            mensagem = u'Usuário deletado com sucesso.'
        )

    #
    # métodos internos
    #

    def _criar_usuario(self, login, senha, id_estabelecimento):
        estabelecimento = Estabelecimento.query.filter_by(id=id_estabelecimento).first()
        novo_usuario = Usuario(login=login, senha=senha, estabelecimento=estabelecimento)
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario

    def _deletar_usuario(self, id):
        usuario = Usuario.query.filter_by(id=id).first()
        db.session.delete(usuario)
        db.session.commit()
