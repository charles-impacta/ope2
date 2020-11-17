import { Component, Injector, OnInit } from '@angular/core';
import { EstabelecimentoService } from 'src/domain/services/estabelecimento.service';
import { AppBaseComponent } from '../shared/app-base-component';

@Component({
  selector: 'app-default',
  templateUrl: './default.component.html',
  styleUrls: ['./default.component.scss']
})
export class DefaultComponent extends AppBaseComponent implements  OnInit {

  title = 'Cardápio na Web';
  hasEstabelecimento : boolean = false;
  constructor(injector: Injector,private estabelecimentoService : EstabelecimentoService) {

    super(injector);
    this.estabelecimentoService.hasEstabelecimento().subscribe((result)=>{
      this.hasEstabelecimento = result;
    });
  }

  ngOnInit(): void {

  }

}
