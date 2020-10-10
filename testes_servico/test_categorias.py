import unittest
import string
import random
import requests

from base_test import BaseTest


class TestCategorias(BaseTest):
    #
    # setUp e tearDown
    #

    @classmethod
    def setUpClass(self):
        self._url = self.url + '/categorias/'

    def setUp(self):
        self.ids_categorias_criadas = []

    def tearDown(self):
        for id in self.ids_categorias_criadas:
            self._delete_categorias(id)

    #
    # testes
    #
    def test_cria_categoria(self):
        # arrange
        data = self._test_data()

        # act
        r = self._post_categorias(data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 2
        assert r_json['id'] > 0
        assert r_json['mensagem'] == 'Categoria criada com sucesso.'

    def test_atualiza_categoria(self):
        # arrange
        data = self._test_data()
        id_categoria = self._post_categorias(data).json()['id']

        put_data = self._test_data()
        put_data['id'] = id_categoria

        # act
        r = requests.put(self._url, json=put_data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 2
        assert r_json['id'] > 0
        assert r_json['nome'] == put_data['nome']

    def test_deleta_categoria(self):
        # arrange
        data = self._test_data()
        id_categoria = self._post_categorias(data).json()['id']

        # act
        r = requests.delete(self._url + str(id_categoria))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 1
        assert r_json['mensagem'] == 'Categoria deletada com sucesso.'

    def test_busca_categoria_por_id(self):
        # arrange
        data = self._test_data()
        id_categoria = self._post_categorias(data).json()['id']

        # act
        r = requests.get(self._url + str(id_categoria))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 3
        assert r_json['id'] > 0
        assert r_json['inativo'] == data['inativo']
        assert r_json['nome'] == data['nome']

    def test_busca_todas_categorias(self):
        # arrange
        data_1 = self._test_data()
        id_categoria_1 = self._post_categorias(data_1).json()['id']
        data_2 = self._test_data()
        id_categoria_2 = self._post_categorias(data_2).json()['id']

        # act
        r = requests.get(self._url)
        r_json = r.json()

        categoria_1 = self._busca_categoria_na_lista(r_json, id_categoria_1)
        categoria_2 = self._busca_categoria_na_lista(r_json, id_categoria_2)

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(categoria_1) == 3
        assert categoria_1['id'] > 0
        assert categoria_1['inativo'] == data_1['inativo']
        assert categoria_1['nome'] == data_1['nome']

        assert len(categoria_2) == 3
        assert categoria_2['id'] > 0
        assert categoria_2['inativo'] == data_2['inativo']
        assert categoria_2['nome'] == data_2['nome']


    #
    # metodos de suporte
    #

    def _test_data(self):
        return {
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'inativo': False
        }

    def _post_categorias(self, data):
        response = requests.post(self._url , json=data)
        self.ids_categorias_criadas.append(response.json()['id'])
        return response

    def _delete_categorias(self, id):
        requests.delete(self._url + str(id))

    def _busca_categoria_na_lista(self, lista, id):
        result = None
        for categoria in lista:
            if categoria['id'] == id:
                result = categoria
        return result
