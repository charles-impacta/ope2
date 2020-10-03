import { HttpErrorResponse } from '@angular/common/http';
import { Component, Injector, OnInit } from '@angular/core';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { ItemCardapio } from 'src/domain/models/item-cardapio.model';
import { ItemCardapioService } from 'src/domain/services/item-cardapio.service';

@Component({
  selector: 'app-produto-cardapio',
  templateUrl: './produto-cardapio.component.html',
  styleUrls: ['./produto-cardapio.component.scss']
})
export class ProdutoCardapioComponent extends AppBaseComponent implements OnInit {

  listProduto: ItemCardapio[] = [];
  constructor(injector: Injector, private itemCardapioService: ItemCardapioService) {
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

}
