import unittest

from ..app import app

class TestApp(unittest.TestCase):
    # setUp e tearDown
    def setUp(self):
        self.client = app.app.test_client()

    # testes

    def test_ola_mundo(self):
        response = self.client.get('/')
        assert response.json['mensagem'] == 'Ola mundo!'

    # metodos de suporte
