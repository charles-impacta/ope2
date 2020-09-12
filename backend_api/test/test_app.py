import unittest

from ..app import app


class TestApp(unittest.TestCase):
    #
    # setUp e tearDown
    #

    def setUp(self):
        self.ids_estabelecimentos_criados = []
        self.client = app.app.test_client()

    def tearDown(self):
        for estabelecimento in self.ids_estabelecimentos_criados:
            self.client.delete('/estabelecimentos/' + str(estabelecimento))
        self.ids_estabelecimentos_criados = []


    #
    # testes
    #

    def test_cria_estabelecimento(self):
        # arrange
        json_data = {
            'nome': 'nome teste',
            'cnpj': '12345678901234'
        }
        
        # act
        response = self._cria_estabelecimento(json_data)
        
        # assert
        assert response.json['mensagem'] == 'Estabelecimento criado com sucesso.'

    def test_busca_estabelecimento(self):
        # arrange
        json_data = {
            'nome': 'nome teste',
            'cnpj': '12345678901234'
        }
        id_estabelecimento = self._cria_estabelecimento(json_data).json['id']

        # act
        response = self.client.get('/estabelecimentos/' + str(id_estabelecimento))

        # assert
        assert response.json['id'] == id_estabelecimento
        assert response.json['nome'] == json_data['nome']
        assert response.json['cnpj'] == json_data['cnpj']

    #
    # metodos de suporte
    #

    def _cria_estabelecimento(self, json_data):
        response = self.client.post('/estabelecimentos/', json=json_data)
        self.ids_estabelecimentos_criados.append(response.json['id'])
        return response
