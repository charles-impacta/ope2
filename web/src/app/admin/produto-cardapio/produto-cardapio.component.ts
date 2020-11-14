import { EstabelecimentoService } from './../../../domain/services/estabelecimento.service';
import { HttpErrorResponse } from '@angular/common/http';
import { Component, Injector, OnInit } from '@angular/core';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { ItemCardapio } from 'src/domain/models/item-cardapio.model';
import { ItemCardapioService } from 'src/domain/services/item-cardapio.service';
import { Estabelecimento } from 'src/domain/models/estabelecimento.model';

@Component({
  selector: 'app-produto-cardapio',
  templateUrl: './produto-cardapio.component.html',
  styleUrls: ['./produto-cardapio.component.scss']
})
export class ProdutoCardapioComponent extends AppBaseComponent implements OnInit {

  listProduto: ItemCardapio[] = [];
  listEstabelecimento: Estabelecimento[] = [];
  estabelecimentoSelected: number = 0;

  constructor(injector: Injector, private itemCardapioService: ItemCardapioService, private estabelecimentoService: EstabelecimentoService) {
    super(injector);
  }

  ngOnInit(): void {

    if (this.authUserService.getSession().isAdmin) {


      this.itemCardapioService.list().subscribe((data) => {
        this.listProduto = data;
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });

    } else {
      this.itemCardapioService.getByEstabelecimento(this.authUserService.getSession().id_estabelecimento).subscribe((data) => {
        this.listProduto = data;
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });

    }

  }

  onChange() {

    if (this.estabelecimentoSelected > 0) {

      this.itemCardapioService.getByEstabelecimento(this.estabelecimentoSelected).subscribe((data) => {
        this.listProduto = data;
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });

    }else{
      this.itemCardapioService.list().subscribe((data) => {
        this.listProduto = data;
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });
    }
  }

}
