import unittest
import string
import random
import requests

from base_test import BaseTest


class TestEstabelecimentos(BaseTest):
    #
    # setUp e tearDown
    #

    @classmethod
    def setUpClass(self):
        self._url = self.url + '/estabelecimentos/'

    def setUp(self):
        self.ids_estabelecimentos_criados = []

    def tearDown(self):
        for id in self.ids_estabelecimentos_criados:
            self._delete_estabelecimentos(id)

    #
    # testes
    #
    def test_cria_estabelecimento(self):
        # arrange
        data = self._test_data()

        # act
        r = self._post_estabelecimentos(data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 2
        assert r_json['id'] > 0
        assert r_json['mensagem'] == 'Estabelecimento criado com sucesso.'

    def test_atualiza_estabelecimento(self):
        # arrange
        data = self._test_data()
        id_estabelecimento = self._post_estabelecimentos(data).json()['id']

        put_data = self._test_data()

        # act
        r = requests.put(self._url + str(id_estabelecimento), json=put_data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 3
        assert r_json['id'] > 0
        assert r_json['cnpj'] == put_data['cnpj']
        assert r_json['nome'] == put_data['nome']

    def test_deleta_estabelecimento(self):
        # arrange
        data = self._test_data()
        id_estabelecimento = self._post_estabelecimentos(data).json()['id']

        # act
        r = requests.delete(self._url + str(id_estabelecimento))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 1
        assert r_json['mensagem'] == 'Estabelecimento deletado com sucesso.'

    def test_busca_estabelecimento_por_id(self):
        # arrange
        data = self._test_data()
        id_estabelecimento = self._post_estabelecimentos(data).json()['id']

        # act
        r = requests.get(self._url + str(id_estabelecimento))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 3
        assert r_json['id'] > 0
        assert r_json['cnpj'] == data['cnpj']
        assert r_json['nome'] == data['nome']

    def test_busca_todos_estabelecimentos(self):
        # arrange
        data_1 = self._test_data()
        id_estabelecimento_1 = self._post_estabelecimentos(data_1).json()['id']
        data_2 = self._test_data()
        id_estabelecimento_2 = self._post_estabelecimentos(data_2).json()['id']

        # act
        r = requests.get(self._url)
        r_json = r.json()

        estabelecimento_1 = self._busca_etabelecimento_na_lista(r_json, id_estabelecimento_1)
        estabelecimento_2 = self._busca_etabelecimento_na_lista(r_json, id_estabelecimento_2)

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(estabelecimento_1) == 3
        assert estabelecimento_1['id'] > 0
        assert estabelecimento_1['cnpj'] == data_1['cnpj']
        assert estabelecimento_1['nome'] == data_1['nome']

        assert len(estabelecimento_2) == 3
        assert estabelecimento_2['id'] > 0
        assert estabelecimento_2['cnpj'] == data_2['cnpj']
        assert estabelecimento_2['nome'] == data_2['nome']


    #
    # metodos de suporte
    #

    def _test_data(self):
        return {
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'cnpj': ''.join(random.choice(string.digits) for _ in range(14))
        }

    def _post_estabelecimentos(self, data):
        response = requests.post(self._url , json=data)
        self.ids_estabelecimentos_criados.append(response.json()['id'])
        return response

    def _delete_estabelecimentos(self, id):
        requests.delete(self._url + str(id))

    def _busca_etabelecimento_na_lista(self, lista, id):
        result = None
        for estabelecimento in lista:
            if estabelecimento['id'] == id:
                result = estabelecimento
        return result
