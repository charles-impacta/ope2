import { EstabelecimentoNewComponent } from './admin/estabelecimento/estabelecimento-new/estabelecimento-new.component';
import { EstabelecimentoEditComponent } from './admin/estabelecimento/estabelecimento-edit/estabelecimento-edit.component';
import { GuardService } from './shared/guard.service';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminComponent } from './admin/admin.component';
import { CategoriaEditComponent } from './admin/categoria/categoria-edit/categoria-edit.component';
import { CategoriaNewComponent } from './admin/categoria/categoria-new/categoria-new.component';
import { CategoriaComponent } from './admin/categoria/categoria.component';
import { EstabelecimentoComponent } from './admin/estabelecimento/estabelecimento.component';
import { ProdutoCardapioEditComponent } from './admin/produto-cardapio/produto-cardapio-edit/produto-cardapio-edit.component';
import { ProdutoCardapioNewComponent } from './admin/produto-cardapio/produto-cardapio-new/produto-cardapio-new.component';
import { ProdutoCardapioComponent } from './admin/produto-cardapio/produto-cardapio.component';
import { CadastroEstabelecimentoComponent } from './cadastro-estabelecimento/cadastro-estabelecimento.component';
import { DefaultComponent } from './default/default.component';
import { LoginComponent } from './login/login.component';


const routes: Routes = [
  {
    component: DefaultComponent, path: ''
  },
  {
    component: CadastroEstabelecimentoComponent,
    path: 'novo-estabelecimento'
  },
  { path: 'login', component: LoginComponent },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [GuardService],
    children: [{
      path: 'categorias',
      component: CategoriaComponent
    }, {
      path: 'categorias/new',
      component: CategoriaNewComponent
    }, {
      path: 'categorias/edit/:id',
      component: CategoriaEditComponent
    }, {
      path: 'produto-cardapio',
      component: ProdutoCardapioComponent
    }, {
      path: 'produto-cardapio/edit/:id',
      component: ProdutoCardapioEditComponent
    }, {
      path: 'produto-cardapio/new',
      component: ProdutoCardapioNewComponent
    }, {
      path: 'estabelecimento', component: EstabelecimentoComponent
    },
    {
      path: 'estabelecimento/edit/:id',
      component: EstabelecimentoEditComponent
    }, {
      path: 'estabelecimento/new',
      component: EstabelecimentoNewComponent
    },
    { path: '', redirectTo: 'index', pathMatch: 'full' }]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {

}
