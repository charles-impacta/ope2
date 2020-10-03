import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit, Injector } from '@angular/core';
import { FormGroup, Validators } from '@angular/forms';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { ItemCardapio } from 'src/domain/models/item-cardapio.model';
import { EstabelecimentoService } from 'src/domain/services/estabelecimento.service';
import { ItemCardapioService } from 'src/domain/services/item-cardapio.service';

@Component({
  selector: 'app-estabelecimento-edit',
  templateUrl: './estabelecimento-edit.component.html',
  styleUrls: ['./estabelecimento-edit.component.scss']
})
export class EstabelecimentoEditComponent extends AppBaseComponent implements OnInit {

  submited: boolean = false;
  listProduto: ItemCardapio[] = [];


  constructor(injector: Injector, private estabelecimentoService: EstabelecimentoService, private itemCardapioService: ItemCardapioService) {
    super(injector);

    this.frmFormulario = this.fb.group({
      nome: ['', Validators.required],
      cnpj: ['', Validators.required]});
  }

  ngOnInit(): void {

    let id_estabelecimento = this.activeRoute.snapshot.paramMap.get('id');

    if (id_estabelecimento != null) {

      this.estabelecimentoService.get(this.authUserService.getSession().id_estabelecimento).subscribe((data) => {
        this.frmFormulario.patchValue(data);
        this.frmFormulario.get('confirmPassword').setValue(data)
      })

      this.itemCardapioService.getByEstabelecimento(id_estabelecimento).subscribe((data) => {
        this.listProduto = data;
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });
    }




  }

  onSubmit() {

  }
  validarPassword(form: FormGroup) {

    return form.get('password').value == form.get('confirmPassword').value ? null : { invalidConfirm: true };
  }
}
