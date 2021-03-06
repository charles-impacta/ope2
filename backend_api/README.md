# OPE2 - Grupo Impactados2020

## Rodando o projeto na sua máquina

### Faça o checkout da branch correta
``` bash
ope2$ git checkout backend
```

### Criar e ativar o virtualenv
``` bash
# No Linux/Mac
ope2$ python -m venv venv
ope2$ source venv/bin/activate
```
``` bash
# No Windows
ope2$ python -m venv venv
ope2$ venv\Scripts\activate.bat
```

### Instalar as dependências
``` bash
(venv) ope2$ pip install -r requirements.txt
```

### Criar as variáveis de ambiente

A variável FLASK_DEBUG só é necessária para rodar o projeto em modo debug. Isso é bastante útil durante o desenvolvimento já que assim o Flask reinicia sozinho sempre que houver alteração no código.

``` bash
# No Linux/Mac
(venv) ope2$ export FLASK_APP=backend_api/app/app.py
(venv) ope2$ export FLASK_DEBUG=1
```
No Windows, crie as variáveis utilizadno as configurações do sistema:
1. FLASK_APP = <caminho completo até o repositório>\backend_api\app\app.py
1. FLASK_DEBUG = 1

### Criar o banco de dados SQLite
``` bash
(venv) ope2$ flask shell
>>> from backend_api.app.model import db
>>> db.create_all()
>>> quit()
```

### Rodar os testes
``` bash
(venv) ope2$ python -m unittest discover backend_api/
```

### Iniciar o Flask
``` bash
(venv) ope2$ flask run
```

## Documentação da API

### Estabelecimentos
``` bash
# Criar um estabelecimento
POST /estabelecimentos/
{
    "nome": "<nome>",
    "cnpj": "<cnpj>"
}

RESPOSTA
{
    "mensagem": "Estabelecimento criado com sucesso.",
    "id": "<id>"
}
```
``` bash
# Deletar um estabelecimento
DELETE /estabelecimentos/<id_estabelecimento>

RESPOSTA
{
    "mensagem": "Estabelecimento deletado com sucesso."
}
```
``` bash
# Listar todos estabelecimentos
GET /estabelecimentos/

RESPOSTA
[{
    "id": "<id>",
    "nome": "<nome>",
    "cnpj": "<cnpj>"
},
{
    "id": "<id>",
    "nome": "<nome>",
    "cnpj": "<cnpj>"
}, ...
]
```
``` bash
# Buscar um estabelecimento
GET /estabelecimentos/<id_estabelecimento>

RESPOSTA
{
    "id": "<id>",
    "nome": "<nome>",
    "cnpj": "<cnpj>"
}
```
``` bash
# Atualizar um estabelecimento
PUT /estabelecimentos/<id_estabelecimento>
{
    "nome": "<nome>",
    "cnpj": "<cnpj>"
}

RESPOSTA
{
    "id": "<id>",
    "nome": "<nome>",
    "cnpj": "<cnpj>"
}
```

### Usuários
``` bash
# Criar um usuário
POST /usuarios/
{
    "login": "<login>",
    "senha": "<senha>",
    "id_estabelecimento": <id_estabelecimento>
}

RESPOSTA
{
    "mensagem": "Usuário criado com sucesso.",
    "id": "<id>"
}
```
``` bash
# Deletar um usuário
DELETE /usuarios/<id_usuario>

RESPOSTA
{
    "mensagem": "Usuário deletado com sucesso."
}
```
``` bash
# Listar todos usuários
GET /usuarios/

RESPOSTA
[{
    "id": "<id>",
    "id_estabelecimento": "<id_estabelecimento>",
    "login": "<login>"
},
{
    "id": "<id>",
    "id_estabelecimento": "<id_estabelecimento>",
    "login": "<login>"
}, ...
]
```
``` bash
# Buscar um usuário
GET /usuarios/<id_usuario>

RESPOSTA
{
    "id": "<id>",
    "id_estabelecimento": "<id_estabelecimento>",
    "login": "<login>"
}
```
``` bash
# Atualizar um usuário
PUT /usuarios/<id_usuario>
{
    "login": "<login>",
    "senha": "<senha>",
    "id_estabelecimento": <id_estabelecimento>
}

RESPOSTA
{
    "id": "<id>",
    "id_estabelecimento": "<id_estabelecimento>",
    "login": "<login>"
}
```
``` bash
# Realizar login do usuário
POST /usuarios/login
{
    "login": "<login>",
    "senha": "<senha>"
}

RESPOSTA
{
    "mensagem": "Login efetuado com sucesso."
}
OU
{
    "mensagem": "Login inválido."
}
```
