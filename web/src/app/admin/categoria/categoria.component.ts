import { CategoriaService } from './../../../domain/services/categoria.service';
import { Categoria } from './../../../domain/models/categoria.model';
import { Component, Injector, OnInit } from '@angular/core';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-categoria',
  templateUrl: './categoria.component.html',
  styleUrls: ['./categoria.component.scss']
})
export class CategoriaComponent extends AppBaseComponent implements OnInit {

  listCategorias: Categoria[] = [];

  constructor(injector: Injector, private categoriaService: CategoriaService) {
    super(injector);
  }

  ngOnInit(): void {

    this.categoriaService.list().subscribe((data) => {
      this.listCategorias = data;
    }, (httpError: HttpErrorResponse) => {
      this.toastService.error(httpError.error);
    })
  }

}
