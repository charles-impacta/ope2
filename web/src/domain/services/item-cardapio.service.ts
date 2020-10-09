import { ItemCardapio } from './../models/item-cardapio.model';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Constants } from 'src/app/shared/constants';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ItemCardapioService {

  constructor(private httpClient: HttpClient) { }

  list(): Observable<ItemCardapio[]> {
    return this.httpClient.get<ItemCardapio[]>(`${Constants.hostApi}/produtos`);
  }

  listAtivos(): Observable<ItemCardapio[]> {
    return this.httpClient.get<ItemCardapio[]>(`${Constants.hostApi}/produtos-ativos`);
  }

  get(itemCardapioId: any): Observable<ItemCardapio> {

    return this.httpClient.get<ItemCardapio>(`${Constants.hostApi}/produtos/${itemCardapioId}`);
  }

  getByCategoria(categoriaId: any): Observable<ItemCardapio[]> {

    return this.httpClient.get<ItemCardapio[]>(`${Constants.hostApi}/produtos-categoria/${categoriaId}`);
  }

  getByCategoriaAtivo(categoriaId: any): Observable<ItemCardapio[]> {

    return this.httpClient.get<ItemCardapio[]>(`${Constants.hostApi}/produtos-categoria-ativo/${categoriaId}`);
  }



  getByEstabelecimento(estabelecimentoId: any): Observable<ItemCardapio[]> {

    return this.httpClient.get<ItemCardapio[]>(`${Constants.hostApi}/produtos-estabelecimento/${estabelecimentoId}`);
  }

  getByEstabelecimentoAtivo(estabelecimentoId: any): Observable<ItemCardapio[]> {

    return this.httpClient.get<ItemCardapio[]>(`${Constants.hostApi}/produtos-estabelecimento-ativo/${estabelecimentoId}`);
  }


  post(model: ItemCardapio) {

    return this.httpClient.post(`${Constants.hostApi}/produtos/`, model);
  }

  put(model: ItemCardapio) {

    return this.httpClient.put(`${Constants.hostApi}/produtos/`, model);

  }
}
