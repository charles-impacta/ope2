import unittest
import string
import random
import requests

from base_test import BaseTest


class TestUsuarios(BaseTest):
    #
    # setUp e tearDown
    #

    @classmethod
    def setUpClass(self):
        self._url = self.url + '/usuarios/'
        self.id_estabelecimento = requests.post(self.url + '/estabelecimentos/' , json={
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'cnpj': ''.join(random.choice(string.digits) for _ in range(14))
        }).json()['id']

    @classmethod
    def tearDownClass(self):
        requests.delete(self.url + '/estabelecimentos/' + str(self.id_estabelecimento))

    def setUp(self):
        self.ids_usuarios_criados = []

    def tearDown(self):
        for id in self.ids_usuarios_criados:
            self._delete_usuarios(id)

    #
    # testes
    #
    def test_cria_usuario(self):
        # arrange
        data = self._test_data()

        # act
        r = self._post_usuarios(data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 2
        assert r_json['id'] > 0
        assert r_json['mensagem'] == 'Usuário criado com sucesso.'


    def test_atualiza_usuarios(self):
        # arrange
        data = self._test_data()
        id_usuario = self._post_usuarios(data).json()['id']

        put_data = self._test_data()

        # act
        r = requests.put(self._url + str(id_usuario), json=put_data)
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 3
        assert r_json['id'] > 0
        assert r_json['login'] == put_data['login']
        assert r_json['id_estabelecimento'] == put_data['id_estabelecimento']

    def test_deleta_usuario(self):
        # arrange
        data = self._test_data()
        id_usuario = self._post_usuarios(data).json()['id']

        # act
        r = requests.delete(self._url + str(id_usuario))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 1
        assert r_json['mensagem'] == 'Usuário deletado com sucesso.'

    def test_busca_usuario_por_id(self):
        # arrange
        data = self._test_data()
        id_usuario = self._post_usuarios(data).json()['id']

        # act
        r = requests.get(self._url + str(id_usuario))
        r_json = r.json()

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(r_json) == 3
        assert r_json['id'] > 0
        assert r_json['login'] == data['login']
        assert r_json['id_estabelecimento'] == data['id_estabelecimento']

    def test_busca_todos_usuarios(self):
        # arrange
        data_1 = self._test_data()
        id_usuario_1 = self._post_usuarios(data_1).json()['id']
        data_2 = self._test_data()
        id_usuario_2 = self._post_usuarios(data_2).json()['id']

        # act
        r = requests.get(self._url)
        r_json = r.json()

        usuario_1 = self._busca_usuario_na_lista(r_json, id_usuario_1)
        usuario_2 = self._busca_usuario_na_lista(r_json, id_usuario_2)

        # assert
        assert r.ok
        assert r.status_code == 200

        assert len(usuario_1) == 3
        assert usuario_1['id'] > 0
        assert usuario_1['login'] == data_1['login']
        assert usuario_1['id_estabelecimento'] == data_1['id_estabelecimento']

        assert len(usuario_1) == 3
        assert usuario_2['id'] > 0
        assert usuario_2['login'] == data_2['login']
        assert usuario_2['id_estabelecimento'] == data_2['id_estabelecimento']


    #
    # metodos de suporte
    #

    def _test_data(self):
        return {
            'login': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32)),
            'senha': ''.join(random.choice(string.digits) for _ in range(64)),
            'id_estabelecimento': self.id_estabelecimento
        }

    def _post_usuarios(self, data):
        response = requests.post(self._url , json=data)
        self.ids_usuarios_criados.append(response.json()['id'])
        return response

    def _delete_usuarios(self, id):
        requests.delete(self._url + str(id))

    def _busca_usuario_na_lista(self, lista, id):
        result = None
        for usuario in lista:
            if usuario['id'] == id:
                result = usuario
        return result
