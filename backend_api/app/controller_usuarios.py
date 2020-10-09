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

    def get_usuarios_id(self, id_usuario):
        usuario = self._buscar_usuario(id_usuario)
        return jsonify(
            id = usuario.id,
            login = usuario.login,
            id_estabelecimento = usuario.estabelecimento.id 
        )

    def get_validar_usuario_login(self, login):

        usuario = self._buscar_usuario_por_login(login)
        
        if usuario is not None:
            raise Exception("Já existe um cadastro com login informado!")
    
    def get_usuarios(self):
        usuarios = self._listar_todos_usuarios()
        json_response = []
        for usuario in usuarios:
            json_response.append({
                'id': usuario.id,
                'login': usuario.login,
                'id_estabelecimento': usuario.estabelecimento.id
            })
        return jsonify(json_response)

    def put_usuarios(self, id_usuario, request):
        login = request.json['login']
        senha = request.json['senha']
        id_estabelecimento = request.json['id_estabelecimento']
        
        usuario = self._atualizar_usuario(id_usuario, login, senha, id_estabelecimento)
        return jsonify(
            id = usuario.id,
            login = usuario.login,
            id_estabelecimento = usuario.estabelecimento.id
        )

    def post_usuarios_login(self, request):
        login = request.json['login']
        senha = request.json['senha']
        return self._efetuar_login(login, senha)
   


    #
    # métodos internos
    #

    def _criar_usuario(self, login, senha, id_estabelecimento):
        estabelecimento = Estabelecimento.query.filter_by(id=id_estabelecimento).first()
        novo_usuario = Usuario(login=login, senha=senha, estabelecimento=estabelecimento, isAdmin=False)
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario

    def _deletar_usuario(self, id):
        usuario = self._buscar_usuario(id)
        db.session.delete(usuario)
        db.session.commit()

    def _buscar_usuario(self, id):
        return Usuario.query.filter_by(id=id).first()

    def _buscar_usuario_por_login(self, login):
        return Usuario.query.filter_by(login=login).first()

    def _listar_todos_usuarios(self):
        return Usuario.query.all()

    def _atualizar_usuario(self, id_usuario, login, senha, id_estabelecimento):

        if(Usuario.query.filter(login == login and  id_usuario != id_usuario).count() > 0):
            raise Exception("Já existe um login com os dados informados!")

        usuario = self._buscar_usuario(id_usuario)
        estabelecimento = Estabelecimento.query.filter_by(id=id_estabelecimento).first()
        usuario.login = login
        usuario.senha = senha
        usuario.estabelecimento = estabelecimento
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def _efetuar_login(self, login, senha):
        usuario = Usuario.query.filter_by(login=login, senha=senha).first()

        if usuario is None:
            raise Exception("Login e/ou senha inválidos!")
        else:
            return jsonify(
            id = usuario.id,
            login = usuario.login,
            id_estabelecimento = usuario.estabelecimento.id,
            isAdmin = usuario.isAdmin)
