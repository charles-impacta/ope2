import { ActivatedRoute, Router } from '@angular/router';
import { Injector } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { AuthUserService } from 'src/domain/services/auth-user.service';

export abstract class AppBaseComponent {

  frmFormulario: FormGroup;
  fb: FormBuilder;
  activeRoute: ActivatedRoute
  router: Router;
  toastService: ToastrService;
  authUserService: AuthUserService;
  public static autoContrast = false;

  constructor(injector: Injector) {

    this.fb = injector.get(FormBuilder);
    this.activeRoute = injector.get(ActivatedRoute);
    this.router = injector.get(Router);
    this.toastService = injector.get(ToastrService);
    this.authUserService = injector.get(AuthUserService);



  }

  onExit() {

    this.authUserService.closeSession();
    this.router.navigate(['/']);

  }

  static onSetAutoContrast() {
    this.autoContrast = !this.autoContrast;
  }

   getContrast() : boolean {
    return AppBaseComponent.autoContrast;
  }

}
