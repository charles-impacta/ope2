import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-status-flag',
  templateUrl: './status-flag.component.html',
  styleUrls: ['./status-flag.component.css']
})
export class StatusFlagComponent{

  @Input() isInativo : boolean = false;
  @Input('text-true') textTrue : string = 'Ativo';
  @Input('text-false') textFalse : string = 'Inativo';
  constructor() { }
}
