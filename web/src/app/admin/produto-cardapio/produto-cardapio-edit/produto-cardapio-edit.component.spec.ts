import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProdutoCardapioEditComponent } from './produto-cardapio-edit.component';

describe('ProdutoCardapioEditComponent', () => {
  let component: ProdutoCardapioEditComponent;
  let fixture: ComponentFixture<ProdutoCardapioEditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProdutoCardapioEditComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProdutoCardapioEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
