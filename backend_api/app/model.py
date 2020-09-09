from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), unique=True, index=True)
    senha = db.Column(db.String(64))
    estabelecimento_id = db.Column(db.Integer, db.ForeignKey('estabelecimentos.id'))

    def __repr__(self):
        return '<Usuario %r>' % self.login

class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)
    cnpj = db.Column(db.String(14), unique=True)
    usuarios = db.relationship('Usuario', backref='estabelecimento')

    def __repr__(self):
        return '<Estabelecimento %r>' % self.nome
