import { ActivatedRoute, Router } from '@angular/router';
import { Injector } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { AuthUserService } from 'src/domain/services/auth-user.service';
import * as _ from "lodash";
export abstract class AppBaseComponent {

  frmFormulario: FormGroup;
  fb: FormBuilder;
  activeRoute: ActivatedRoute
  router: Router;
  toastService: ToastrService;
  authUserService: AuthUserService;
  public autoContrast = false;

  constructor(injector: Injector) {

    this.fb = injector.get(FormBuilder);
    this.activeRoute = injector.get(ActivatedRoute);
    this.router = injector.get(Router);
    this.toastService = injector.get(ToastrService);
    this.authUserService = injector.get(AuthUserService);
    this.onStartAutoContrast();
  }

  onExit() {

    this.authUserService.closeSession();

    this.router.navigate(['/']);

  }

  onSetAutoContrast() {

      localStorage.setItem("enable-contrast", _.toString(!this.contrast));
  }

  onStartAutoContrast() {

    if(localStorage.getItem("enable-contrast") == null){

      localStorage.setItem("enable-contrast","false");
    }

  }

  get contrast() : boolean {

    return JSON.parse(localStorage.getItem("enable-contrast"));
  }
}
