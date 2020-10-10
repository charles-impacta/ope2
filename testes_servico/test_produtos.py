import unittest
import string
import random
import requests

from base_test import BaseTest


class TestProdutos(BaseTest):
    #
    # setUp e tearDown
    #

    @classmethod
    def setUpClass(self):
        self._url = self.url + '/produtos/'
        self.id_estabelecimento = requests.post(self.url + '/estabelecimentos/' , json={
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'cnpj': ''.join(random.choice(string.digits) for _ in range(14))
        }).json()['id']
        self.id_categoria = requests.post(self.url + '/categorias/' , json={
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'inativo': False
        }).json()['id']

    @classmethod
    def tearDownClass(self):
        requests.delete(self.url + '/estabelecimentos/' + str(self.id_estabelecimento))
        requests.delete(self.url + '/categorias/' + str(self.id_categoria))

    def setUp(self):
        self.ids_produtos_criados = []

    def tearDown(self):
        for id in self.ids_produtos_criados:
            self._delete_produtos(id)

    #
    # testes
    #
    def test_cria_produto(self):
        # arrange
        data = self._test_data()

        # act
        r = self._post_produtos(data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 2
        assert r_json['id'] > 0
        assert r_json['mensagem'] == 'Produto criado com sucesso.'

    def test_atualiza_produto(self):
        # arrange
        data = self._test_data()
        id_produto = self._post_produtos(data).json()['id']

        put_data = self._test_data()
        put_data['id'] = id_produto

        # act
        r = requests.put(self._url, json=put_data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200
        assert len(r_json) == 8
        self._assert_response(r_json, put_data)

    def test_deleta_produto(self):
        # arrange
        data = self._test_data()
        id_produto = self._post_produtos(data).json()['id']

        # act
        r = requests.delete(self._url + str(id_produto))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 1
        assert r_json['mensagem'] == 'Produto deletado com sucesso.'

    def test_busca_produto_por_id(self):
        # arrange
        data = self._test_data()
        id_produto = self._post_produtos(data).json()['id']

        # act
        r = requests.get(self._url + str(id_produto))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 9
        self._assert_response(r_json, data)

    def test_busca_todos_produtos(self):
        # arrange
        data_1 = self._test_data()
        id_produto_1 = self._post_produtos(data_1).json()['id']
        data_2 = self._test_data()
        id_produto_2 = self._post_produtos(data_2).json()['id']

        # act
        r = requests.get(self._url)
        r_json = r.json()

        produto_1 = self._busca_produto_na_lista(r_json, id_produto_1)
        produto_2 = self._busca_produto_na_lista(r_json, id_produto_2)

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(produto_1) == 9
        self._assert_response(produto_1, data_1)

        assert len(produto_2) == 9
        self._assert_response(produto_2, data_2)


    #
    # metodos de suporte
    #

    def _assert_response(self, r_json, data):
        assert r_json['id'] > 0
        assert r_json['nome'] == data['nome']
        assert r_json['descricao'] == data['descricao']
        assert r_json['ingredientes'] == data['ingredientes']
        assert r_json['modo_de_preparo'] == data['modo_de_preparo']
        assert r_json['preco'] == data['preco']
        assert r_json['estabelecimento_id'] == data['estabelecimento_id']
        assert r_json['categoria_id'] == data['categoria_id']

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

    def _post_produtos(self, data):
        response = requests.post(self._url , json=data)
        self.ids_produtos_criados.append(response.json()['id'])
        return response

    def _delete_produtos(self, id):
        requests.delete(self._url + str(id))

    def _busca_produto_na_lista(self, lista, id):
        result = None
        for produto in lista:
            if produto['id'] == id:
                result = produto
        return result
