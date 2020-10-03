import { Component, Injector, OnInit } from '@angular/core';
import { Usuario } from 'src/domain/models/usuario.model';
import { AppBaseComponent } from '../shared/app-base-component';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent extends AppBaseComponent implements OnInit {

  usuarioAuth : Usuario;

  constructor(injector: Injector) {
    super(injector);
  }

  ngOnInit(): void {

    this.usuarioAuth = this.authUserService.getSession();
  }



}
