import { Component, Injector, OnDestroy, OnInit } from '@angular/core';
import { NavigationEnd } from '@angular/router';
import { AppBaseComponent } from 'src/app/shared/app-base-component';
import { ItemCardapio } from 'src/domain/models/item-cardapio.model';
import { CategoriaService } from 'src/domain/services/categoria.service';
import { EstabelecimentoService } from 'src/domain/services/estabelecimento.service';
import { ItemCardapioService } from 'src/domain/services/item-cardapio.service';

@Component({
  selector: 'app-item-cardapio',
  templateUrl: './item-cardapio.component.html',
  styleUrls: ['./item-cardapio.component.scss']
})
export class ItemCardapioComponent extends AppBaseComponent implements OnInit, OnDestroy {

  listProduto: ItemCardapio[] = [];
  descricaoGrupo : string = "";
  navigationSubscription;

  constructor(injector: Injector,
    private itemCardapioService: ItemCardapioService,
    private estabelecimentoService: EstabelecimentoService,
    private categoriaService: CategoriaService) {

    super(injector);

    if (this.activeRoute.snapshot.paramMap.get("estabelecidomento_id")) {

      this.estabelecimentoService.get(this.activeRoute.snapshot.paramMap.get("estabelecidomento_id")).subscribe((data)=>{
        this.descricaoGrupo = `Loja - ${data.nome}` ;
      });

      this.itemCardapioService.getByEstabelecimentoAtivo(this.activeRoute.snapshot.paramMap.get("estabelecidomento_id")).subscribe((data)=>{
        this.listProduto = data;
      },(error)=>{
        this.toastService.error(error);
      });

    } else if (this.activeRoute.snapshot.paramMap.get("categoria_id")) {

      this.categoriaService.get(this.activeRoute.snapshot.paramMap.get("categoria_id")).subscribe((data)=>{
        this.descricaoGrupo = `${data.nome}` ;
      });


      this.itemCardapioService.getByCategoriaAtivo(this.activeRoute.snapshot.paramMap.get("categoria_id")).subscribe((data)=>{
        this.listProduto = data;
      },(error)=>{
        this.toastService.error(error);
      });
    } else {


      this.itemCardapioService.listAtivos().subscribe((data)=>{
        this.listProduto = data;
      },(error)=>{
        this.toastService.error(error);
      });
    }

  }

  ngOnInit(): void {


  this.navigationSubscription = this.router.events.subscribe((e: any) => {
    // If it is a NavigationEnd event re-initalise the component
    if (e instanceof NavigationEnd) {
      this.initialiseInvites();
    }
  });
}

initialiseInvites() {
  if (this.activeRoute.snapshot.paramMap.get("estabelecidomento_id")) {

    this.estabelecimentoService.get(this.activeRoute.snapshot.paramMap.get("estabelecidomento_id")).subscribe((data)=>{
      this.descricaoGrupo = `Loja - ${data.nome}` ;
    });

    this.itemCardapioService.getByEstabelecimento(this.activeRoute.snapshot.paramMap.get("estabelecidomento_id")).subscribe((data)=>{
      this.listProduto = data;
    },(error)=>{
      this.toastService.error(error);
    });

  } else if (this.activeRoute.snapshot.paramMap.get("categoria_id")) {

    this.categoriaService.get(this.activeRoute.snapshot.paramMap.get("categoria_id")).subscribe((data)=>{
      this.descricaoGrupo = `${data.nome}` ;
    });


    this.itemCardapioService.getByCategoria(this.activeRoute.snapshot.paramMap.get("categoria_id")).subscribe((data)=>{
      this.listProduto = data;
    },(error)=>{
      this.toastService.error(error);
    });
  }
  else {
    this.itemCardapioService.list().subscribe((data)=>{
      this.listProduto = data;
    },(error)=>{
      this.toastService.error(error);
    });
  }

}
ngOnDestroy() {
   // avoid memory leaks here by cleaning up after ourselves. If we
   // don't then we will continue to run our initialiseInvites()
   // method on every navigationEnd event.
   if (this.navigationSubscription) {
      this.navigationSubscription.unsubscribe();
   }
 }

}
