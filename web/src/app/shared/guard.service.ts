import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthUserService } from 'src/domain/services/auth-user.service';

@Injectable({
  providedIn: 'root'
})
export class GuardService implements CanActivate {

  constructor(private authUserService: AuthUserService, private router: Router) { }
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {
    if(this.authUserService.isAuthenticated){
      return true;
    }else{
      this.authUserService.closeSession();
      this.router.navigate(['/login']);
    }
  }
}
@Injectable({
  providedIn: 'root'
})
export class GuardServiceAdmin implements CanActivate {

  constructor(private authUserService: AuthUserService, private router: Router) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {

    if(this.authUserService.isAuthenticated && this.authUserService.getSession().isAdmin ){
      return true;
    }else{
      this.router.navigate(['/admin']);
    }
  }
}
