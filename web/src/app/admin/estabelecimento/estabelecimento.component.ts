import { Component, Injector, OnInit } from '@angular/core';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { Estabelecimento } from 'src/domain/models/estabelecimento.model';
import { ItemCardapio } from 'src/domain/models/item-cardapio.model';
import { EstabelecimentoService } from 'src/domain/services/estabelecimento.service';

@Component({
  selector: 'app-estabelecimento',
  templateUrl: './estabelecimento.component.html',
  styleUrls: ['./estabelecimento.component.scss']
})
export class EstabelecimentoComponent extends AppBaseComponent implements OnInit {

  listEstabelecimento: Estabelecimento[] = [];

  constructor(injector: Injector, private estabelecimentoService: EstabelecimentoService) {
    super(injector);
  }

  ngOnInit(): void {
    this.listEstabelecimento = [];

    this.estabelecimentoService.get(this.authUserService.getSession().id_estabelecimento).subscribe((data) => {
      this.listEstabelecimento.push(data);
    });
  }
}
