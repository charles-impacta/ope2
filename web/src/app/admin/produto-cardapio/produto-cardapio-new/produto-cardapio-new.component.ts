import { HttpErrorResponse } from '@angular/common/http';
import { Component, Injector, OnInit } from '@angular/core';
import { Validators } from '@angular/forms';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { Categoria } from 'src/domain/models/categoria.model';
import { CategoriaService } from 'src/domain/services/categoria.service';
import { ItemCardapioService } from 'src/domain/services/item-cardapio.service';

@Component({
  selector: 'app-produto-cardapio-new',
  templateUrl: './produto-cardapio-new.component.html',
  styleUrls: ['./produto-cardapio-new.component.scss']
})
export class ProdutoCardapioNewComponent extends AppBaseComponent implements OnInit {


  listCategorias: Categoria[];

  submited: boolean = false;

  constructor(injector: Injector,
    private itemCardapioService: ItemCardapioService,
    private categoriaService: CategoriaService) {

    super(injector);

    this.frmFormulario = this.fb.group({
      nome: ['', Validators.required],
      descricao: ['', Validators.required],
      ingredientes: ['', Validators.required],
      modo_de_preparo: ['', Validators.required],
      preco: [0, [Validators.required, Validators.min(0.01)]],
      categoria_id: ['', Validators.required],
      estabelecimento_id: [this.authUserService.getSession().id_estabelecimento],
      inativo : [false]
    });
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
      this.itemCardapioService.post(this.frmFormulario.value).subscribe((res) => {
        this.toastService.success("Produto cadastrado com sucesso!");
        this.router.navigate(['./admin/produto-cardapio']);
      },(httpError: HttpErrorResponse)=>{
        this.toastService.error(httpError.error);
      });

    } else {
      this.toastService.error("Não foi possível cadastrar o produto, verifique o(s) campo(s) em destaque!");
    }
  }

}
