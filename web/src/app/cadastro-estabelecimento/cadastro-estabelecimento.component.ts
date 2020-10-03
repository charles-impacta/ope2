import { UsuarioService } from './../../domain/services/usuario.service';
import { EstabelecimentoService } from './../../domain/services/estabelecimento.service';
import { Component, Injector, OnInit } from '@angular/core';
import { FormGroup, Validators } from '@angular/forms';
import { AppBaseComponent } from '../shared/app-base-component';
import { HttpErrorResponse } from '@angular/common/http';
import { Usuario } from 'src/domain/models/usuario.model';

@Component({
  selector: 'app-cadastro-estabelecimento',
  templateUrl: './cadastro-estabelecimento.component.html',
  styleUrls: ['./cadastro-estabelecimento.component.scss']
})
export class CadastroEstabelecimentoComponent extends AppBaseComponent implements OnInit {

  submited: boolean = false;

  constructor(injector: Injector, private estabelecimentoService: EstabelecimentoService, private usuarioService: UsuarioService) {

    super(injector);

    this.frmFormulario = this.fb.group({
      nome: ['', Validators.required],
      cnpj: ['', Validators.required],
      password: ['', Validators.required],
      confirmPassword: ['', Validators.required],
      login: ['', [Validators.required, Validators.email]],
    }, { validator: this.validarPassword });
  }

  ngOnInit(): void {
  }

  onSubmit() {

    this.submited = true;

    if (this.frmFormulario.valid) {

      this.usuarioService.validarLogin(this.frmFormulario.value).subscribe(res => {

        this.estabelecimentoService.post(this.frmFormulario.value).subscribe((res) => {

          const usuario = new Usuario(this.frmFormulario.get('login').value, this.frmFormulario.get('password').value, res.id, false);

          this.usuarioService.post(usuario).subscribe(res => {
            this.toastService.success("Estabelecimento cadastrado com sucesso");
            this.router.navigate(['/login']);
          }, (error: HttpErrorResponse) => {
            this.toastService.warning(error.error);
          });

        }, (httpError: HttpErrorResponse) => {
          this.toastService.warning(httpError.error);
        });
      }, (httpError: HttpErrorResponse) => {
        this.toastService.warning(httpError.error);
      });

    }

  }

  validarPassword(form: FormGroup) {

    return form.get('password').value == form.get('confirmPassword').value ? null : { invalidConfirm: true };
  }

}
