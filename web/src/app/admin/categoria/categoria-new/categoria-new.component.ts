import { HttpErrorResponse } from '@angular/common/http';
import { Injector } from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { Validators } from '@angular/forms';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { CategoriaService } from 'src/domain/services/categoria.service';

@Component({
  selector: 'app-categoria-new',
  templateUrl: './categoria-new.component.html',
  styleUrls: ['./categoria-new.component.scss']
})
export class CategoriaNewComponent extends AppBaseComponent implements OnInit {


  submited: boolean = false;

  constructor(injector: Injector, private categoriaService: CategoriaService) {

    super(injector);

    this.frmFormulario = this.fb.group({
      nome: ['', Validators.required]
    });
  }

  ngOnInit(): void {
  }

  onSubmit() {

    this.submited = true;

    if (this.frmFormulario.valid) {
      this.categoriaService.post(this.frmFormulario.value).subscribe((res) => {
        this.toastService.success("Categoria cadastrada com sucesso!");
        this.router.navigate(['./admin/categorias']);
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });
    } else {
      this.toastService.error("Não foi possível cadastrar a categoria, verifique o(s) campo(s) em destaque!");
    }
  }

}
