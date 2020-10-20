import { Component, Injector, OnInit } from '@angular/core';
import { Categoria } from 'src/domain/models/categoria.model';
import { Estabelecimento } from 'src/domain/models/estabelecimento.model';
import { CategoriaService } from 'src/domain/services/categoria.service';
import { EstabelecimentoService } from 'src/domain/services/estabelecimento.service';
import { AppBaseComponent } from '../shared/app-base-component';

@Component({
  selector: 'app-cardapio',
  templateUrl: './cardapio.component.html',
  styleUrls: ['./cardapio.component.scss']
})
export class CardapioComponent extends AppBaseComponent implements OnInit {

  listEstabelecimentos: Estabelecimento[] = [];
  listCategorias: Categoria[] = [];

  constructor(injector: Injector, private estabelecimentoService: EstabelecimentoService, private categoriaService: CategoriaService) {

    super(injector);
    this.estabelecimentoService.list().subscribe((data) => {
      this.listEstabelecimentos = data;
    }, (error) => {
      this.toastService.error(error);
    })

    this.categoriaService.listActive().subscribe((data) => {
      this.listCategorias = data;
    }, (error) => {
      this.toastService.error(error);
    })
  }


  ngOnInit(): void {
  }

  get navbarsExampleDefault(){

    return window.matchMedia("(max-width:360px)").matches ? "navbarsMobile" : "navbars"

  }

  onSetAutoContrast(){
    AppBaseComponent.onSetAutoContrast();
  }

}
