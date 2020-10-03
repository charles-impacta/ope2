import { ItemCardapioService } from './../../../../domain/services/item-cardapio.service';
import { Component, Injector, OnInit } from '@angular/core';
import { Validators } from '@angular/forms';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { HttpErrorResponse } from '@angular/common/http';
import { CategoriaService } from 'src/domain/services/categoria.service';
import { Categoria } from 'src/domain/models/categoria.model';


@Component({
  selector: 'app-produto-cardapio-edit',
  templateUrl: './produto-cardapio-edit.component.html',
  styleUrls: ['./produto-cardapio-edit.component.scss']
})
export class ProdutoCardapioEditComponent extends AppBaseComponent implements OnInit {


  listCategorias: Categoria[];

  submited: boolean = false;

  constructor(injector: Injector,
    private itemCardapioService: ItemCardapioService,
    private categoriaService: CategoriaService) {

    super(injector);

    this.frmFormulario = this.fb.group({
      id: [, [Validators.required, Validators.min(1)]],
      nome: ['', Validators.required],
      descricao: ['', Validators.required],
      ingredientes: ['', Validators.required],
      modo_de_preparo: ['', Validators.required],
      preco: [0, [Validators.required, Validators.min(0.01)]],
      categoria_id: ['', Validators.required],
      estabelecimento_id: [this.authUserService.getSession().id_estabelecimento]
    });

    const id = this.activeRoute.snapshot.paramMap.get("id");

    if (id !== null) {
      this.itemCardapioService.get(id).subscribe((data) => {

        this.frmFormulario.patchValue(data);
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });
    }

  }

  ngOnInit(): void {

    this.categoriaService.list().subscribe(data => {
      this.listCategorias = data;
    }, (httpError: HttpErrorResponse) => {
      this.toastService.error(httpError.error);
    });
  }

  onSubmit() {

    this.submited = true;

    if (this.frmFormulario.valid) {
      this.itemCardapioService.put(this.frmFormulario.value).subscribe((res) => {
        this.toastService.success("Produto atualizado com sucesso!");
        this.router.navigate(['./admin/produto-cardapio']);
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });

    } else {
      this.toastService.error("Não foi possível cadastrar o produto, verifique o(s) campo(s) em destaque!");
    }
  }

}
