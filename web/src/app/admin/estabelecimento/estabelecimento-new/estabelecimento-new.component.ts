import { Component, Injector, OnInit } from '@angular/core';
import { AppBaseComponent } from 'src/app/shared/app-base-component';

@Component({
  selector: 'app-estabelecimento-new',
  templateUrl: './estabelecimento-new.component.html',
  styleUrls: ['./estabelecimento-new.component.scss']
})
export class EstabelecimentoNewComponent extends AppBaseComponent implements OnInit {

  submited:boolean = false;
  constructor(injector: Injector) {
    super(injector);
  }

  ngOnInit(): void {
  }

  onSubmit(){

  }

}
