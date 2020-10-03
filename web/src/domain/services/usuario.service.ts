import { Usuario } from './../models/usuario.model';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Constants } from 'src/app/shared/constants';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private httpClient: HttpClient) { }

  post(usuario: Usuario): Observable<any> {

    return this.httpClient.post(`${Constants.hostApi}/usuarios/`, usuario, { headers: { 'Content-Type': 'application/json' } });

  }

  validarLogin(usuario: Usuario): Observable<any> {
    return this.httpClient.get(`${Constants.hostApi}/usuarios/validar-login/${usuario.login}`);
  }

  login(usuario: Usuario): Observable<Usuario> {

    return this.httpClient.post<Usuario>(`${Constants.hostApi}/usuarios/login`, usuario, { headers: { 'Content-Type': 'application/json' } });

  }

}
