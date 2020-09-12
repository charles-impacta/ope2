from .model import db, Estabelecimento

class ControllerEstabelecimento():
    def criar_estabelecimento(self, nome, cnpj):
        novo_estabelecimento = Estabelecimento(nome=nome, cnpj=cnpj)
        db.session.add(novo_estabelecimento)
        db.session.commit()
        return novo_estabelecimento.id

    def deletar_estabelecimento(self, id):
        estabelecimento = Estabelecimento.query.filter_by(id=id).first()
        db.session.delete(estabelecimento)
        db.session.commit()

    def buscar_estabelecimento(self, id):
        return Estabelecimento.query.filter_by(id=id).first()

    def atualizar_estabelecimento(self, id, nome, cnpj):
        estabelecimento = Estabelecimento.query.filter_by(id=id).first()
        estabelecimento.nome = nome
        estabelecimento.cnpj = cnpj
        db.session.add(estabelecimento)
        db.session.commit()
