
import { Component, Injector, OnInit } from '@angular/core';
import { UsuarioService } from 'src/domain/services/usuario.service';
import { AppBaseComponent } from '../shared/app-base-component';
import { HttpErrorResponse } from '@angular/common/http';
import { Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent extends AppBaseComponent implements OnInit {

  submited: boolean = false;

  constructor(injector: Injector, private usuarioService: UsuarioService) {

    super(injector);

    this.frmFormulario = this.fb.group({
      login: ['', [Validators.required, Validators.email]],
      senha: ['', Validators.required]
    })
  }

  ngOnInit(): void {
  }

  onSubmit() {

    this.submited = true;

    if (this.frmFormulario.valid) {

      this.usuarioService.login(this.frmFormulario.value).subscribe((res) => {
        this.authUserService.startSession(res);
        this.router.navigate(['/admin']);
      }, (httpError: HttpErrorResponse) => {
        this.toastService.warning(httpError.error);
      });


    } else {
      this.toastService.warning("Verifique os campos em destaque!");
    }

  }

}
