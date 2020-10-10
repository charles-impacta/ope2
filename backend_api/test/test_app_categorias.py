import unittest, os, sys, random, string

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from app import app


class TestAppCategorias(unittest.TestCase):
    #
    # setUp e tearDown
    #

    def setUp(self):
        self.ids_categorias_criadas = []
        self.client = app.app.test_client()

    def tearDown(self):
        for categoria in self.ids_categorias_criadas:
            self.client.delete('/categorias/' + str(categoria))
        self.ids_categorias_criadas = []


    #
    # testes
    #

    def test_cria_categoria(self):
        # arrange
        json_data = self._test_data()

        # act
        response = self._cria_categoria(json_data)

        # assert
        assert response.status_code == 200
        assert response.json['mensagem'] == 'Categoria criada com sucesso.'

    def test_categoria_nome_repetido(self):
        # arrange
        json_data = self._test_data()
        self._cria_categoria(json_data)

        # act
        response = self.client.post('/categorias/', json=json_data)

        # assert
        assert response.status_code == 400

    def test_deletar_categoria(self):
        # arrange
        json_data = self._test_data()
        id_categoria = self.client.post('/categorias/', json=json_data).json['id']

        # act
        response = self.client.delete('categorias/' + str(id_categoria))

        # assert
        assert response.status_code == 200
        assert response.json['mensagem'] == 'Categoria deletada com sucesso.'

    def test_atualizar_categoria(self):
        # arrange
        json_data = self._test_data()
        id_categoria = self._cria_categoria(json_data).json['id']
        novo_json_data = self._test_data()
        novo_json_data['id'] = id_categoria

        # act
        response = self.client.put('categorias/', json=novo_json_data)

        # assert
        assert response.status_code == 200
        assert response.json['id'] == id_categoria
        assert response.json['nome'] == novo_json_data['nome']

    def test_atualizar_categoria_nome_repetido(self):
        # arrange
        json_data = self._test_data()
        id_categoria = self._cria_categoria(json_data).json['id']
        novo_json_data = self._test_data()
        self._cria_categoria(novo_json_data).json['id']
        novo_json_data['id'] = id_categoria

        # act
        response = self.client.put('categorias/', json=novo_json_data)

        # assert
        assert response.status_code == 400

    def test_busca_categoria(self):
        # arrange
        json_data = self._test_data()
        id_categoria = self._cria_categoria(json_data).json['id']

        # act
        response = self.client.get('categorias/' + str(id_categoria))

        # assert
        assert response.status_code == 200
        assert response.json['nome'] == json_data['nome']

    def test_lista_todas_categorias(self):
        # arrange
        json_data1 = self._test_data()
        id_categoria1 = self._cria_categoria(json_data1).json['id']
        json_data2 = self._test_data()
        id_categoria2 = self._cria_categoria(json_data2).json['id']

        # act
        response = self.client.get('categorias/')

        # assert
        assert response.status_code == 200

        for categoria in response.json:
            if categoria['id'] == id_categoria1:
                categoria1 = categoria
            if categoria['id'] == id_categoria2:
                categoria2 = categoria

        assert categoria1['nome'] == json_data1['nome']
        assert categoria2['nome'] == json_data2['nome']

    def test_lista_categorias_ativas(self):
        # arrange
        json_data1 = self._test_data()
        id_categoria1 = self._cria_categoria(json_data1).json['id']
        json_data2 = self._test_data()
        json_data2['inativo'] = True
        id_categoria2 = self._cria_categoria(json_data2).json['id']

        # act
        response = self.client.get('categorias-ativas/')

        # assert
        categoria1 = False
        categoria2 = False
        for categoria in response.json:
            if categoria['id'] == id_categoria1:
                categoria1 = True
            if categoria['id'] == id_categoria2:
                categoria2 = True

        assert categoria1
        assert not categoria2

    #
    # metodos de suporte
    #

    def _cria_categoria(self, json_data):
        response = self.client.post('/categorias/', json=json_data)
        self.ids_categorias_criadas.append(response.json['id'])
        return response

    def _test_data(self):
        return {
            'nome': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64)),
            'inativo': False
        }
