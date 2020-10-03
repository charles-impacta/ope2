from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), unique=True, index=True)
    senha = db.Column(db.String(64))
    isAdmin = db.Column(db.Boolean)
    estabelecimento_id = db.Column(db.Integer, db.ForeignKey('estabelecimentos.id'))

    def __repr__(self):
        return '<Usuario %r>' % self.login


class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)
    cnpj = db.Column(db.String(14), unique=True)

    usuarios = db.relationship('Usuario', backref='estabelecimento')
    produtos = db.relationship('Produto', backref='estabelecimento')

    def __repr__(self):
        return '<Estabelecimento %r>' % self.nome


class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)
    descricao = db.Column(db.String(256))
    ingredientes = db.Column(db.String(512))
    modo_de_preparo = db.Column(db.String(512))
    preco = db.Column(db.Float)

    estabelecimento_id = db.Column(db.Integer, db.ForeignKey('estabelecimentos.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))

    def __repr__(self):
        return '<Produto %r>' % self.nome


class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)

    produtos = db.relationship('Produto', backref='categoria')

    def __repr__(self):
        return '<Categoria %r>' % self.nome
