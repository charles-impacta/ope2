import unittest

from ..app import app


class TestAppUsuarios(unittest.TestCase):
    #
    # setUp e tearDown
    #

    @classmethod
    def setUpClass(self):
        self.client = app.app.test_client()
        self.id_estabelecimento = self.client.post('/estabelecimentos/', json={
            'nome': 'nome teste',
            'cnpj': '12345678901234'
        }).json['id']

    @classmethod
    def tearDownClass(self):
        self.client.delete('/estabelecimentos/' + str(self.id_estabelecimento))

    def setUp(self):
        self.ids_usuarios_criados = []

    def tearDown(self):
        for id_usuario in self.ids_usuarios_criados:
            self.client.delete('/usuarios/' + str(id_usuario))
        self.ids_usuarios_criados = []

    #
    # testes
    #

    def test_cria_usuario(self):
        # arrange
        json_data = {
            'login': 'login teste',
            'senha': 'senha teste',
            'id_estabelecimento': self.id_estabelecimento
        }

        #act
        response = self._cria_usuario(json_data)

        # assert
        assert response.json['mensagem'] == u'Usuário criado com sucesso.'
    #
    # metodos de suporte
    #

    def _cria_usuario(self, json_data):
        response = self.client.post('/usuarios/', json=json_data)
        self.ids_usuarios_criados.append(response.json['id'])
        return response
