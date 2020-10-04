export class Usuario {
  id:number
  login: string;
  senha: string;
  id_estabelecimento: number;
  isAdmin: boolean;

  constructor(login: string, senha: string, id_estabelecimento: number,isAdmin: boolean) {

    this.login = login;
    this.senha = senha;
    this.id_estabelecimento = id_estabelecimento;
    this.isAdmin = isAdmin;
  }
}
