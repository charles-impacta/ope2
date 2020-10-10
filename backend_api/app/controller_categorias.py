from .model import db, Categoria
from flask import jsonify
import json 
from str2bool import str2bool

class ControllerCategorias():

    def post_categorias(self, request):
        nome = request.json['nome']
        inativo = str2bool(str(request.json['inativo']).lower())
        novo_categoria = self._criar_categoria(nome=nome, inativo=inativo)
        return jsonify(
            mensagem='Categoria criada com sucesso.',
            id=novo_categoria.id
        )

    def delete_categorias(self, id_categoria):
        self._deletar_categoria(id_categoria)
        return jsonify(
            mensagem='Categoria deletada com sucesso.'
        )

    def get_categorias_id(self, id_categoria):
        categoria = self._buscar_categoria(id_categoria)
        return jsonify(
            id=categoria.id,
            nome=categoria.nome,
            inativo=categoria.inativo)

    def get_categorias(self):
        categorias = self._listar_todos_categorias()
        json_response = []
        for categoria in categorias:
            json_response.append({
                'id': categoria.id,
                'nome': categoria.nome,
                'inativo' : categoria.inativo
            })
        return jsonify(json_response)

    def get_categorias_ativas(self):
        categorias = self._listar_todos_categorias_ativas()
        json_response = []
        for categoria in categorias:
            json_response.append({
                'id': categoria.id,
                'nome': categoria.nome
            })
        return jsonify(json_response)

    def put_categorias(self, request):
        categoria = self._buscar_categoria(request.json["id"])

        if categoria == None:
            raise Exception("Nenhuma categoria encontrada!")

        if Categoria.query.filter(Categoria.nome == request.json["nome"] , Categoria.id != request.json["id"]).count() > 0:
            raise Exception("Já existe uma categoria com o nome informado!")

        categoria.nome = request.json['nome']
        categoria.inativo = str2bool(str(request.json['inativo']).lower())
        categoria = self._atualizar_categoria(categoria)
        return jsonify(
            id=categoria.id,
            nome=categoria.nome
        )

    #
    # métodos internos
    #

    def _criar_categoria(self, nome, inativo):

        if Categoria.query.filter_by(nome=nome).count() > 0:
            raise Exception("Já existe uma categoria com o nome informado")

        novo_categoria = Categoria(nome=nome, inativo=inativo)
        db.session.add(novo_categoria)
        db.session.commit()
        return novo_categoria

    def _deletar_categoria(self, id):
        categoria = self._buscar_categoria(id)
        db.session.delete(categoria)
        db.session.commit()

    def _buscar_categoria(self, id):
        return Categoria.query.filter_by(id=id).first()

    def _atualizar_categoria(self, categoria):
        db.session.add(categoria)
        db.session.commit()
        return categoria

    def _listar_todos_categorias(self):
        return Categoria.query.all()

    def _listar_todos_categorias_ativas(self):
        return Categoria.query.filter_by(inativo=False)
