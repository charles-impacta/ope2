import unittest, os, sys, random, string

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from app import app


class TestAppProdutos(unittest.TestCase):
    #
    # setUp e tearDown
    #

    @classmethod
    def setUpClass(self):
        self.client = app.app.test_client()

        estabelecimento = self.client.post('/estabelecimentos/', json={
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'cnpj': ''.join(random.choice(string.digits) for _ in range(14))
        })
        self.id_estabelecimento = estabelecimento.json['id']

        categoria = self.client.post('/categorias/', json={
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'inativo': False
        })
        self.id_categoria = categoria.json['id']

    @classmethod
    def tearDownClass(self):
        self.client.delete('/estabelecimentos/' + str(self.id_estabelecimento))
        self.client.delete('/categorias/' + str(self.id_categoria))

    def setUp(self):
        self.ids_produtos_criados = []

    def tearDown(self):
        for produto in self.ids_produtos_criados:
            self.client.delete('/produtos/' + str(produto))
        self.ids_produtos_criados = []


    #
    # testes
    #

    def test_cria_produto(self):
        # arrange
        json_data = self._test_data()

        # act
        response = self._cria_produto(json_data)

        # assert
        assert response.status_code == 200
        assert response.json['mensagem'] == 'Produto criado com sucesso.'

    def test_cria_produto_nome_repetido(self):
        # arrange
        json_data = self._test_data()
        self._cria_produto(json_data)

        # act
        response = self.client.post('/produtos/', json=json_data)

        # assert
        assert response.status_code == 400

    def test_atualiza_produto(self):
        # arrange
        json_data = self._test_data()
        id_produto = self._cria_produto(json_data).json['id']
        novo_json_data = self._test_data()
        novo_json_data['id'] = id_produto

        # act
        response = self.client.put('/produtos/', json=novo_json_data)

        # assert
        assert response.status_code == 200
        self._assert_produto(novo_json_data, response.json)

    def test_atualiza_produto_nome_repetido(self):
        # arrange
        json_data = self._test_data()
        id_produto = self._cria_produto(json_data).json['id']
        novo_json_data = self._test_data()
        self._cria_produto(novo_json_data).json['id']
        novo_json_data['id'] = id_produto

        # act
        response = self.client.put('/produtos/', json=novo_json_data)

        # assert
        assert response.status_code == 400

    def test_deleta_produto(self):
        # arrange
        json_data = self._test_data()
        id_produto = self.client.post('/produtos/', json=json_data).json['id']

        # act
        response = self.client.delete('/produtos/' + str(id_produto))

        # assert
        assert response.status_code == 200
        assert response.json['mensagem'] == 'Produto deletado com sucesso.'

    def test_busca_produto_por_id(self):
        # arrange
        json_data = self._test_data()
        id_produto = self._cria_produto(json_data).json['id']

        # act
        response = self.client.get('/produtos/' + str(id_produto))

        # assert
        assert response.status_code == 200
        self._assert_produto(json_data, response.json)

    def test_busca_produtos_por_estabelecimento(self):
        # arrange
        json_data1 = self._test_data()
        id_produto1 = self._cria_produto(json_data1).json['id']
        json_data2 = self._test_data()
        id_produto2 = self._cria_produto(json_data2).json['id']

        # act
        response = self.client.get('/produtos-estabelecimento/' + str(self.id_estabelecimento))

        # assert
        assert response.status_code == 200
        for produto in response.json:
            if produto['id'] == id_produto1:
                self._assert_produto(json_data1, produto)
            if produto['id'] == id_produto2:
                self._assert_produto(json_data2, produto)

    def test_busca_produtos_ativos_por_estabelecimento(self):
        # arrange
        json_data1 = self._test_data()
        id_produto1 = self._cria_produto(json_data1).json['id']
        json_data2 = self._test_data()
        json_data2['inativo'] = True
        id_produto2 = self._cria_produto(json_data2).json['id']

        # act
        response = self.client.get('/produtos-estabelecimento-ativo/' + str(self.id_estabelecimento))

        # assert
        assert response.status_code == 200
        produto2 = False
        for produto in response.json:
            if produto['id'] == id_produto1:
                self._assert_produto(json_data1, produto)
                produto1 = True
            if produto['id'] == id_produto2:
                produto2 = True
        assert produto1
        assert not produto2

    def test_busca_produtos_ativos_por_categoria(self):
        # arrange
        json_data1 = self._test_data()
        id_produto1 = self._cria_produto(json_data1).json['id']
        json_data2 = self._test_data()
        json_data2['inativo'] = True
        id_produto2 = self._cria_produto(json_data2).json['id']

        # act
        response = self.client.get('/produtos-categoria-ativo/' + str(self.id_categoria))

        # assert
        assert response.status_code == 200
        produto1 = False
        produto2 = False
        for produto in response.json:
            if produto['id'] == id_produto1:
                self._assert_produto(json_data1, produto)
                produto1 = True
            if produto['id'] == id_produto2:
                produto2 = True
        assert produto1
        assert not produto2

    def test_busca_produtos_por_categoria(self):
        # arrange
        json_data1 = self._test_data()
        id_produto1 = self._cria_produto(json_data1).json['id']
        json_data2 = self._test_data()
        id_produto2 = self._cria_produto(json_data2).json['id']

        # act
        response = self.client.get('/produtos-categoria/' + str(self.id_categoria))

        # assert
        assert response.status_code == 200
        for produto in response.json:
            if produto['id'] == id_produto1:
                self._assert_produto(json_data1, produto)
            if produto['id'] == id_produto2:
                self._assert_produto(json_data2, produto)

    def test_lista_produtos(self):
        # arrange
        json_data1 = self._test_data()
        id_produto1 = self._cria_produto(json_data1).json['id']
        json_data2 = self._test_data()
        id_produto2 = self._cria_produto(json_data2).json['id']

        # act
        response = self.client.get('/produtos/')

        # assert
        assert response.status_code == 200
        for produto in response.json:
            if produto['id'] == id_produto1:
                self._assert_produto(json_data1, produto)
            if produto['id'] == id_produto2:
                self._assert_produto(json_data2, produto)

    def test_lista_produtos_ativos(self):
        # arrange
        json_data1 = self._test_data()
        id_produto1 = self._cria_produto(json_data1).json['id']
        json_data2 = self._test_data()
        json_data2['inativo'] = True
        id_produto2 = self._cria_produto(json_data2).json['id']

        # act
        response = self.client.get('/produtos-ativos/')

        # assert
        assert response.status_code == 200
        produto1 = False
        produto2 = False
        for produto in response.json:
            if produto['id'] == id_produto1:
                self._assert_produto(json_data1, produto)
                produto1 = True
            if produto['id'] == id_produto2:
                produto2 = True
        assert produto1
        assert not produto2

    #
    # metodos de suporte
    #

    def _assert_produto(self, json_data, response_json):
        assert response_json['descricao'] == json_data['descricao']
        assert response_json['ingredientes'] == json_data['ingredientes']
        assert response_json['modo_de_preparo'] == json_data['modo_de_preparo']
        assert response_json['nome'] == json_data['nome']
        assert response_json['preco'] == json_data['preco']
        assert response_json['estabelecimento_id'] == json_data['estabelecimento_id']
        assert response_json['categoria_id'] == json_data['categoria_id']

    def _cria_produto(self, json_data):
        response = self.client.post('/produtos/', json=json_data)
        self.ids_produtos_criados.append(response.json['id'])
        return response

    def _test_data(self):
        return {
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'descricao': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(256)),
            'ingredientes': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(512)),
            'modo_de_preparo': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(512)),
            'preco': 29.99,
            'inativo': False,
            'estabelecimento_id': self.id_estabelecimento,
            'categoria_id': self.id_categoria
        }
