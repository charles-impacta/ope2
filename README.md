# OPE2 - Grupo Impactados2020

## Rodando o projeto na sua máquina

### Faça o checkout da branch correta
``` bash
ope2$ git checkout backend
```

### Criar e ativar o virtualenv
``` bash
ope2$ python -m venv venv
ope2$ source venv/bin/activate
```

### Instalar as dependências
``` bash
(venv) ope2$ pip install -r requirements.txt
```

### Criar o banco de dados SQLite
``` bash
(venv) ope2$ flask shell
>>> from backend_api.app.model import db
>>> db.create_all()
>>> quit()
```

### Rodar os testes
``` bash
(venv) ope2$ python -m unittest discover
```

### Iniciar o Flask em modo Debug
``` bash
(venv) ope2$ export FLASK_APP=backend_api/app/app.py
(venv) ope2$ export FLASK_DEBUG=1
(venv) ope2$ flask run
```

## Documentação da API

### Estabelecimentos
``` bash
# Criar um estabelecimento
POST /estabelecimentos
{
    'nome': '<nome>',
    'cnpj': '<cnpj>'
}

RESPOSTA
{
    'mensagem': 'Estabelecimento criado com sucesso.',
    'id': '<id>'
}
```
``` bash
# Deletar um estabelecimento
DELETE /estabelecimentos/<id_estabelecimento>

RESPOSTA
{
    'mensagem': 'Estabelecimento deletado com sucesso.'
}
```
``` bash
# Listar todos estabelecimentos
GET /estabelecimentos/

RESPOSTA
[{
    'id': '<id>',
    'nome': '<nome>',
    'cnpj': '<cnpj>'
},
{
    'id': '<id>',
    'nome': '<nome>',
    'cnpj': '<cnpj>'
}, ...
]
```
``` bash
# Buscar um estabelecimento
GET /estabelecimentos/<id_estabelecimento>

RESPOSTA
{
    'id': '<id>',
    'nome': '<nome>',
    'cnpj': '<cnpj>'
}
```
``` bash
# Atualizar um estabelecimento
PUT /estabelecimentos/<id_estabelecimento>
{
    'nome': '<nome>',
    'cnpj': '<cnpj>'
}

RESPOSTA
{
    'id': '<id>',
    'nome': '<nome>',
    'cnpj': '<cnpj>'
}
```
