from .model import db, Produto, Estabelecimento, Categoria
from flask import jsonify
from str2bool import str2bool

class ControllerProdutos():

    def post_produtos(self, request):
        nome = request.json['nome']
        descricao = request.json['descricao']
        ingredientes = request.json['ingredientes']
        modo_de_preparo = request.json['modo_de_preparo']
        preco = request.json['preco']
        estabelecimento_id = request.json['estabelecimento_id']
        categoria_id = request.json['categoria_id']
        inativo = str2bool(str(request.json['inativo']))
        novo_produto = self._criar_produto(nome, descricao, ingredientes, modo_de_preparo, preco, estabelecimento_id, categoria_id,inativo)
        return jsonify(
            mensagem='Produto criado com sucesso.',
            id=novo_produto.id
        )

    def delete_produtos(self, id_produto):
        self._deletar_produto(id_produto)
        return jsonify(
            mensagem='Produto deletado com sucesso.'
        )

    def get_produtos_id(self, id_produto):
        produto = self._buscar_produto(id_produto)
        return jsonify(
            id=produto.id,
            nome=produto.nome,
            descricao=produto.descricao,
            ingredientes=produto.ingredientes,
            modo_de_preparo=produto.modo_de_preparo,
            preco=produto.preco,
            estabelecimento_id=produto.estabelecimento.id,
            categoria_id=produto.categoria.id,
            inativo=produto.inativo
        )
    
    def get_produtos_estabelecimento_id(self, estabelecimento_id):
        produtos = self._buscar_produtos_estabelecimento(estabelecimento_id)
        json_response = []
        for produto in produtos:
            json_response.append({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'ingredientes': produto.ingredientes,
                'modo_de_preparo': produto.modo_de_preparo,
                'preco': produto.preco,
                'estabelecimento_id': produto.estabelecimento.id,
                'categoria_id': produto.categoria.id,
                'inativo':produto.inativo
            })
        return jsonify(json_response)

    def get_produtos_estabelecimento_id_ativo(self, estabelecimento_id):
        produtos = self._buscar_produtos_estabelecimento_ativo(estabelecimento_id)
        json_response = []
        for produto in produtos:
            json_response.append({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'ingredientes': produto.ingredientes,
                'modo_de_preparo': produto.modo_de_preparo,
                'preco': produto.preco,
                'estabelecimento_id': produto.estabelecimento.id,
                'categoria_id': produto.categoria.id
            })
        return jsonify(json_response)        

    def get_produtos_categoria_id(self, categoria_id):
        produtos = self._buscar_produtos_categoria(categoria_id)
        json_response = []
        for produto in produtos:
            json_response.append({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'ingredientes': produto.ingredientes,
                'modo_de_preparo': produto.modo_de_preparo,
                'preco': produto.preco,
                'estabelecimento_id': produto.estabelecimento.id,
                'categoria_id': produto.categoria.id
            })
        return jsonify(json_response)
   
    def get_produtos_categoria_id_ativo(self, categoria_id):
        produtos = self._buscar_produtos_categoria_ativo(categoria_id)
        json_response = []
        for produto in produtos:
            json_response.append({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'ingredientes': produto.ingredientes,
                'modo_de_preparo': produto.modo_de_preparo,
                'preco': produto.preco,
                'estabelecimento_id': produto.estabelecimento.id,
                'categoria_id': produto.categoria.id
            })
        return jsonify(json_response)
    def get_produtos(self):
        produtos = self._listar_todos_produtos()
        json_response = []
        for produto in produtos:
            json_response.append({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'ingredientes': produto.ingredientes,
                'modo_de_preparo': produto.modo_de_preparo,
                'preco': produto.preco,
                'estabelecimento_id': produto.estabelecimento.id,
                'categoria_id': produto.categoria.id,
                'inativo' : produto.inativo
            })
        return jsonify(json_response)

    def get_produtos_ativos(self):
        produtos = self._listar_todos_produtos_ativos()
        json_response = []
        for produto in produtos:
            json_response.append({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'ingredientes': produto.ingredientes,
                'modo_de_preparo': produto.modo_de_preparo,
                'preco': produto.preco,
                'estabelecimento_id': produto.estabelecimento.id,
                'categoria_id': produto.categoria.id,
                'inativo' : produto.inativo
            })
        return jsonify(json_response)

    def put_produtos(self, request):
        
        id = request.json['id']
        nome = request.json['nome']
        descricao = request.json['descricao']
        ingredientes = request.json['ingredientes']
        modo_de_preparo = request.json['modo_de_preparo']
        preco = request.json['preco']
        estabelecimento_id = request.json['estabelecimento_id']
        categoria_id = request.json['categoria_id']
        inativo = request.json['inativo']

        produto = self._atualizar_produto(id, nome, descricao, ingredientes, modo_de_preparo, preco, estabelecimento_id, categoria_id, inativo)
        return jsonify(
            id=produto.id,
            nome=produto.nome,
            descricao=produto.descricao,
            ingredientes=produto.ingredientes,
            modo_de_preparo=produto.modo_de_preparo,
            preco=produto.preco,
            estabelecimento_id=produto.estabelecimento.id,
            categoria_id=produto.categoria.id
        )

    #
    # métodos internos
    #

    def _criar_produto(self, nome, descricao, ingredientes, modo_de_preparo, preco, estabelecimento_id, categoria_id,inativo):
        
        estabelecimento = Estabelecimento.query.filter_by(id=estabelecimento_id).first()
        
        categoria = Categoria.query.filter_by(id=categoria_id).first()

        if Produto.query.filter(Produto.nome == nome , Produto.estabelecimento_id == estabelecimento_id).count() > 0:
            raise Exception("Já existe um produto com o nome informado!")
        
        novo_produto = Produto(nome=nome, descricao=descricao, ingredientes=ingredientes,
                               modo_de_preparo=modo_de_preparo, preco=preco, estabelecimento=estabelecimento, categoria=categoria,inativo=inativo)
        
        db.session.add(novo_produto)
        db.session.commit()
        return novo_produto

    def _deletar_produto(self, id):
        produto = self._buscar_produto(id)
        db.session.delete(produto)
        db.session.commit()

    def _buscar_produto(self, id):
        return Produto.query.filter_by(id=id).first()

    def _buscar_produtos_estabelecimento(self, estabelecimento_id):
        return Produto.query.filter_by(estabelecimento_id=estabelecimento_id)
    
    def _buscar_produtos_estabelecimento_ativo(self, estabelecimento_id):
        return Produto.query.filter_by(estabelecimento_id=estabelecimento_id,inativo=False)
        
    def _buscar_produtos_categoria(self, categoria_id):
        return Produto.query.filter_by(categoria_id=categoria_id)

    def _buscar_produtos_categoria_ativo(self, categoria_id):
        return Produto.query.filter_by(categoria_id=categoria_id,inativo=False)

    def _atualizar_produto(self, id, nome, descricao, ingredientes, modo_de_preparo, preco, estabelecimento_id, categoria_id, inativo):

        produto = self._buscar_produto(id)

        if produto == None:
            raise Exception("Nenhum produto encontrado!")

        if Produto.query.filter(Produto.nome == nome , Produto.estabelecimento_id == estabelecimento_id , Produto.id != id).count() > 0:
            raise Exception("Já existe um produto com o nome informado!")

        
        estabelecimento = Estabelecimento.query.filter_by(id=estabelecimento_id).first()
        categoria = Categoria.query.filter_by(id=categoria_id).first()
        produto.nome = nome
        produto.descricao = descricao
        produto.ingredientes = ingredientes
        produto.modo_de_preparo = modo_de_preparo
        produto.preco = preco
        produto.estabelecimento = estabelecimento
        produto.inativo = str2bool(str(inativo).lower())
        produto.categoria = categoria
        
        db.session.add(produto)
        db.session.commit()
        return produto

    def _listar_todos_produtos(self):
        return Produto.query.all()
    
    def _listar_todos_produtos_ativos(self):
        return Produto.query.filter_by(inativo=False)
