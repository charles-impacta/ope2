import unittest
import string
import random
import requests

from .base_test import BaseTest


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
