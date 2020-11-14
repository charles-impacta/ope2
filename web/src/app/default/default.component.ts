import { Component, OnInit } from '@angular/core';
import { EstabelecimentoService } from 'src/domain/services/estabelecimento.service';

@Component({
  selector: 'app-default',
  templateUrl: './default.component.html',
  styleUrls: ['./default.component.scss']
})
export class DefaultComponent implements  OnInit {

  title = 'Cardápio na Web';
  hasEstabelecimento : boolean = false;
  constructor(private estabelecimentoService : EstabelecimentoService) {
    this.estabelecimentoService.hasEstabelecimento().subscribe((result)=>{
      this.hasEstabelecimento = result;
    });
  }

  ngOnInit(): void {

  }

}
