import { EstabelecimentoResult } from './../../app/shared/services-proxies';
import { Constants } from './../../app/shared/constants';
import { Estabelecimento } from './../models/estabelecimento.model';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EstabelecimentoService {

  constructor(private httpClient: HttpClient) { }

  post(estabelecimento: Estabelecimento): Observable<EstabelecimentoResult> {

    return this.httpClient.post<EstabelecimentoResult>(`${Constants.hostApi}/estabelecimentos/`, estabelecimento, { headers: { 'Content-Type': 'application/json' } });

  }

  list(): Observable<Estabelecimento[]> {
    return this.httpClient.get<Estabelecimento[]>(`${Constants.hostApi}/estabelecimentos/`);
  }

  get(estabelecimentoId: any) :Observable<Estabelecimento> {
    return this.httpClient.get<Estabelecimento>(`${Constants.hostApi}/estabelecimentos/${estabelecimentoId}`);
  }


}
