import { Injectable } from '@angular/core';
import { Usuario } from '../models/usuario.model';

@Injectable({
  providedIn: 'root'
})
export class AuthUserService {

  constructor() { }

  startSession(usuario: Usuario) {

    window.localStorage.removeItem("user-auth");

    if (window.localStorage.getItem("user-auth") == null) {

      window.localStorage.setItem("user-auth", JSON.stringify(usuario));
    }

  }

  closeSession() {

    window.localStorage.removeItem("user-auth");


  }

  getSession(): Usuario {

    return JSON.parse(localStorage.getItem("user-auth"));
  }

  get isAuthenticated(): boolean {

    return JSON.parse(localStorage.getItem("user-auth")) != null;
  }

}
