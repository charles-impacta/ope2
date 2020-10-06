import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Constants } from 'src/app/shared/constants';
import { Categoria } from '../models/categoria.model';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {

  constructor(private httpClient: HttpClient) { }

  list(): Observable<Categoria[]> {

    return this.httpClient.get<Categoria[]>(`${Constants.hostApi}/categorias/`);
  }

  listActive(): Observable<Categoria[]> {

    return this.httpClient.get<Categoria[]>(`${Constants.hostApi}/categorias-ativas/`);
  }

  get(categoriaId: string): Observable<Categoria> {
    return this.httpClient.get<Categoria>(`${Constants.hostApi}/categorias/${categoriaId}`);
  }

  post(model: Categoria) {
    return this.httpClient.post(`${Constants.hostApi}/categorias/`, model);
  }

  put(model: Categoria) {
    return this.httpClient.put(`${Constants.hostApi}/categorias/`, model);
  }
}
