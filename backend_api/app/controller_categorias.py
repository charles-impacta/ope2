from .model import db, Categoria
from flask import jsonify

class ControllerCategorias():

    def post_categorias(self, request):
        nome = request.json['nome']
        novo_categoria = self._criar_categoria(nome)
        return jsonify(
            mensagem='Categoria criada com sucesso.',
            id = novo_categoria.id
        )

    def delete_categorias(self, id_categoria):
        self._deletar_categoria(id_categoria)
        return jsonify(
            mensagem = 'Categoria deletada com sucesso.'
        )

    def get_categorias_id(self, id_categoria):
        categoria = self._buscar_categoria(id_categoria)
        return jsonify(
            id = categoria.id,
            nome = categoria.nome
        )

    def get_categorias(self):
        categorias = self._listar_todos_categorias()
        json_response = []
        for categoria in categorias:
            json_response.append({
                'id': categoria.id,
                'nome': categoria.nome
            })    
        return jsonify(json_response)

    def put_categorias(self, id_categoria, request):
        nome = request.json['nome']
        categoria = self._atualizar_categoria(id_categoria, nome)
        return jsonify(
            id = categoria.id,
            nome = categoria.nome
        )

    #
    # métodos internos
    #

    def _criar_categoria(self, nome):
        novo_categoria = Categoria(nome=nome)
        db.session.add(novo_categoria)
        db.session.commit()
        return novo_categoria

    def _deletar_categoria(self, id):
        categoria = self._buscar_categoria(id)
        db.session.delete(categoria)
        db.session.commit()

    def _buscar_categoria(self, id):
        return Categoria.query.filter_by(id=id).first()

    def _atualizar_categoria(self, id, nome):
        categoria = self._buscar_categoria(id)
        categoria.nome = nome
        db.session.add(categoria)
        db.session.commit()
        return categoria

    def _listar_todos_categorias(self):
        return Categoria.query.all()
