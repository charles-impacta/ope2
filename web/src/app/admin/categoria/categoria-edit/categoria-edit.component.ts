import { HttpErrorResponse } from '@angular/common/http';
import { Component, Injector, OnInit } from '@angular/core';
import { Validators } from '@angular/forms';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { CategoriaService } from 'src/domain/services/categoria.service';

@Component({
  selector: 'app-categoria-edit',
  templateUrl: './categoria-edit.component.html',
  styleUrls: ['./categoria-edit.component.scss']
})
export class CategoriaEditComponent extends AppBaseComponent implements OnInit {


  submited: boolean = false;

  constructor(injector: Injector, private categoriaService: CategoriaService) {

    super(injector);

    this.frmFormulario = this.fb.group({
      id: [0, [Validators.required, Validators.min(1)]],
      nome: ['', Validators.required]
    });

    const id = this.activeRoute.snapshot.paramMap.get("id");

    if (id !== null) {

      this.categoriaService.get(id).subscribe((data) => {
        this.frmFormulario.patchValue(data);
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });

    }

  }

  ngOnInit(): void {
  }

  onSubmit() {

    this.submited = true;

    if (this.frmFormulario.valid) {
      this.categoriaService.put(this.frmFormulario.value).subscribe((res) => {
        this.toastService.success("Categoria atualizada com sucesso!");
        this.router.navigate(['./admin/categorias']);
      }, (httpError: HttpErrorResponse) => {
        this.toastService.error(httpError.error);
      });
    } else {
      this.toastService.error("Não foi possível cadastrar a categoria, verifique o(s) campo(s) em destaque!");
    }
  }

}
