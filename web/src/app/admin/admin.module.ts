import { AdminComponent } from './admin.component';
import { EstabelecimentoComponent } from './estabelecimento/estabelecimento.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EstabelecimentoNewComponent } from './estabelecimento/estabelecimento-new/estabelecimento-new.component';
import { EstabelecimentoEditComponent } from './estabelecimento/estabelecimento-edit/estabelecimento-edit.component';
import { ProdutoCardapioComponent } from './produto-cardapio/produto-cardapio.component';
import { ProdutoCardapioNewComponent } from './produto-cardapio/produto-cardapio-new/produto-cardapio-new.component';
import { ProdutoCardapioEditComponent } from './produto-cardapio/produto-cardapio-edit/produto-cardapio-edit.component';
import { SharedModule } from '../shared/shared.module';
import { AppRoutingModule } from '../app-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CategoriaComponent } from './categoria/categoria.component';
import { CategoriaNewComponent } from './categoria/categoria-new/categoria-new.component';
import { CategoriaEditComponent } from './categoria/categoria-edit/categoria-edit.component';
import { CurrencyMaskModule } from 'ngx-currency-mask';
import { NgxMaskModule } from 'ngx-mask';
import { UsuarioComponent } from './usuario/usuario.component';
import { UsuarioEditComponent } from './usuario/usuario-edit/usuario-edit.component';

@NgModule({
  declarations: [EstabelecimentoComponent, AdminComponent, EstabelecimentoNewComponent, EstabelecimentoEditComponent, ProdutoCardapioComponent, ProdutoCardapioNewComponent, ProdutoCardapioEditComponent, CategoriaComponent, CategoriaNewComponent, CategoriaEditComponent, UsuarioComponent, UsuarioEditComponent],
  exports: [AdminComponent],
  imports: [
    CommonModule,
    NgxMaskModule.forRoot(),
    SharedModule,
    ReactiveFormsModule,
    FormsModule,
    AppRoutingModule,
    CurrencyMaskModule
  ]
})
export class AdminModule {

}
